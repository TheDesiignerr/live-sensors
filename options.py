from colorama import Fore, Style, init

init(autoreset=True)

def printOptions():
    options ="""
+--------------------------------------------------------------------+   
|    [0] - Setup                                                     | 
|    Sets up all needed packages for this tool                       | 
|    (Only run if this is the first time using this tool)            | 
|    (This action needs sudo permission)                             | 
|                                                                    |
|    [1] - Live Check                                                | 
|    Displays live temp of all detected sensors                      |
|                                                                    |
|    [2] - Interval                                                  | 
|    Sets refresh rate of live logging                               |
|    (Refresh rate is set in seconds)                                |
|    Default: 1                                                      |
|                                                                    |
|    [99] - Exit                                                     | 
|    Exits LiveSensors                                               | 
+--------------------------------------------------------------------+
    """
    print(Fore.RED + options)