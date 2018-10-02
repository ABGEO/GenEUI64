#!/usr/bin/python3

print()
print("Welcome to")
print("  ____            _____ _   _ ___ __   _  _   ")
print(" / ___| ___ _ __ | ____| | | |_ _/ /_ | || |  ")
print("| |  _ / _ \ '_ \|  _| | | | || | '_ \| || |_ ")
print("| |_| |  __/ | | | |___| |_| || | (_) |__   _|")
print(" \____|\___|_| |_|_____|\___/|___\___/   |_|  ")
print()
print("IPv6 Interface ID generator")
print("        	           {Directed ByABGEO}")
print()

def ConvertBase(num, To=10, From=10):
	if isinstance(num, str):
		n = int(num, From)
	else:
		n = int(num)

	alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	if n < To:
		return alphabet[n]
	else:
		return ConvertBase(n // To, To) + alphabet[n % To]

def EnterMAC():
	mac = str(input ("Enter MAC Adress (Example : B6CF18D6708F):  "))

	if len(mac) != 12:
		print ("Invalid MAC Adress! Try Again!")
		EnterMAC()

	return mac

MAC = EnterMAC()

ChBit = ConvertBase(MAC[1:2], From=16, To=2)

if len(ChBit) != 4:
	ChBit = ((4-len(ChBit))*'0') + ChBit

if ChBit[2] == '1':
	ChBit = ChBit[:2] + '0' + ChBit[3]
else:
	ChBit = ChBit[:2] + '1' + ChBit[3]

print ("Interface ID: " + MAC[:1] + ConvertBase(ChBit, From=2, To=16) + MAC[2:6] + "FFFE" + MAC[6:])
