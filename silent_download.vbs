Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "dist\download_tanks.exe" & chr(34), 0
Set WshShell = Nothing
