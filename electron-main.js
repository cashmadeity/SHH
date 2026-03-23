/**
 * YOUTUBE LEARNER - Electron Main Process
 * Native Windows/macOS/Linux app
 */

const { app, BrowserWindow, Menu, ipcMain, Tray, nativeImage } = require('electron');
const path = require('path');
const { spawn } = require('child_process');
const fs = require('fs');

let mainWindow;
let tray;
let serverProcess;
const PORT = 9000;

// ============================================================================
// CREATE WINDOW
// ============================================================================

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1400,
    height: 900,
    minWidth: 800,
    minHeight: 600,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'electron-preload.js'),
    },
    icon: path.join(__dirname, 'icon.png'),
  });

  mainWindow.loadURL(`http://localhost:${PORT}`);

  // DevTools in dev mode
  // mainWindow.webContents.openDevTools();

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

// ============================================================================
// START WEB SERVER
// ============================================================================

function startServer() {
  return new Promise((resolve) => {
    const serverPath = path.join(__dirname, 'yt-learner-ui.js');
    
    serverProcess = spawn('node', [serverPath], {
      cwd: __dirname,
      stdio: 'pipe',
    });

    serverProcess.on('error', (err) => {
      console.error('Server error:', err);
    });

    // Wait for server to be ready
    setTimeout(() => {
      resolve();
    }, 2000);
  });
}

// ============================================================================
// SYSTEM TRAY
// ============================================================================

function createTray() {
  // Create a simple icon (white square)
  const trayIcon = nativeImage.createFromPath(path.join(__dirname, 'icon.png'));
  tray = new Tray(trayIcon);

  const contextMenu = Menu.buildFromTemplate([
    {
      label: 'Show',
      click: () => {
        mainWindow.show();
      },
    },
    {
      label: 'Quit',
      click: () => {
        app.quit();
      },
    },
  ]);

  tray.setContextMenu(contextMenu);
  tray.on('double-click', () => {
    mainWindow.show();
  });
}

// ============================================================================
// APP LIFECYCLE
// ============================================================================

app.on('ready', async () => {
  try {
    await startServer();
    createWindow();
    createTray();
  } catch (err) {
    console.error('Failed to start:', err);
    app.quit();
  }
});

app.on('window-all-closed', () => {
  // On macOS, keep app running
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  // On macOS, re-open window
  if (mainWindow === null) {
    createWindow();
  }
});

app.on('quit', () => {
  // Kill server process
  if (serverProcess) {
    serverProcess.kill();
  }
});

// ============================================================================
// IPC: QUIT APP
// ============================================================================

ipcMain.on('quit-app', () => {
  app.quit();
});
