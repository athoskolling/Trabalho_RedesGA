import socket  # Importa a biblioteca padrão para uso de sockets

# Cria o socket com IPv4 (AF_INET) e protocolo TCP (SOCK_STREAM)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket ao IP e à porta
server.bind(('localhost', 8080))

# Coloca o socket em modo de escuta, aguardando conexões
server.listen()

print("Servidor Web aguardando conexão na porta 8080")

# Loop para receber e responder mensagens
while True:

    # Aceita uma conexão (bloqueante)
    conn, addr = server.accept()
    print(f"Conectado por {addr}")

    data = conn.recv(1024)  # Lê até 1024 bytes
    if not data:            # Se não recebeu dados, encerra
        conn.close()
        continue

    requisicao = data.decode('utf-8')
    print("REQUISIÇÃO RECEBIDA: ")
    print(requisicao)

    primeira_linha = requisicao.splitlines()[0] # Divide a requisição em linhas e pega a primeira

    parts = primeira_linha.split(" ") # Divide a primeira linha em partes (método, caminho, versão)

    route = parts[1]

    print("Rota solicitada: ", route)

    if route == "/":
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Bem-vindo à página inicial!</h1>"
    elif route == "/sobre":
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1> ADICIONAR AS INFOS </h1><p>Esta é a página sobre.</p>"
    else:
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<h1>Página não encontrada</h1>"

    conn.sendall(response.encode('utf-8'))  # Converte a resposta para bytes e envia ao cliente

    conn.close()  # Fecha a conexão
    print("Conexão encerrada.")




#te amo athos kolling beijo te amo julia roos costa, voce esta dentro do meu coração
#teste git commit