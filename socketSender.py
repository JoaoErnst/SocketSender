#!/usr/bin/python3
import socket

print("Interagindo com o Servidor FTP")

ip = input("Digite o IP: ")
porta = 21


usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
meusocket.connect((ip, porta))
banner = meusocket.recv(1024)
print(banner.decode('utf-8'))


meusocket.send(f"USER {usuario}\r\n".encode('utf-8'))
banner = meusocket.recv(1024)
print(banner.decode('utf-8'))


meusocket.send(f"PASS {senha}\r\n".encode('utf-8'))
banner = meusocket.recv(1024)
print(banner.decode('utf-8'))

meusocket.close()
 
