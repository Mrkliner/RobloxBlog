import socket as sk
import colorama as color

color.init()

command = 'conn'

while True:
	print (color.Fore.GREEN, end='')
	command = 'conn'
	ip = input('IP: ')
	while command != 'reconn':
		clientsock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
		clientsock.connect((ip, 8080))
		print (color.Fore.BLUE, end='')
		command = input('Data: ')
		if command != 'reconn': clientsock.send(bytes(command, encoding='utf-8'))
		clientsock.close()