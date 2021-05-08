#!/usr/bin/env/ python3

#####################################################################
#																	#
#		This is an automation tool for Linux Privilege Escalation	#
#																	#
# 			It does:												#
#				+ OS, Release, and Kernel information gathering     #
#				+ Root service check                                #
#				+ SUID-GUID check ('can this user sudo anything?')  #
#				+ Check for SUID-GUID abusable binaries             #
#																	#
#####################################################################



# Importing required libraries:
import os


# This function will check for OS, Release, and Kernel information
def OS_CHECK():
	if bit != 0:
		print ('[+] OS/Kernel Check Function')
		# Running some commands in terminal to identify the system
		os.system('uname -a')
		os.system('cat /etc/os-release')
		os.system('cat /etc/issue')
		print ('[+] OS Check CLEARED -> Proceeding with Root Service Check')
		print ('------------------------------------------------------')
		print ('------------------------------------------------------')
		print ('------------------------------------------------------')
		ROOT_SERVICE_CHECK()
	
	else:
		print ('[+] OS/Kernel Check Function')
		os.system('uname -a')
		os.system('cat /etc/os-release')
		os.system('cat /etc/issue')
		GOTOMAIN = input ('[+] Press ENTER to return to MAIN function')
		MAIN()


# This function will check for services running as root
def ROOT_SERVICE_CHECK():
	if bit != 0:
		print ('[+] Root Service Check Function')
		os.system('ps aux | grep root')
		print('[+] Root Service Check CLEARED -> Proceeding with SUID/GUID Check')
		print ('------------------------------------------------------')
		print ('------------------------------------------------------')
		print ('------------------------------------------------------')
		SUID_GUID_CHECK()
	else:	
		print ('[+] Root Service Check Function')
		os.system('ps aux | grep root')
		GOTOMAIN = input ('[+] Press ENTER to return to MAIN function')
		MAIN()


# This function will check for SUID/GUID abusable binaris
def SUID_GUID_CHECK():
	if bit != 0:
		print ('[+] SUID Check Function')
		os.system('find / -perm -u=s -type f 2>/dev/null') # 's' is the SUID bit set for the file permission
		print ('------------------------------------------------------')
		print('[+] GUID check function')
		os.system('find / -perm -g=s -type f 2>/dev/null')
		print ('------------------------------------------------------')
		print ('------------------------------------------------------')
		print ('------------------------------------------------------')
		print ('[+] SUID/GUID Check CLEARED')
		print ('------------------------------------------------------')
		print ('Full Scan Cleared Successfully!!!')
		print ('------------------------------------------------------')
		GOTOMAIN = input ('[+] Press ENTER to return to Main Menu')
		MAIN()
	else:
		print ('[+] SUID/GUID Check Function')
		os.system('find / -perm -u=s -type f 2>/dev/null') # 's' is the SUID bit set for the file permission
		os.system('find / -perm -g=s -type f 2>/dev/null')
		GOTOMAIN = input ('[+] Press ENTER to return to Main Menu')
		MAIN()


# This is the main function that enables options
def MAIN():
	global bit # this is a global variable used to process all the functions if Option 4 is selected
	bit = 0
	print ('[+] Please select one of the following options: ')
	OPTION = input ('''
		[+] 1. OS/Kernel Check
		[+] 2. Root Service Check
		[+] 3. SUID/GUID User Check
		[+] 4. Full Scan (run all)
		[+] 5. To exit

		LPC >>> ''')

	# Selections:
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
		print ('You chose option 4. --- Proceeding with Full Scan')
		bit = bit + 1
		OS_CHECK ()

	elif OPTION == '5':
		print ('You chose option 4. --- Proceeding to EXIT')

	else :
		BAD_OPTION = input ('Invalid option. Press ENTER to continue')
		MAIN()
MAIN()

