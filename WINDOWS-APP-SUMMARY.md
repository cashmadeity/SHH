# YouTube Learner - Windows App

## What You Have

Three ways to run the YouTube Learner on Windows:

### 1. **Standalone .exe (Recommended) 🎯**

Single executable file, no installation needed.

**Build:**
```bash
npm install -g pkg  # (once)
npm run build-exe
```

**Result:** `YouTubeLearner.exe` (2-5 MB)

**Run:** Double-click `YouTubeLearner.exe`

**Pros:**
- Single file
- Zero setup
- Portable (copy anywhere)
- Starts web server automatically

---

### 2. **Electron App (Native Windows)**

Full Windows app experience.

**Features:**
- System tray icon
- Windows shortcuts
- Native window
- NSIS installer

**Setup:**
```bash
npm install electron --save-dev
npm run electron
```

**Build installer:**
```bash
npm run build-nsis
```

**Pros:**
- Native feel
- Professional installer
- Desktop shortcuts
- System tray integration

---

### 3. **Web Browser (Current)**

Run in any browser.

```bash
npm start
# Then open: http://localhost:9000
```

**Pros:**
- Works on any device
- Easy to update

---

## Quick Start Guide for Windows

### If you just want to run it:

1. **Copy these files to Windows:**
   - `yt-learner-ui.js`
   - `youtube-learner-zero-cost.js`
   - `learning-inbox-manager.js`
   - `youtube-retriever.py`
   - `package.json`
   - `node_modules/` (or run `npm install`)

2. **Install Node.js** (if not already installed):
   - Download from nodejs.org
   - Install (default settings fine)

3. **On Windows, in command prompt:**
   ```
   cd path\to\youtube-learner
   npm install
   node build-windows.bat
   ```

4. **Done!** `YouTubeLearner.exe` is ready

---

### If you want to build a custom installer:

1. Install NSIS: https://nsis.sourceforge.io/download/
2. Run: `npm run build-nsis`
3. Distribute `YouTubeLearner-Setup.exe`

---

## File Structure

```
youtube-learner/
├── yt-learner-ui.js                 (web server)
├── youtube-learner-zero-cost.js     (local processing)
├── learning-inbox-manager.js        (pipeline)
├── youtube-retriever.py             (search)
├── electron-main.js                 (Electron entry)
├── electron-preload.js              (Electron IPC)
├── package.json                     (dependencies)
├── build-windows.bat                (build script)
├── installer.nsi                    (NSIS config)
├── icon.png                         (app icon)
├── BUILD-WINDOWS-APP.md             (detailed guide)
├── memory/                          (learned videos)
└── node_modules/                    (dependencies)
```

---

## Next Steps

1. **Test locally:**
   ```bash
   npm start
   # Open http://localhost:9000
   ```

2. **Build .exe:**
   ```bash
   npm run build-exe
   # Creates YouTubeLearner.exe
   ```

3. **Share:**
   - Send `YouTubeLearner.exe` to anyone
   - They can run it without Node.js

---

## System Requirements (for running .exe)

- Windows 7+ or Windows Server 2008+
- No additional software needed
- ~50 MB disk space for Node.js bundled in .exe

---

**Status:** ✅ Ready to deploy  
**Updated:** 2026-03-23
