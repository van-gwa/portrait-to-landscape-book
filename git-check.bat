@echo off
cd /d "D:\obsidianProject\portrait-to-landscape"
echo ========================================
echo   Git Status Check
echo ========================================
echo.

:: Check if there are uncommitted changes
git status --porcelain >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [OK] Working tree clean, nothing to commit
    echo.
    pause
    exit /b 0
)

echo [INFO] Uncommitted changes detected:
echo.
git status --short
echo.

:: Count files
set count=0
for /f "delims=" %%i in ('git status --porcelain') do set /a count+=1
echo ----------------------------------------
echo   Total: %count% file(s) changed
echo ========================================
echo.

set confirm=
set /p confirm="Commit now? (y/n): "
if /i "%confirm%"=="y" (
    call "%~dp0git-commit.bat"
)

echo.
pause
