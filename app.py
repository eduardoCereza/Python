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

def deletar(contato):
    reset()

    i = 0
    print("CONTATOS: \n")
    for contato in contatos:
        nome = contato["name"]
        print(f"{i}. {nome}")
        i += 1

    cnt = int (input("\nQUAL CONTANTO VC QUER DELETAR? DIGITE O NUMERO: "))
    contato_para_remover = contatos[cnt]
    contatos.remove(contato_para_remover)

#Lista de opcoes
options = [
    "[ 1 ] SALVAR",
    "[ 2 ] EDITAR",
    "[ 3 ] DELETAR",
    "[ 4 ] MARCA COMO FAVORITO",
    "[ 5 ] VER USUÁRIOS CADASTRADOS",
    "[ 6 ] VER USUÁRIOS FAVORITOS",
    "[ 7 ] SAIR"
    ]


def mostrar_opcoes():
    print("\nEscolha uma das opcoes abaixo:\n")
    for option in options:
        print(option)

def criar_contato():
    name = input("DIGITE O NOME: ")
    telefone = input("DIGITE O TELEFONE: ")
    email = input("DIGITE O EMAIL: ")
    
    
    contato = {
        "name": name,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    return contato


def alternar_favorito(contatos):
    if not contatos:
        print("Nenhum contato cadastrado.")
        input("ENTER para voltar...")
        return

    os.system('cls')
    print("CONTATOS (★ favorito)\n")
    for i, c in enumerate(contatos, start=1):
        estrela = "★" if c.get("favorito") else " "
        print(f"[ {i} ] [{estrela}] {c['name']}")

    try:
        idx = int(input("\nEscolha o contato: ")) - 1
        if idx < 0 or idx >= len(contatos):
            print("Contato inválido!")
            input("ENTER...")
            return
    except ValueError:
        print("Digite um número!")
        input("ENTER...")
        return

    contatos[idx]["favorito"] = not contatos[idx].get("favorito", False)

    status = "MARCAD0 como favorito" if contatos[idx]["favorito"] else "DESMARCADO dos favoritos"
    print(f"\n{contatos[idx]['name']} foi {status}!")
    input("ENTER para voltar...")

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
            deletar(contato)
        case 4: 
            alternar_favorito(contatos)
            mostrar_menu = True
        case 5: 
            reset()
            i = 1
            print("CONTATOS\n")
            for contato in contatos:
                nome = contato["name"]
                email = contato["email"]
                telefone = contato["telefone"]
                favorito = contato["favorito"]
                print(f"{i}. {nome}")
                print(f"    TELEFONE: {telefone}")
                print(f"    EMAIL: {email}")
                print(f"    FAVORITO: {favorito}")
                i += 1
            pausa()              
            mostrar_menu = True
        case 6:
            reset()
            i = 1
            print("CONTATOS\n")
            for contato in contatos:
                if contato["favorito"] == True:
                    nome = contato["name"]
                    email = contato["email"]
                    telefone = contato["telefone"]
                    print(f"{i}. {nome}")
                    print(f"    TELEFONE: {telefone}")
                    print(f"    EMAIL: {email}")
                    i += 1
            pausa()              
            mostrar_menu = True
        case 7:
            print("SAIR")
            os.system('cls')
            break
        case _: 
            reset()


