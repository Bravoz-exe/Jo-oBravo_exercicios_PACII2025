import socket

HOST = "127.0.0.1"
PORT = 12340

# Criar socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Permite reutilizar a porta
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Ligar ao endereço
server.bind((HOST, PORT))

# Ficar à espera de conexões
server.listen()

print(f"Servidor ativo em {HOST}:{PORT}")
print("A aguardar cliente...\n")

# Aceitar cliente
client_socket, addr = server.accept()
print(f"Cliente ligado: {addr}\n")

# Comunicação contínua
try:
    while True:
        mensagem = client_socket.recv(1024).decode()

        if not mensagem:
            break

        print(f"Cliente: {mensagem}")

        resposta = input("Tu: ")
        client_socket.send(resposta.encode())

except Exception as e:
    print("Erro:", e)

# Fechar conexões
client_socket.close()
server.close()
print("\nServidor encerrado.")