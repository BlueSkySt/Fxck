import time
import os
import sys 
import colorama
from colorama import Fore, Style, init
colorama.init()

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)

def slowprints(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.06)

def fastprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.1/10)

def fastprints(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.01)

def main():
    os.system("clear")
    time.sleep(1)
    fastprints(Fore.GREEN + """
            __   
           /  \   
           |  |  
           |  |
         __|  |__
        /  |  |  \__ 
      __|  |  |  |  |
     /  /        |  |
     \              |
      \             /
       \___________/

    """)
    slowprints("YOU'VE BEEN HACKED ! HAHAHAAHAHA")



if __name__ == "__main__":
    main()
