lista = list()



def salvar(produto):
    lista.append(produto.copy())

def validar_codigo(codigo):
    for item in lista:
        if codigo == item['codigo']:
            return True

def visualizar():
    for i in lista:
        print(i)

def cadastro():
    print()
    print('Etapa de realizar o cadastramento do produto.')
    while(True): 
        produto = {'codigo':"", 'tamanho':"", 'comentario':[]}  
        print("Tela de cadastro, por gentileza preencher as informções abaixo:")
        produto['codigo'] = (input('Digite o código do item que irá cadastrar: '))
        while validar_codigo(produto['codigo']): 
            produto['codigo'] = str(input('Código já existe, favor informar outro: '))
        produto['tamanho'] = str(input('Digite as dimenções do produto no formato LxAxP (LARGURAxALTURAxPROFUNDIDADE): '))
        while(True):
            comentario = (input('Digite um comentario ao item: '))
            produto['comentario'].append(comentario)
            if (int(input("Deseja adicionar mais comentários? {0} sim {1} não")) == 1): break 
        salvar(produto)
        if (int(input("Deseja cadastrar mais um item? {0} sim {1} não")) == 1): break

while(True):
    opcao = int(input('1-CADASTRAR\n2-VISUALIZAR CADASTROS\n3-SAIR'))
    if (opcao == 1):
        cadastro()

    elif (opcao == 2):
        visualizar()

    elif opcao == 3:
        break   

    else:
        print('opção não existe')
        opcao = int(input('1-CADASTRAR\n2-PESQUISAR\n3-DELETAR\n4-VISUALIZAR CADASTROS\n5-SAIR'))