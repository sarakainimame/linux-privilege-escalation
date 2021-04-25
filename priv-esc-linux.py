#!/usr/bin/env/ python3


### This is an automation tool for privilege escalation in Linux

# It does:
#	+ OS, Release, and Kernel information gathering
#	+ Root service check
#	+ SUID-GUID check ('can this user sudo anything?')
#	+ Check for SUID-GUID abusable binaries

# Importing the needed libraries:
import os


# This function will check for OS, Release, and Kernel information
def OS_CHECK():
	os.system('clear')
	print ('[+] OS/Kernel check function')
	# Running some commands in terminal to identify the system
	os.system('uname -a')
	os.system('cat /etc/os-release')
	os.system('cat /etc/issue')
	GOTOMAIN = input ('Press ENTER to return to MAIN function')
	MAIN()


# This function will check for services running as root
def ROOT_SERVICE_CHECK():
	os.system('clear')
	print ('[+] Root Service check function')
	GOTOMAIN = input ('Press ENTER to return to MAIN function')
	MAIN()


# This function will check for SUID/GUID abusable binaris
def SUID_GUID_CHECK():
	os.system('clear')
	print ('[+] SUID/GUID check function')
	GOTOMAIN = input ('Press ENTER to return to MAIN function')
	MAIN()

def MAIN():
	os.system('clear')
	print ('[+] Please select one of the following options: ')
	OPTION = input ('''
		[+] 1. OS/Kernel Check
		[+] 2. Root Service Check
		[+] 3. SUID/GUID User Check
		[+] 4. To exit

		LPC >>> ''')

	if OPTION == '1':
		print ('You chose option 1. --- Proceeding to OS/Kernel Check')
		OS_CHECK()

	elif OPTION == '2':
		print ('You chose option 2. --- Proceeding to Root Service Check')
		ROOT_SERVICE_CHECK()

	elif OPTION == '3':
		print ('You chose option 3. --- Proceeding to SUID/GUID User Check')
		SUID_GUID_CHECK()

	elif OPTION == '4':
		print ('You chose option 4. --- Proceeding to EXIT')

	else :
		BAD_OPTION = input ('Invalid option. Press ENTER to continue')
		MAIN()
MAIN()

