# Build YouTube Learner Windows App

Two ways to run on Windows:

## Option 1: Standalone Executable (Simplest)

Uses `pkg` to bundle Node.js + app into a single .exe file.

### Setup (do once):
```bash
npm install -g pkg
```

### Build:
```bash
npm run build-exe
```

Output: `YouTubeLearner.exe` (standalone, no dependencies)

**On Windows:**
1. Download `YouTubeLearner.exe`
2. Double-click to run
3. App opens automatically on port 9000

---

## Option 2: Electron App (Native Windows App)

Full native Windows experience with system tray, shortcuts, installer.

### Prerequisites:
- Node.js installed
- NSIS (for installer): https://nsis.sourceforge.io/download/

### Build:
```bash
npm install electron --save-dev
npm run electron
```

**Development:**
```bash
npm run electron-dev
```

**Production Build (with Installer):**
```bash
npm run build-exe          # Creates executable
npm run build-nsis         # Creates .exe installer
```

---

## Option 3: Web Browser (Current Setup)

Keep using the browser version:
```bash
npm start
```

Then open: `http://localhost:9000`

---

## Recommended: Use Option 1 (pkg)

**Why:**
- Single .exe file (2-5 MB)
- No external dependencies
- Just works on Windows
- Fast startup

**Steps:**
1. Install pkg: `npm install -g pkg`
2. Run: `npm run build-exe`
3. Share `YouTubeLearner.exe` with anyone

---

## Troubleshooting

**"node not found"**
- Install Node.js from nodejs.org
- Restart terminal

**"Port 9000 already in use"**
- Change PORT in yt-learner-ui.js
- Or kill process: `netstat -ano | findstr 9000` → `taskkill /pid <PID> /F`

**Electron won't start**
- `npm install electron --save-dev` again
- Check Node version: `node -v` (should be 14+)

---

**Status:** ✅ Ready to build  
**Updated:** 2026-03-23
