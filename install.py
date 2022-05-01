import subprocess

class Install:

    def __init__(self, Software_Path:str):
        self.Software_Path = Software_Path
        self.PowerShell_Command = "powershell.exe "
        
    def Check_Extention(self):

        Software_Path = self.Software_Path
        if Software_Path.endswith("exe") == True: # exe 
            # This PowerShell Command To Install EXE Software.
            CommandLine =  f"Start-Process -FilePath {Software_Path} -Args '/silent /install' -Verb RunAs -Wait;"
        
        elif Software_Path.endswith("msi") == True:
            # This PowerShell Command To Install MSI Software.
            CommandLine = f" msiexec.exe /a {Software_Path} /norestart /passive"

        else:
            # print Error 
            return "Error Open only msi or exe"
        return CommandLine
        
    def install_Software(self):
        
        PowerShell_Command = self.PowerShell_Command
        # Check Software Extention
        CommandLine = Install.Check_Extention(self)
        Command = PowerShell_Command + CommandLine

        try:
            process = subprocess.run(Command, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            return process
        except Exception as e:
            return f"Eror Found Class: Install Function: install_Software Error is {e}"
        
        




    




                
                 





