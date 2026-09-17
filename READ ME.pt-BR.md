# 🌐 Servidor Web com Sockets TCP

> Trabalho prático desenvolvido para a disciplina de **Redes de Computadores — UNISINOS**.

Servidor Web desenvolvido em **Python**, utilizando diretamente **Sockets TCP** para receber e responder a requisições **HTTP/1.1**, sem o uso de frameworks ou servidores Web prontos.

## 🛠️ Tecnologias

* 🐍 Python
* 🔌 TCP Sockets
* 🌐 HTTP/1.1
* 📄 HTML

## ✨ Funcionalidades

* `GET /` → Página principal
* `GET /sobre` → Informações sobre Socket, TCP e HTTP
* `404 Not Found` → Recursos inexistentes
* Exibição das requisições HTTP no terminal
* Comunicação diretamente através de Socket TCP

## ▶️ Como executar

```bash
python servidor_web.py
```

Depois, acesse no navegador:

```text
http://localhost:8080
```

ou:

```text
http://localhost:8080/sobre
```

Para testar o erro `404`:

```text
http://localhost:8080/rota-inexistente
```

## 📡 Funcionamento

```text
Cliente
   │
   │  HTTP GET
   ▼
Socket TCP
   │
   ▼
Servidor
   │
   │  HTTP Response
   ▼
Cliente
```

## 📚 Conceitos

**Socket • TCP • HTTP • IP • Portas • Comunicação Cliente-Servidor**

---

## 👩‍💻 Authors

Developed with 💙 by **Athos Nunes Kolling** & **Júlia Roos Costa**
