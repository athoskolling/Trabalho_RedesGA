import socket  # Importa a biblioteca padrão para uso de sockets

# Cria o socket com IPv4 (AF_INET) e protocolo TCP (SOCK_STREAM)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket ao IP e à porta (onde o servidor vai ficar disponível)
server.bind(('localhost', 8080))

# Coloca o socket em modo de escuta, aguardando conexões
server.listen()

print("Servidor Web aguardando conexao na porta 8080")

# Loop que mantem o servidor rodando para receber e responder mensagens (requisições)
while True:

    # Aceita uma conexão (bloqueante)
    conn, addr = server.accept()
    print(f"\nConectado por {addr}")

    # Recebe a requisição enviada pelo navegador
    data = conn.recv(1024)  # Lê até 1024 bytes
    if not data:            # Se não recebeu dados, encerra
        conn.close()
        continue

    # Converte os bytes recebidos em texto
    requisicao = data.decode('utf-8')
    print("REQUISICAO RECEBIDA: ")
    print(requisicao)

    # Pega a primeira linha, por exemplo: GET /sobre HTTP/1.1
    # Separa método, rota e versão HTTP
    primeira_linha = requisicao.splitlines()[0] # Divide a requisição em linhas e pega a primeira
    parts = primeira_linha.split(" ") # Divide a primeira linha em partes (método, caminho, versão)

    metodo = parts[0]
    route = parts[1]
    versao_http = parts[2]

    print("Metodo:", metodo)
    print("Rota solicitada:", route)
    print("Versao HTTP:", versao_http)

    # O servidor aceita apenas requisições GET
    if metodo != "GET":
        response = (
            "HTTP/1.1 405 Method Not Allowed\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            "Connection: close\r\n"
            "\r\n"
            "<h1>405 - Metodo nao permitido</h1>"
            "<p>Este servidor aceita apenas requisicoes GET.</p>"
        )

    # Página inicial
    elif route == "/":
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            "Connection: close\r\n"
            "\r\n"
            "<html>"
            "<head>"
            "<title>Pagina Inicial</title>"
            "</head>"
            "<body>"
            "<h1>Bem-vindo a pagina inicial!</h1>"
            "<p>Servidor Web desenvolvido utilizando Socket TCP.</p>"
            '<p><a href="/sobre">Acessar pagina Sobre</a></p>'
            "</body>"
            "</html>"
            )

    # Página "sobre", com explicações sobre Socket, TCP e HTTP
    elif route == "/sobre":
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            "Connection: close\r\n"
            "\r\n"
            "<html>"
            "<head>"
            "<title>Sobre</title>"
            "</head>"
            "<body>"

            "<h1>Sobre o servidor</h1>"

            "<h2>Socket</h2>"
            "<p>"
            "Socket é um ponto de comunicação que permite a troca de dados "
            "entre aplicações através de uma rede. Ele funciona como uma ligação "
            "entre dois dispositivos, permitindo o envio e o recebimento de informações."
            "</p>"

            "<p>"
            "Para que os dados cheguem ao lugar certo, o socket utiliza um número "
            "de porta. A porta identifica qual aplicação deve receber aquela informação "
            "dentro do computador, como se fosse o número de um apartamento dentro de um prédio."
            "</p>"

            "<h2>TCP</h2>"
            "<p>"
            "TCP, ou Transmission Control Protocol, é um protocolo da camada de transporte "
            "que ajuda a garantir que os dados cheguem corretamente ao destino. "
            "Ele organiza os dados em partes e verifica se tudo chegou na ordem certa. "
            "Se alguma parte se perder durante o caminho, ela pode ser enviada novamente."
            "</p>"

            "<h2>HTTP</h2>"
            "<p>"
            "HTTP, ou Hypertext Transfer Protocol, é um protocolo usado na comunicação "
            "entre o navegador e um servidor Web. Quando acessamos um site, o navegador "
            "envia uma requisição para o servidor pedindo os dados da página. Depois, "
            "o servidor responde enviando as informações necessárias para que o conteúdo "
            "seja exibido na tela."
            "</p>"

            '<p><a href="/">Voltar para a página inicial</a></p>'

            "</body>"
            "</html>"
        )

    # Qualquer outra rota retorna 404
    else:
        response = (
            "HTTP/1.1 404 Not Found\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            "Connection: close\r\n"
            "\r\n"
            "<html>"
            "<head>"
            "<title>404</title>"
            "</head>"
            "<body>"
            "<h1>404 - Pagina nao encontrada</h1>"
            "<p>O recurso solicitado nao existe neste servidor.</p>"
            '<p><a href="/">Voltar para a pagina inicial</a></p>'
            "</body>"
            "</html>"
        )

    # Envia a resposta para o navegador
    conn.sendall(response.encode('utf-8'))  # Converte a resposta para bytes e envia ao cliente
    print("Resposta enviada:", response.splitlines()[0]) #Exibe a primeira linha da resposta


    # Fecha a conexão atual e volta a esperar outra
    conn.close()
    print("Conexao encerrada.")
