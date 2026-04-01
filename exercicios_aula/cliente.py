import socket

HOST = "127.0.0.1"
PORT = 12340

# Criar socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ligar ao servidor
try:
    client.connect((HOST, PORT))
    print("Ligado ao servidor!\n")

    while True:
        mensagem = input("Tu: ")
        client.send(mensagem.encode())

        resposta = client.recv(1024).decode()

        if not resposta:
            break

        print(f"Servidor: {resposta}")

except Exception as e:
    print("Erro:", e)

# Fechar conexão
client.close()
print("\nLigação terminada.")