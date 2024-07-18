import socket
import os


def start_client(host='127.0.0.1', port=50000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Abre um socket para a conexão
    client_socket.connect((host, port))  # Conecta o socket na porta escolhida

    try:
        option = -1
        while True:  # Menu de opções
            while option not in ['0', '1', '2', '3', '4', '5', '6', '7']:
                os.system("cls")
                option = input(
                    "==========================================================\n"
                    "                 Prova 1 - Fundamentos\n"
                    "==========================================================\n"
                    "                 Questões dispóniveis\n"
                    "**********************************************************\n"
                    "Questão [1]: Conversão de base\n"
                    "Questão [2]: Operações com diferentes bases\n"
                    "Questão [3]: Divisão com binários\n"
                    "Questão [4]: Padrão IEEE 754\n"
                    "Questão [5]: Codificação UTF-8\n"
                    "Questão [6]: Álgebra booleana\n"
                    "Questão [7]: Expressões booleanas\n"
                    "---------------------------------------------------------\n"
                    "  Sair  [0]\n"
                    "*********************************************************\n"
                    "Opção: ")

            if option == '0':
                print("Programa encerrado.")
                break

            if option == '1':
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n"
                "1. Realize as seguintes conversões de base:\n\n"
                "(a) 2AA16 para base 10.\n"
                "(b) 356 para base 2.\n"
                "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                menu_text()
                option = input("Opção: ")

                if option == "1":
                    item_a = input("\n(a) Resposta: ")
                    item_b = input("(b) Resposta: ")

                    # Envia a resposta para o servidor e recebe o resultado
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    client_socket.send(f"Questão1_a:{item_a}".encode())
                    print(f"Sua resposta: {item_a} | {client_socket.recv(1024).decode()}")
                    client_socket.send(f"Questão1_b:{item_b}".encode())
                    print(f"Sua resposta: {item_b} | {client_socket.recv(1024).decode()}")
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    client_socket.send(f"Questão1_resposta".encode())
                    print(f"{client_socket.recv(1024).decode()}")
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    input("")
                    option = -1
                    continue

                if option not in ["1"]:
                    option = -1
                    continue

            if option == '2':
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n"
                "2. (1,0 pt) Realize as seguintes operações, considerando que as sequˆencias de bits são representações\n"
                "binárias de números inteiros com sinal, usando a convenção complemento a 2 para a representação de\n"
                "números negativos (com palavra de tamanho fixo de 8 bits). Os resultados devem ser apresentados na\n"
                "mesma codificação, ou seja, em base 2 e complemento a 2 com 8 bits. Indique se houve overflow\n"
                "ou se o resultado é válido.\n"
                "Resposta válida: '(valor) válido' ou '(valor) inválido'\n\n"
                
                "(a) 11010111 + 11100111\n"
                "(b) 11100100 - 10101111\n"
                "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                menu_text()
                option = input("Opção: ")

                if option == "1":
                    item_a = input("\n(a) Resposta: ")
                    item_b = input("(b) Resposta: ")

                    # Envia a resposta para o servidor e recebe o resultado
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    client_socket.send(f"Questão2_a:{item_a}".encode())
                    print(f"Sua resposta: {item_a} | {client_socket.recv(1024).decode()}")
                    client_socket.send(f"Questão2_b:{item_b}".encode())
                    print(f"Sua resposta: {item_b} | {client_socket.recv(1024).decode()}")
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    client_socket.send(f"Questão2_resposta".encode())
                    print(f"{client_socket.recv(1024).decode()}")
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    input("")
                    option = -1
                    continue

                if option not in ["1"]:
                    option = -1
                    continue

            if option == '3':
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n"
                "3. Forneça o quociente inteiro da divisão 01101001 / 11110101, considerando que os números se\n" 
                "representados em base 2 a convenção para a representação de números inteiros negativos\n"
                "é complemento a 2 (com palavra de tamanho fixo de 8 bits). O resultado deve ser apresentado\n"
                "na mesma codificação, ou seja, em base 2 e complemento a 2 com 8 bits.\n"
                "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                menu_text()
                option = input("Opção: ")

                if option == "1":
                    item_a = input("\nResposta: ")
                    # Envia a resposta para o servidor e recebe o resultado
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    client_socket.send(f"Questão3_a:{item_a}".encode())
                    print(f"Sua resposta: {item_a} | {client_socket.recv(1024).decode()}")
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    client_socket.send(f"Questão3_resposta".encode())
                    print(f"{client_socket.recv(1024).decode()}")
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    input("")
                    option = -1
                    continue

                if option not in ["1"]:
                    option = -1
                    continue

            if option == '4':
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n"
                "4. Qual a sequência de bits que representa o valor -750.1875 no padrão IEEE 754\n"
                "em precisão simples (float)?\n\n"
                "(a) Indique a sequência de bits\n"
                "(b) Visualização em dígitos hexadecimais.\n" 
                "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                menu_text()
                option = input("Opção: ")

                if option == "1":
                    item_a = input("\n(a) Resposta: ")
                    item_b = input("(b) Resposta: ")

                    # Envia a resposta para o servidor e recebe o resultado
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    client_socket.send(f"Questão4_a:{item_a}".encode())
                    print(f"Sua resposta: {item_a} | {client_socket.recv(1024).decode()}")
                    client_socket.send(f"Questão4_b:{item_b}".encode())
                    print(f"Sua resposta: {item_b} | {client_socket.recv(1024).decode()}")
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    client_socket.send(f"Questão4_resposta".encode())
                    print(f"{client_socket.recv(1024).decode()}")
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    input("")
                    option = -1
                    continue

                if option not in ["1"]:
                    option = -1
                    continue

            if option == '5':
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n"
                "5. Considere que um trecho de memória do computador contém a frase: 'Sera?'\n\n"
                "(a) Forneça, usando símbolos hexadecimais, a codificação da frase em\n"
                "UTF-8 (tabela ASCII fornecida na figura 1).\n"
                "Resposta válida: (char1) (char2) (char3) (char4) (char5)\n\n"
                
                "(b) Compare a quantidade de bytes ocupada por essa frase e por sua versão acentuada (Será? ),\n" 
                "também em UTF-8. O código (code point) da letra á é U+00E1 e a tabela UTF-8 de distribuição das\n"
                "informações em 1 a 4 bytes é dada pela figura 2.\n"
                "Resposta válida: (char1) (char2) (char3) (char4) (char5)\n"
                "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                menu_text()
                option = input("Opção: ")

                if option == "1":
                    item_a = input("\n(a) Resposta: ")
                    item_b = input("(b) Resposta: ")

                    # Envia a resposta para o servidor e recebe o resultado
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    client_socket.send(f"Questão5_a:{item_a}".encode())
                    print(f"Sua resposta: {item_a} | {client_socket.recv(1024).decode()}")
                    client_socket.send(f"Questão5_b:{item_b}".encode())
                    print(f"Sua resposta: {item_b} | {client_socket.recv(1024).decode()}")
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    client_socket.send(f"Questão5_resposta".encode())
                    print(f"{client_socket.recv(1024).decode()}")
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    input("")
                    option = -1
                    continue

                if option not in ["1"]:
                    option = -1
                    continue

            if option == '6':
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n"
                "6. Considere a fórmula a seguir, correspondente a uma função F(A,B,C,D,E):\n"
                "F(A,B,C,D,E) = !A.!B.!C.!D.!E + !A.!B.C.!D.E + A.!B.!C.!D.!E\n\n"
                
                "Imagine que você dispõe apenas de portas lógicas do tipo AND (E) de até 3 entradas, OR (OU) de até\n"
                "3 entradas e inversores (portas NOT). Reescreva (através de manipulação algébrica, indicando qual foi\n"
                "a propriedade usada em cada passo) essa fórmula de maneira a conseguir implementá-la com as portas\n"
                "lógicas disponíveis. Não precisa desenhar.\n"
                "Resposta válida: utilize () para envolver grupos e ! para negar.\n"
                "Exemplo: !(A.B.C) + !(A+B+C) + (A+B+C)\n"
                "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                menu_text()
                option = input("Opção: ")

                if option == "1":
                    item_a = input("\nResposta: ")
                    # Envia a resposta para o servidor e recebe o resultado
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    client_socket.send(f"Questão6_a:{item_a}".encode())
                    print(f"Sua resposta: {item_a} | {client_socket.recv(1024).decode()}")
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    client_socket.send(f"Questão6_resposta".encode())
                    print(f"{client_socket.recv(1024).decode()}")
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    input("")
                    option = -1
                    continue

                if option not in ["1"]:
                    option = -1
                    continue

            if option == '7':
                print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n"
                "Imagine agora que você precisa implementar uma expressão que faz o E de 3 variáveis ABC mas você\n"
                "dispõe apenas de portas lógicas do tipo AND (E) de exatamente 4 entradas. Você vai precisar de alguma\n"
                "solução para lidar com menos entradas do que a porta lógica espera. Explique quais propriedades\n"
                "algébricas dos operadores lógicos foram usadas nessa solução.\n"
                "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
                menu_text()
                option = input("Opção: ")

                if option == "1":
                    item_a = input("\nResposta: ")
                    # Envia a resposta para o servidor e recebe o resultado
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    client_socket.send(f"Questão7_a:{item_a}".encode())
                    print(f"Sua resposta: {item_a} | {client_socket.recv(1024).decode()}")
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    client_socket.send(f"Questão7_resposta".encode())
                    print(f"{client_socket.recv(1024).decode()}")
                    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    input("")
                    option = -1
                    continue

                if option not in ["1"]:
                    option = -1
                    continue

        exit()

    except KeyboardInterrupt:
        pass
    finally:  # Fecha o cliente e sai do programa
        client_socket.close()
        exit()

def menu_text():
    print("Resolver  [1]\n"
          "  Sair    [ ]\n"
          "-------------------------------------------------------")

start_client()
