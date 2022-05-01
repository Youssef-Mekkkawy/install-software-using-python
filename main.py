from install import Install
import os
from termcolor import colored

# Path of Software
Software_Path = "Path Your Software"
# Software Name {Get Name from Path}.
Software_Name = os.path.basename(Software_Path)
# Call Class
proc = Install(Software_Path)
# Call method {Funtion}
process = proc.install_Software()
# Check if File Install.
try:
    if process.returncode == 0:
        print("Installed Successfully:", colored(Software_Name, 'green'))
    elif process.returncode == 1:
        print("Not installed :",colored(Software_Name, 'red'))
except Exception as e:
    print(f"Erro Found Class: Function: No: Error is {e}")
