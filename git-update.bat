@echo off
cd /d "D:\obsidianProject\portrait-to-landscape"
echo ========================================
echo   Git Pull - Update from GitHub
echo ========================================
echo.
git pull origin master
echo.
if %ERRORLEVEL% EQU 0 (
    echo [OK] Pull completed successfully
) else (
    echo [ERROR] Pull failed, check errors above
)
echo.
pause
