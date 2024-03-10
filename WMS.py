lista = list()
produto = dict()

def salvar():
    lista.append(produto.copy())

def comentario():
    print()

def validar_codigo(codigo):
    for item in lista:
        if codigo == item['codigo']:
            return True
    return False

def visualizar():
    for i in lista:
        print(i)

def cadastro():
    print()
    print('Etapa de realizar o cadastramento do produto.')
    while(True):    
            print("Tela de cadastro, por gentileza preencher as informções abaixo:")
            produto['codigo'] = (input('Digite o código do item que irá cadastrar: '))
            while validar_codigo(produto['codigo']): 
                produto['codigo'] = str(input('Código já existe, favor informar outro: '))
            produto['tamanho'] = str(input('Digite as dimenções do produto no formato : '))
            salvar()
            if (int(input("Deseja continuar? {0} sim {1} não")) == 1): break

while(True):
    opcao = int(input('1-CADASTRAR\n2-ADICIONAR COMENTÁRIOS\n4-VISUALIZAR CADASTROS\n3-SAIR'))
    if (opcao == 1):
        cadastro()

    elif (opcao == 4):
        visualizar()
            
    elif (opcao ==2):
        comentario()

    elif opcao == 3:
        break   

    else:
        print('opção não existe')
        opcao = int(input('1-CADASTRAR\n2-PESQUISAR\n3-DELETAR\n4-VISUALIZAR CADASTROS\n5-SAIR'))