Write-Host "Applying Mouse & Keyboard Gaming Tweaks..."

# --- Maus ---
Set-ItemProperty -Path "HKCU:\Control Panel\Mouse" -Name MouseSpeed -Value 0
Set-ItemProperty -Path "HKCU:\Control Panel\Mouse" -Name MouseThreshold1 -Value 0
Set-ItemProperty -Path "HKCU:\Control Panel\Mouse" -Name MouseThreshold2 -Value 0

Set-ItemProperty -Path "HKCU:\Control Panel\Mouse" -Name MouseSensitivity -Value 10

Remove-ItemProperty -Path "HKCU:\Control Panel\Mouse" -Name SmoothMouseXCurve -ErrorAction SilentlyContinue
Remove-ItemProperty -Path "HKCU:\Control Panel\Mouse" -Name SmoothMouseYCurve -ErrorAction SilentlyContinue

# --- Tastatur ---
Set-ItemProperty -Path "HKCU:\Control Panel\Keyboard" -Name KeyboardDelay -Value 0
Set-ItemProperty -Path "HKCU:\Control Panel\Keyboard" -Name KeyboardSpeed -Value 31

Write-Host "Mouse & Keyboard Tweaks applied! Bitte neu anmelden oder Windows neu starten."
