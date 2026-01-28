import os 
import time

os.system('cls')
def reset(): 
    time.sleep(1)
    os.system('cls')

def pausa(msg="\nDeseja voltar? Aperte ENTER..."):
    input(msg)

mostrarMenu = True

contatos = []


def salvar(contato):
    contatos.append(contato)
    reset()
    print("SALVO COM SUCESSO!")

def editar():
    reset()

    i = 0
    print("CONTATOS: \n")
    for contato in contatos:
        nome = contato["name"]
        print(f"{i}. {nome}")
        i += 1

    cnt = int (input("\nQUAL CONTANTO VC QUER EDITAR? DIGITE O NUMERO: "))


    repetir = True

    if(repetir):
        print("\n[ 1 ] NOME")
        print("[ 2 ] TELEFONE")
        print("[ 3 ] EMAIL")
        opt = int (input("\nDIGITE A OPCAO QUE QUER EDITAR: "))

        if(opt == 1):
            name = input("DIGITE UM NOVO NOME: ")
            contatos[cnt]["name"] = name
            repetir = False
        elif(opt == 2):
            telefone = input("DIGITE UM NOVO TELEFONE: ")
            contatos[cnt]["telefone"] = telefone
            repetir = False

        elif(opt == 3):
            email = input("DIGITE UM NOVO EMAIL: ")
            contatos[cnt]["email"] = email
            repetir = False
        else:
            print("DIGITE UMA OPCAO VÁLIDA!")
            time.sleep(2)
            os.system('cls')
            repetir = True
    else:
        pausa()
        mostrarMenu = True



#Lista de opcoes
options = [
    "[ 1 ] SALVAR",
    "[ 2 ] EDITAR",
    "[ 3 ] DELETAR",
    "[ 4 ] MARCA COMO FAVORITO",
    "[ 5 ] VER USUÁRIOS CADASTRADOS",
    "[ 6 ] SAIR"
    ]


def mostrar_opcoes():
    print("\nEscolha uma das opcoes abaixo:\n")
    for option in options:
        print(option)

def criar_contato():
    name = input("DIGITE O NOME: ")
    telefone = input("DIGITE O TELEGONE: ")
    email = input("DIGITE O EMAIL: ")
    
    contato = {
        "name": name,
        "telefone": telefone,
        "email": email,
    }
    return contato



while True:
    if mostrarMenu:
        reset()
        mostrar_opcoes()
        mostrar_menu = False 

    resposta = int (input("\nEscolha uma opcao: "))

    match resposta:
        case 1: 
            os.system('cls')
            salvar(criar_contato())
            
        case 2: 
            editar()
        case 3: 
            print("DELETAR")
        case 4: 
            print("MARCA COMO FAVORITO")
        case 5: 
            reset()
            i = 1
            print("CONTATOS\n")
            for contato in contatos:
                nome = contato["name"]
                email = contato["email"]
                telefone = contato["telefone"]
                print(f"{i}. {nome}")
                print(f"    TELEFONE: {telefone}")
                print(f"    EMAIL: {email}")
                i += 1
            pausa()              
            mostrar_menu = True  
        case 6:
            print("SAIR")
            os.system('cls')
            break
        case _: 
            reset()


