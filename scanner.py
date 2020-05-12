"""
Description:
 - Simple Port Scanner for Scanning the important and open ports on a target machine.

Developed By: 
   ______  ___    __        __          __  _____             _ _____ __ __
  / ____ \/   |  / /_______/ /_  ____ _/ /_/ ___/____  ____  (_) ___// // /
 / / __ `/ /| | / //_/ ___/ __ \/ __ `/ __/\__ \/ __ \/ __ \/ / __ \/ // /_
/ / /_/ / ___ |/ ,< (__  ) / / / /_/ / /_ ___/ / /_/ / / / / / /_/ /__  __/
\ \__,_/_/  |_/_/|_/____/_/ /_/\__,_/\__//____/\____/_/ /_/_/\____/  /_/   
 \____/                                                                    
"""

import os
import time
import sys
import socket
from datetime import datetime
from subprocess import check_output
from threading import Thread

#5
# Scanner Thread Class Begins
class MyPortScanner(Thread):
	def __init__(self, target): 
		Thread.__init__(self)
		self.target = target

	def run(self): 
		target = self.target		
		try:
			count = 0
			for port in range(1, 65535):
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
				socket.setdefaulttimeout(1)
				result = s.connect_ex((target,port)) 
				if result == 0:
					count += 1
					print("Port : {0} | Status: OPEN\t".format(port), end="") 
					if count % 4 == 0: print("")				
				s.close()
		except KeyboardInterrupt:
			print("\n Exiting Program")
			sys.exit()
		except socket.gaierror:
			print("Hostname couldn't be resolved")
			sys.exit()
		except socket.error:
			print("Couldn't connect to server")
			sys.exit()
# Scanner Thread Class Ends

# 0
os.system("clear")

# 1 
# Define Target
# Pre-Execution Begins
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) 
else:
	print("Invalid amount of arguement")
	print("Syntax: python3 scanner.py <ip>")
	exit()
# Pre-Execution Ends	

# 2 
# Welcome Section Begins
print("Welcome", check_output("whoami").decode().upper(), end="")
# Welcome Section Begins

#3
# Banner Begins
print("-"*150)
print("Welcome to Port-Scanner..")

banner = """
/-------  ----------  /--------  -----------
|      |  |        |  |       |       |
|      |  |        |  |       |       |
| |-----  |        |  |----\--/       |
| |       |        |  |     \         |
| |       |        |  |      \        |
| |       ----------  |       \       |

--------  --------- /------\  /\      |  /\      |  --------  /--------
|         |         |      |  | \     |  | \     |  |         |       |
|         |         |      |  |  \    |  |  \    |  |         |       |
--------  |         |======|  |   \   |  |   \   |  --------  |----\--/
       |  |         |      |  |    \  |  |    \  |  |         |     \  
       |  |         |      |  |     \ |  |     \ |  |         |      \ 
--------  --------- |      |  |      \/  |      \/  --------  |       \ 
"""
print(banner)
print("Developed By: Akshat Soni - @akshatsoni64 \t\t Guided By: Heath Adams (The Cyber Mentor) - @hmaverickadams")
print("\n*Notes:\n - Please Don't Copy the Code.\n - Contributions and Suggestions are allowed.")
print("-"*150)
# Banner Ends

#4
# Execution Section Ends
print("\nHost: ", target)

t_scan = MyPortScanner(target)
t_scan.start()
t_scan.join()
# Execution Section Ends

#6
# Footer Begins
print("\n{0} *!! ThankYou !!* {1}".format(("-"*66),("-"*66)))
# Footer Ends
                                                              