# Wi-riX Framework Updater
Write-Host "🔄 Updating Wi-riX Framework..." -ForegroundColor Cyan

# Pull latest changes
git pull origin main

# Install/update requirements
pip install -r requirements.txt --upgrade

Write-Host "[+] Update complete!" -ForegroundColor Green
Write-Host "[+] Run: python wirix.py" -ForegroundColor Yellow