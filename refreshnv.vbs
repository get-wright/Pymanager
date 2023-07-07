Set objShell = CreateObject("Wscript.Shell")
Set colSystemEnvVars = objShell.Environment("System")
Set colUserEnvVars = objShell.Environment("User")
For Each strItem in colSystemEnvVars
    Wscript.Echo strItem
Next
For Each strItem in colUserEnvVars
    Wscript.Echo strItem
Next