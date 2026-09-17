import socket  # Importa a biblioteca padrão para uso de sockets

# Cria o socket com IPv4 (AF_INET) e protocolo TCP (SOCK_STREAM)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket ao IP e à porta
server.bind(('localhost', 8080))

# Coloca o socket em modo de escuta, aguardando conexões
server.listen()

print("Servidor TCP aguardando conexão...")

# Aceita uma conexão (bloqueante)
conn, addr = server.accept()
print(f"Conectado por {addr}")

# Loop para receber e responder mensagens
while True:
    data = conn.recv(1024)  # Lê até 1024 bytes
    if not data:            # Se não recebeu dados, encerra
        break
    conn.sendall(data)      # Envia de volta os mesmos dados

conn.close()  # Fecha a conexão
print("Conexão encerrada.")
print()
