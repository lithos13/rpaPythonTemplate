$exclude = @("venv", "RPA_Template.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "RPA_Template.zip" -Force