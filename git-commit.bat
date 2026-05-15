@echo off
cd /d "D:\obsidianProject\portrait-to-landscape"
echo ========================================
echo   Git Commit and Push to GitHub
echo ========================================
echo.

:: Check if there are any changes
git status --porcelain >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo [INFO] No changes detected, nothing to commit
    echo.
    pause
    exit /b 0
)

echo Changed files:
echo.
git status --short
echo.

:: Input commit message
set msg=
set /p msg="Enter commit message (press Enter for default): "
if "%msg%"=="" (
    git add -A
    git commit -m "update"
) else (
    git add -A
    git commit -m "%msg%"
)

if %ERRORLEVEL% EQU 0 (
    echo.
    echo [OK] Commit done, pushing to GitHub...
    echo.
    git push origin master
    if %ERRORLEVEL% EQU 0 (
        echo [OK] Push completed
    ) else (
        echo [ERROR] Push failed, check network or permissions
    )
) else (
    echo [INFO] Nothing to commit
)

echo.
pause
