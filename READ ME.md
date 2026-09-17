# 🌐 Web Server Using TCP Sockets

> Practical project developed for the **Computer Networks — UNISINOS** course.

A Web server developed in **Python**, using **TCP Sockets** directly to receive and respond to **HTTP/1.1** requests, without using frameworks or ready-made Web servers.

## 🛠️ Technologies

* 🐍 Python
* 🔌 TCP Sockets
* 🌐 HTTP/1.1
* 📄 HTML

## ✨ Features

* `GET /` → Main page
* `GET /sobre` → Information about Sockets, TCP and HTTP
* `404 Not Found` → Non-existing resources
* HTTP requests displayed in the terminal
* Communication directly through TCP Sockets

## ▶️ How to Run

```bash
python servidor_web.py
```

Then open a browser and access:

```text
http://localhost:8080
```

or:

```text
http://localhost:8080/sobre
```

To test the `404` response:

```text
http://localhost:8080/non-existent-route
```

## 📡 How It Works

```text
Client
   │
   │  HTTP GET
   ▼
TCP Socket
   │
   ▼
Server
   │
   │  HTTP Response
   ▼
Client
```

## 📚 Concepts

**Sockets • TCP • HTTP • IP • Ports • Client-Server Communication**

---

## 👩‍💻 Authors

Developed with 💙 by **Athos Nunes Kolling** & **Júlia Roos Costa**
