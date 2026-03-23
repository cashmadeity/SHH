; YouTube Learner Windows Installer
; Built with NSIS (Nullsoft Scriptable Install System)

!include "MUI2.nsh"

; Basic Settings
Name "YouTube Learner"
OutFile "YouTubeLearner-Setup.exe"
InstallDir "$PROGRAMFILES\YouTubeLearner"
ShowInstDetails show
ShowUninstDetails show

; UI Settings
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

; Installer sections
Section "Install YouTube Learner"
  SetOutPath "$INSTDIR"
  
  ; Copy all app files
  File /r "dist\*.*"
  
  ; Create Start Menu shortcuts
  CreateDirectory "$SMPROGRAMS\YouTubeLearner"
  CreateShortCut "$SMPROGRAMS\YouTubeLearner\YouTube Learner.lnk" "$INSTDIR\YouTubeLearner.exe"
  CreateShortCut "$SMPROGRAMS\YouTubeLearner\Uninstall.lnk" "$INSTDIR\Uninstall.exe"
  
  ; Create Desktop shortcut
  CreateShortCut "$DESKTOP\YouTube Learner.lnk" "$INSTDIR\YouTubeLearner.exe"
  
  ; Create uninstaller
  WriteUninstaller "$INSTDIR\Uninstall.exe"
  
  ; Registry entries for Add/Remove Programs
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\YouTubeLearner" "DisplayName" "YouTube Learner"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\YouTubeLearner" "UninstallString" "$INSTDIR\Uninstall.exe"
SectionEnd

; Uninstaller section
Section "Uninstall"
  RMDir /r "$INSTDIR"
  RMDir /r "$SMPROGRAMS\YouTubeLearner"
  Delete "$DESKTOP\YouTube Learner.lnk"
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\YouTubeLearner"
SectionEnd
