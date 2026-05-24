# Wi-riX Framework Installer for Windows
Write-Host "🔥 Wi-riX Framework Installer" -ForegroundColor Cyan
Write-Host "👑 Developer: Wi-riX" -ForegroundColor Yellow

# Create directories
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\Wi-riX\WP_Exploit_Framework" | Out-Null
Set-Location "$env:USERPROFILE\Wi-riX\WP_Exploit_Framework"

# Create subdirectories
@('exploits','reports','shells','targets','logs','config','tests','docs','screenshots') | ForEach-Object {
    New-Item -ItemType Directory -Force -Path $_ | Out-Null
}

Write-Host "[+] Framework installed successfully!" -ForegroundColor Green
Write-Host "[+] Run: python wirix.py" -ForegroundColor Yellow