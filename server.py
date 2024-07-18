import socket
import threading
import keyboard  # Essa biblioteca não é padrão // utilizar "pip install keyboard"
import os


def handle_client(client_socket, clients, clients_lock):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            # Detecta do cliente a questão enviada e retorna a resposta correta e a correção feita

            if "Questão1" in message:
                correct_a = "682"
                correct_b = "101100100"
                if "Questão1_a" in message:
                    if message.replace("Questão1_a:", "") == correct_a:
                        result = "Correto"
                    else:
                        result = "Incorreto"
                    client_socket.send(result.encode())

                if "Questão1_b" in message:
                    if message.replace("Questão1_b:", "") == correct_b:
                        result = "Correto"
                    else:
                        result = "Incorreto"
                    client_socket.send(result.encode())

                if "Questão1_resposta" in message:
                    client_socket.send(f"Resposta correta Item (a): {correct_a}\n"
                                       f"Resposta correta item (b): {correct_b}".encode())

            if "Questão2" in message:
                correct_a = "10111110 válido"
                correct_b = "00110101 válido"
                if "Questão2_a" in message:
                    if message.replace("Questão2_a:", "") == correct_a:
                        result = "Correto"
                    else:
                        result = "Incorreto"
                    client_socket.send(result.encode())

                if "Questão2_b" in message:
                    if message.replace("Questão2_b:", "") == correct_b:
                        result = "Correto"
                    else:
                        result = "Incorreto"
                    client_socket.send(result.encode())

                if "Questão2_resposta" in message:
                    client_socket.send(f"Resposta correta Item (a): {correct_a}\n"
                                       f"Resposta correta item (b): {correct_b}".encode())

            if "Questão3" in message:
                correct_a = "11110111"
                if "Questão3_a" in message:
                    if message.replace("Questão3_a:", "") == correct_a:
                        result = "Correto"
                    else:
                        result = "Incorreto"
                    client_socket.send(result.encode())

                if "Questão3_resposta" in message:
                    client_socket.send(f"Resposta correta: {correct_a}".encode())

            if "Questão4" in message:
                correct_a = "11000100001110111000110000000000"
                correct_b = "C43B8C00"
                if "Questão4_a" in message:
                    if message.replace("Questão4_a:", "") == correct_a:
                        result = "Correto"
                    else:
                        result = "Incorreto"
                    client_socket.send(result.encode())

                if "Questão4_b" in message:
                    if message.replace("Questão4_b:", "").upper() == correct_b:
                        result = "Correto"
                    else:
                        result = "Incorreto"
                    client_socket.send(result.encode())

                if "Questão4_resposta" in message:
                    client_socket.send(f"Resposta correta Item (a): {correct_a}\n"
                                       f"Resposta correta item (b): {correct_b}".encode())

            if "Questão5" in message:
                correct_a = "53 65 72 61 3F"
                correct_b = "53 65 72 C3 A1 3F"
                if "Questão5_a" in message:
                    if message.replace("Questão5_a:", "").upper() == correct_a:
                        result = "Correto"
                    else:
                        result = "Incorreto"
                    client_socket.send(result.encode())

                if "Questão5_b" in message:
                    if message.replace("Questão5_b:", "").upper() == correct_b:
                        result = "Correto"
                    else:
                        result = "Incorreto"
                    client_socket.send(result.encode())

                if "Questão5_resposta" in message:
                    client_socket.send(f"Resposta correta Item (a): {correct_a}\n"
                                       f"Resposta correta item (b): {correct_b}".encode())

            if "Questão6" in message:
                correct_a = "!(B+C+D).!E+!(A+B+D).C.E"
                if "Questão6_a" in message:
                    if message.replace("Questão6_a:", "").upper().replace(" ", "") == correct_a:
                        result = "Correto"
                    else:
                        result = "Incorreto"
                    client_socket.send(result.encode())

                if "Questão6_resposta" in message:
                    client_socket.send(f"Resposta correta: {correct_a}".encode())

            if "Questão7" in message:
                correct_a = "ACB=E"
                if "Questão7_a" in message:
                    if message.replace("Questão7_a:", "").upper() == correct_a:
                        result = "Correto"
                    else:
                        result = "Incorreto"
                    client_socket.send(result.encode())

                if "Questão7_resposta" in message:
                    client_socket.send(f"Resposta correta: {correct_a}".encode())

        except Exception as e:
            print(f"Error: {e}")
            break
    with clients_lock:  # Remove o clientes do servidor e fecha sua conexão com ele
        clients.remove(client_socket)
    client_socket.close()


def start_server(host='127.0.0.1', port=50000):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um socket para servidor
    server_socket.bind((host, port))  # Coloca o servidor para escutar na porta escolhida
    server_socket.listen(10)  # Extende o limite para 10 conexões simultâneas
    print(f"Server started on {host}:{port}")

    clients = []
    clients_lock = threading.Lock()

    stop_flag = threading.Event()

    def accept_clients():
        while not stop_flag.is_set():  # Se mantém enquanto a flag de parada é falsa
            try:
                client_socket, addr = server_socket.accept()  # Aceita uma nova conexão de um cliente
                print(f"Connection from {addr}")
                with clients_lock:  # Adquire o lock para proteger a lista de clientes
                    clients.append(client_socket)  # Adiciona o socket do cliente à lista de clientes
                client_handler = threading.Thread(target=handle_client, args=(
                    client_socket, clients, clients_lock))  # Cria uma nova thread para lidar com o cliente
                client_handler.start()  # Inicia a thread para tratar a conexão do cliente
            except OSError:
                break

    client_accept_thread = threading.Thread(target=accept_clients)
    client_accept_thread.start()

    print("Press 'ESC' to stop the server.")
    keyboard.wait('ESC')
    stop_flag.set()
    server_socket.close()

    # Notificar todos os clientes e fechá-los
    with clients_lock:
        for client_socket in clients:
            try:
                client_socket.send("Desligando servidor!".encode())
            except Exception as e:
                print(f"Erro ao enviar mensagem de fechamento: {e}")
            finally:
                client_socket.close()

    print("Server stopped.")


start_server()
