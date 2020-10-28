from PyQt5 import uic,QtWidgets
import sqlite3

logins = ['ifpe123',]
senhas = ['ifpe321',]
def chama_segunda_tela():
    #faz com q a lab 4 não apareça nada e limpa o campo depois de colocar a informação certa
    primeira_tela.label_4.setText("")
    #criar uma variavel chamando a 1tela no lineedit(que é o nome da area do login) e colocando como texto
    nome_usuario = primeira_tela.lineEdit.text()
    #fez a mesma coisa de cima
    senha = primeira_tela.lineEdit_2.text()
    #agr a condiç para aparecer a proxima tela
    if nome_usuario in logins and senha in senhas:
        #se a condiç de cima passar ele fecha a 1 tela e abre a 2
        primeira_tela.close()
        segunda_tela.show()
    else:
        #na 1 tela na label 4 vai mostrar o texto...
        primeira_tela.label_4.setText("Dados de login incorretos!")


def cadastrar():
    atendimento.label_2.setText("")
    tela_cadastro.label_3.setText("")
    tela_cadastro.label_2.setText("")
    #aqui vamos salvar os dados informados em cada campo em uma variavel
    nome = tela_cadastro.lineEdit.text()
    login = tela_cadastro.lineEdit_2.text()
    senha = tela_cadastro.lineEdit_3.text()
    c_senha = tela_cadastro.lineEdit_4.text()

    #aqui vemos se as senhas estão iguais
    if (senha == c_senha):
        logins.append(login)
        senhas.append(senha)
        tela_cadastro.label_3.setText("Cadastrado!")
    else:
        tela_cadastro.label_2.setText("Dados invalidos!")


def sair():
    segunda_tela.close()
    primeira_tela.show()

def abre_tela_cadastro():
    tela_cadastro.show()

def abre_tela_adicionar_produto():
    adicionar_produto.show()

def sair1():
    adicionar_produto.close()
    adicionar_produto.label_2.setText("")
    segunda_tela.show()

def abre_tela_estoque():
    estoque.show()

def sair2():
    estoque.close()
    segunda_tela.show()

def abre_tela_atendimento():
    atendimento.show()

def sair3():
    atendimento.label_2.setText("")
    atendimento.close()
    segunda_tela.show()

def sair4():
    tela_cadastro.close()

#criamos listas
nomep = []
valores = []
unidades = []
#aqui cadastramos os produtos pela tela de cadastro e mostramos na tela de estoque
def cadastrar_produto():
    adicionar_produto.label_2.setText("")
    #criamos uma variavel associada a algum determinado elemento de uma pagina e o transformamos em texto
    nome_produto = adicionar_produto.lineEdit.text()
    valor_produto = adicionar_produto.lineEdit_2.text()
    unidade_produto = adicionar_produto.lineEdit_3.text()

    if nome_produto in nomep:
        adicionar_produto.label_2.setText("Produto já cadastrado!")
        adicionar_produto.label_3.setText("")

    if nome_produto not in nomep:
    #aqui verificamos se o valor digitado pode ser transformado em float/int
        try:
            valor = float(valor_produto)
            unid = int(unidade_produto)
        except:
            adicionar_produto.label_2.setText("O valor do produto ou unidade foi digitado de forma incorreta!")
            adicionar_produto.label_3.setText("")

        #se a try/tentativa der certo 
        else:
            valor = float(valor_produto)
            unid = int(unidade_produto)

            nomep.append(nome_produto)
            valores.append(valor)
            unidades.append(unid)

            #adicionamos a uma lista na tela
            estoque.listWidget.addItem(nome_produto)
            estoque.listWidget_2.addItem(valor_produto)
            estoque.listWidget_3.addItem(unidade_produto)
            adicionar_produto.label_3.setText('Produto cadastrado!')
            print(nomep)
            print(valores)
            print(unidades)


#area de atendimento
totalvalor = []
def confirmar():
    produto_comprado = atendimento.lineEdit.text()
    quantidade_comprada = atendimento.lineEdit_2.text()
    if produto_comprado not in nomep:
        atendimento.label_2.setText("Produto não encontrado no estoque!")
        atendimento.label_3.setText("")
    try:
        quanttt = int(quantidade_comprada)
    except:
        atendimento.label_2.setText("Quantidade invalida!")
    else:
        quanttt = int(quantidade_comprada)
        if produto_comprado in nomep:
            for c, v in enumerate(nomep):
                if v == produto_comprado and unidades[c] >= quanttt:
                    atendimento.listWidget.addItem(f"Você comprou {quanttt} de {v}(s)")
                    unidades[c] -= quanttt
                    atendimento.label_3.setText(f"Quantidade atual de {v} é {unidades[c]}.")
                    totalvalor.append(valores[c] * quanttt)
                    print(totalvalor)



def calcular():
    contagem = 0
    x = 0
    while True:
        x += totalvalor[contagem]
        contagem += 1
        if contagem == len(totalvalor):
            break
    atendimento.listWidget.addItem(f"sua compra deu {x}")



#aqui vamos fazer a declaração dos arquivos feitos no QTdesigner
app=QtWidgets.QApplication([])
#aqui vamos chamar a 1 e 2 tela, elas devem esta nas pastas ao lado
#nome da tela = uic.loadUI("nome do arquivo ao lado")
primeira_tela = uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
tela_cadastro = uic.loadUi("tela_cadastro.ui")
adicionar_produto = uic.loadUi("adicionar_produto.ui")
atendimento = uic.loadUi("atendimento.ui")
estoque = uic.loadUi("estoque.ui")

#aqui vamos conectar a primeira tela com a segunda ou ao contrario.
#na 1 tela quando clicar no pushbutton vai connect a variavel chama_segunda_tela...
primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
#na 2 tela quando clicar no pushb_4 vai retornar a função 'sair' que fecha a segunda e abre a 1...
segunda_tela.pushButton_4.clicked.connect(sair)
#isso ira transformar a senha naquelas bolinhas...
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
#quando clicar no pushb_2 vai conectar a função abre_tela... e abrir o cadastro
primeira_tela.pushButton_2.clicked.connect(abre_tela_cadastro)
#aqui é o botao de cadastro na tela de cadastrar
tela_cadastro.pushButton.clicked.connect(cadastrar)
#sair cadastro
tela_cadastro.pushButton_2.clicked.connect(sair4)
#abrir tela de add prod no estoque
segunda_tela.pushButton.clicked.connect(abre_tela_adicionar_produto)
#aqui quando clicar no sair da tela de add prod ele volta para a principal
adicionar_produto.pushButton.clicked.connect(sair1)
#aqui abre a tela de estoque
segunda_tela.pushButton_3.clicked.connect(abre_tela_estoque)
#aq sai da tela de estoque
estoque.pushButton.clicked.connect(sair2)
#abrir tela de atendimento
segunda_tela.pushButton_2.clicked.connect(abre_tela_atendimento)
#sair tela de atend
atendimento.pushButton.clicked.connect(sair3)
#quando clicar em adicionar o produto vai para lista
adicionar_produto.pushButton_2.clicked.connect(cadastrar_produto)
#aqui
atendimento.pushButton_2.clicked.connect(confirmar)
atendimento.pushButton_3.clicked.connect(calcular)

#quando der play ele vai começar nessa tela...
primeira_tela.show()
app.exec()
