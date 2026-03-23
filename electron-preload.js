/**
 * Preload script for IPC communication
 */

const { ipcRenderer } = require('electron');

window.electronAPI = {
  quitApp: () => ipcRenderer.send('quit-app'),
};
