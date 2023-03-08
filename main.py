import os
import colorama
import urllib.request
from colorama import Fore

os.system("title JOKR - CMD BYPASS v1.0.0a")

gay = Fore.GREEN + """
 88888  dP"Yb  
    88 dP   Yb 
o.  88 Yb   dP 
"bodP'  YbodP  
""" + Fore.MAGENTA + """
88  dP 88""Yb  
88odP  88__dP  
88"Yb  88"Yb   
b88 Yb 88  Yb\n"""
print(gay)
print(Fore.GREEN + "Version:" + Fore.MAGENTA + " v1.0.0a")
print(Fore.GREEN + "C" + Fore.MAGENTA + "M" + Fore.GREEN + "D" + " " + Fore.MAGENTA + "B" + Fore.GREEN + "Y" + Fore.MAGENTA + "P" + Fore.GREEN + "A" + Fore.MAGENTA + "S" + Fore.GREEN + "S\n")
print(Fore.GREEN + "Type" + Fore.MAGENTA + " 'proxy' " + Fore.GREEN + "to load up the proxy.")

def main():
    command = input(Fore.GREEN + "CMD " + Fore.MAGENTA + "-> " + Fore.LIGHTGREEN_EX + "")
    if command == "proxy":
        print(Fore.GREEN + "proxy URL" + Fore.MAGENTA + "->" + Fore.LIGHTGREEN_EX + " https://brainmaths.rover666.repl.co")
        urllib.request.urlopen("https://brainmaths.rover666.repl.co")
        main()
        
    os.system(command)
    main()

main()