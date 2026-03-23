@echo off
REM YouTube Learner - Windows Build Script

echo.
echo ================================
echo  YouTube Learner - Windows Build
echo ================================
echo.

REM Check if pkg is installed
npm list -g pkg > nul 2>&1
if errorlevel 1 (
    echo Installing pkg globally...
    npm install -g pkg
)

echo.
echo Building standalone .exe...
npm run build-exe

if exist YouTubeLearner.exe (
    echo.
    echo ✅ SUCCESS!
    echo YouTubeLearner.exe created
    echo.
    echo Run it:
    echo   YouTubeLearner.exe
    echo.
    echo Then open:
    echo   http://localhost:9000
    echo.
) else (
    echo.
    echo ❌ Build failed
    echo Check error messages above
    echo.
)

pause
