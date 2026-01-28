import os 
import time

os.system('cls')

#Lista de opcoes
options = [
    "[ 1 ] SALVAR",
    "[ 2 ] EDITAR",
    "[ 3 ] DELETAR",
    "[ 4 ] MARCA COMO FAVORITO",
    "[ 5 ] SAIR"
    ]


def mostrar_opcoes():
    print("\nEscolha uma das opcoes abaixo:\n")
    for option in options:
        print(option)
    
while True:
    mostrar_opcoes()
    resposta = int (input("\nEscolha uma opcao: "))

    match resposta:
        case 1: 
            print("SALVAR")
        case 2: 
            print("EDITAR")
        case 3: 
            print("DELETAR")
        case 4: 
            print("MARCA COMO FAVORITO")
        case 5:
            print("SAIR")
            os.system('cls')
            break
        case _: 
            print("\nESCOLHA UMA OPCAO VÁLIDA")
            time.sleep(1)
            os.system('cls')
            mostrar_opcoes()

    time.sleep(1)
    os.system('cls')
