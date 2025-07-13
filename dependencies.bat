@echo off
echo === WhatsApp Group Automation Dependency Installer ===

:: Initialize npm if package.json doesn't exist
if not exist package.json (
    echo Initializing npm project...
    npm init -y
)

:: Install required packages
echo Installing required Node.js packages...

npm install whatsapp-web.js puppeteer csv-parser qrcode-terminal

echo.
echo ✅ Dependencies installed successfully!
echo.
pause
