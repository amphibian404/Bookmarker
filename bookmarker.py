#python3
from colorama import Fore
import os

print(f'''
                                                                                                                
                             {Fore.GREEN},---.                   ,--.     ,--.,--.   ,--.                  {Fore.RED},---.  {Fore.GREEN},--.    {Fore.RED},---. 
                            {Fore.GREEN}/  O  \ ,--,--,--. ,---. |  ,---. `--'|  |-. `--' ,--,--.,--,--,  {Fore.RED}/    | {Fore.GREEN}/    \  {Fore.RED}/    | 
                           {Fore.GREEN}|  .-.  ||        || .-. ||  .-.  |,--.| .-. ',--.' ,-.  ||      \{Fore.RED}/  '  |{Fore.GREEN}|  ()  |{Fore.RED}/  '  | 
                           {Fore.GREEN}|  | |  ||  |  |  || '-' '|  | |  ||  || `-' ||  |\ '-'  ||  ||  |{Fore.RED}'--|  | {Fore.GREEN}\    / {Fore.RED}'--|  | 
                           {Fore.GREEN}`--' `--'`--`--`--'|  |-' `--' `--'`--' `---' `--' `--`--'`--''--'{Fore.RED}   `--'  {Fore.GREEN}`--'     {Fore.RED}`--' 
                                              {Fore.GREEN}`--'                                                                  
                                        {Fore.GREEN}[=]----------{Fore.MAGENTA}Author: {Fore.YELLOW}Amphibian404{Fore.GREEN}-----------------------------[=]
                                        {Fore.GREEN}[=]----------{Fore.MAGENTA}GitHub: {Fore.YELLOW}https://github.com/amphibian404{Fore.GREEN}----------[=]
                                        {Fore.GREEN}[=]----------{Fore.MAGENTA}Mail: {Fore.YELLOW}amphibian404@protonmail.com{Fore.GREEN}----------------[=]


{Fore.YELLOW} ___________________________________                                     
{Fore.YELLOW}|      |                            |
{Fore.YELLOW}| TOOL | BOOKMARKER + EXTRACTOR TOOL|
{Fore.YELLOW}|______|____________________________|
                                        
                                        

1.{Fore.GREEN} BOOKMARKER
     
      ''')



Option_S=str(input(Fore.GREEN+'RESPONSE -> ')).upper()
word=input(Fore.GREEN+'ENTER SPECIFIC WORD TO BOOKMARK -> ')
FileName = input(Fore.GREEN+'ENTER TARGET FILE (target.txt) -> ')
ffsave=input(Fore.GREEN+'ENTER FILE TO SAVE REZ (save.txt)-> ')
FFile = open(FileName).read().splitlines()
FFList=len(FFile)
print(f'{Fore.YELLOW}TOTAL LINES : {Fore.MAGENTA}{FFList}')
count = 0
    
for ui in FFile:
    if word in ui:
        print(f"{Fore.YELLOW}TOTAL BOOKMARK MATCH : {Fore.MAGENTA}{count}",end="\r")
        count += 1
        fu=open(ffsave,'a+')
        fu.write(ui)
    else:
        pass    
print(f"{Fore.YELLOW}TOTAL BOOKMARK MATCH : {Fore.MAGENTA}{count}")        
