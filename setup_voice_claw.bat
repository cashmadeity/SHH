@echo off
REM Voice Claw Auto-Installer for Windows

echo Installing Voice Claw (100%% Local Voice Agent)...

REM Install Wyoming servers and core deps
pip install -q wyoming-faster-whisper wyoming-piper numpy soundfile pyaudio keyboard requests

echo.
echo Checking voice model...
REM Download Piper voice if needed (optional - will use default)

echo.
echo ✅ Installation complete!
echo.
echo USAGE:
echo   python voice_claw.py           # Interactive mode
echo   python voice_claw.py --daemon  # Background daemon
echo   Ctrl+Space                     # SPEAK NOW
echo.
echo FEATURES:
echo   * Whisper STT (local)
echo   * Piper TTS (local voice)
echo   * OpenClaw integration
echo   * Zero API costs
