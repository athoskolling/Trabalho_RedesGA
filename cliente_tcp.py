import socket

# Cria o socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor na porta 12345
client.connect(('localhost', 12345))

# Envia dados (em bytes)
mensagem = ("Olá, servidor! Tudo bem? Como você está?")
client.sendall(mensagem.encode('utf-8'))

# Recebe resposta
data = client.recv(1024)

print('Recebido:', data.decode('utf-8'))  # Converte de bytes para string

client.close()  # Fecha o socket
print()
