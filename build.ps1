$exclude = @("venv", "RPA_ProcesoPrepa.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "RPA_ProcesoPrepa.zip" -Force