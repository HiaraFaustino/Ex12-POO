import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os.path
import pickle

class MatriculaInvalida(Exception):
    pass

class CursoInvalido(Exception):
    pass

class Equipe:
    def __init__(self, curso, listaEstEquipe):
        self.__curso = curso 
        self.__listaEstEquipe = listaEstEquipe

    @property
    def curso(self):
        return self.__curso
    
    @property
    def listaEstEquipe(self):
        return self.__listaEstEquipe

class Curso:
    def __init__(self, sigla, nome):
        self.__sigla = sigla
        self.__nome = nome

    @property
    def sigla(self):
        return self.__sigla
    
    @property
    def nome(self):
        return self.__nome
    
class Estudante:
    def __init__(self, nroMatric, nome, curso):
        self.__nroMatric = nroMatric
        self.__nome = nome
        self.__curso = curso

    @property
    def nroMatric(self):
        return self.__nroMatric

    @property
    def nome(self):
        return self.__nome
    
    @property
    def curso(self):
        return self.__curso
    
class LimiteInsereCurso(tk.Toplevel):
    def __init__(self, controle, listaCurso):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Inserir curso")
        self.controle = controle

        self.frameCurso = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCurso.pack()
        self.frameButton.pack()

        self.labelCurso = tk.Label(self.frameCurso,text="Curso: ")
        self.labelCurso.pack(side="left")
        self.escolhacombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameCurso,width=20,textvariable=self.escolhacombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCurso

        self.buttonSubmit = tk.Button(self.frameButton,text="Inserir curso")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.insereCurso)

        self.buttonClose = tk.Button(self.frameButton,text="Close")
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controle.closeHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteInsereEquipe(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Criação de equipe")
        self.controle = controle

        self.frameNroMatric = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNroMatric.pack()
        self.frameButton.pack()

        self.labelNroMatric = tk.Label(self.frameNroMatric,text="Número de matrícula: ")
        self.labelNroMatric.pack(side="left")
        self.inputNroMatric = tk.Entry(self.frameNroMatric,width=20)
        self.inputNroMatric.pack(side="left")

        self.buttonAdiciona = tk.Button(self.frameButton,text="Adicionar")
        self.buttonAdiciona.pack(side="left")
        self.buttonAdiciona.bind("<Button>", controle.addEstudante)

        self.ButtonCria = tk.Button(self.frameButton,text="Cria Equipe")
        self.ButtonCria.pack(side="left")
        self.ButtonCria.bind("<Button>", controle.criaEquipe)

        self.buttonClose = tk.Button(self.frameButton,text="Close")
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controle.closeHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteInsereConsulta(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title('Consulta')
        self.controle = controle

        self.frameSigla = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameSigla.pack()
        self.frameButton.pack()

        self.labelSigla = tk.Label(self.frameSigla,text="Sigla do curso: ")
        self.labelSigla.pack(side="left")
        self.inputSigla = tk.Entry(self.frameSigla,width=20)
        self.inputSigla.pack(side="left")

        self.buttonConsulta = tk.Button(self.frameButton,text="Consultar")
        self.buttonConsulta.pack(side="left")
        self.buttonConsulta.bind("<Button>", controle.consultar)

        self.buttonClose = tk.Button(self.frameButton,text="Close")
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controle.closeHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteInsereDados(tk.Toplevel):
    def __init__(self, controle, dados):

        tk.Toplevel.__init__(self)
        self.geometry('250x250')
        self.title("Dados do Campeonato")
        self.controle = controle

        self.frameDados = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameDados.pack()
        self.frameButton.pack()

        self.labelDados = tk.Label(self.frameDados,text="Dados das equipes: ")
        self.labelDados.pack(side="top")
        self.textDados = tk.Text(self.frameDados,height=10,width=30)
        self.textDados.pack(side="top")
        self.textDados.insert(tk.END, dados)

        self.buttonClose = tk.Button(self.frameButton,text="Close")
        self.buttonClose.pack(side="left")
        self.buttonClose.bind("<Button>", controle.closeHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlEquipe():
    def __init__(self, controlePrincipal):
        self.cursoSel = None #variavel para receber o curso selecionado
        self.ctrlPrincipal = controlePrincipal
        self.listaEstEquipe = []
        self.listaEquipe = []

        if not os.path.isfile("equipe.pickle"):
            self.listaEquipe = []
        else:
            with open("equipe.pickle", "rb") as f:
                self.listaEquipe = pickle.load(f)

        c1 = Curso("CCO", "Ciência da Computação")
        c2 = Curso("SIN", "Sistemas de Informação")
        c3 = Curso("EEL", "Engenharia Elétrica")
        self.listaCurso = []
        self.listaCurso.append(c1)
        self.listaCurso.append(c2)
        self.listaCurso.append(c3)
        #Inserir mais cursos, se quiser
        self.listaEstudante = []
        self.listaEstudante.append(Estudante(1001, "José da Silva", c1))
        self.listaEstudante.append(Estudante(1002, "João de Souza", c1))
        self.listaEstudante.append(Estudante(1003, "Rui Santos", c2))
        self.listaEstudante.append(Estudante(1004, "Maria Silva", c2))
        self.listaEstudante.append(Estudante(1005, "Ana Pereira", c3))
        self.listaEstudante.append(Estudante(1006, "João Ferreira", c2))
        self.listaEstudante.append(Estudante(1007, "Davi Santos", c1))
        self.listaEstudante.append(Estudante(1008, "Marcos Souza", c3))
        self.listaEstudante.append(Estudante(1009, "Fernanda Costa", c2))
        self.listaEstudante.append(Estudante(1010, "Henrique Mendonça", c3))
        #Inserir mais 7 alunos, totalizando pelo menos 10 na lista
        
    def getNomeCurso(self):
        listaNomeCurso = [] #lista de cursos por nome
        for curso in self.listaCurso:
            listaNomeCurso.append(curso.nome)#add a lista o nome dos cursos
        return listaNomeCurso#utilizado no combobox para criarEquipe
    
    def getCurso(self, nome):#serve para pegar o curso por nome
        cursoSel = None
        for curso in self.listaCurso:
            if curso.nome == nome:
                cursoSel = curso
        return cursoSel

    def criarEquipe(self):
        self.limite = LimiteInsereCurso(self, self.getNomeCurso())

    def insereCurso(self, event):
        cursoNome = self.limite.escolhacombo.get()#pega o curso da combobox
        self.cursoSel = self.getCurso(cursoNome)#recebe o curso selecionado
        self.limite.destroy()
        self.limite = LimiteInsereEquipe(self)

    def getEstudante(self, nroMatric):#serve para pegar o estudante pelo nro matric
        est = None
        for estudante in self.listaEstudante:
            if estudante.nroMatric == nroMatric:
                est = estudante
        return est#usado para addEstudante

    def addEstudante(self, event):
        nroMatric = int(self.limite.inputNroMatric.get())#recebe o nro da matricula
        try:
            estudante = self.getEstudante(nroMatric)#estudante recebe o nro matric correspondente
            if estudante is None:
                raise MatriculaInvalida()
            if estudante.curso != self.cursoSel:
                raise CursoInvalido()
            if estudante not in self.listaEstEquipe:
                self.listaEstEquipe.append(estudante)#add estudante na listaEstEquipe
                self.clearHandlerEquipe(event)
                self.limite.mostraJanela('Sucesso', 'Estudante adicionado com sucesso!')
            else:
                self.limite.mostraJanela('Aviso', 'Estudante já foi adicionado!')
            
        except MatriculaInvalida:
            self.limite.mostraJanela('Erro', 'Matrícula inexistente!')
            return
        except CursoInvalido:
            self.limite.mostraJanela('Erro', 'Estudante não está matriculado no curso!')
            return
        except ValueError:
            self.limite.mostraJanela('Erro', 'Insira um valor numérico!')
            return
            
    def criaEquipe(self, event):
        if self.cursoSel is None or len(self.listaEstEquipe) == 0:#se não estiver selecionado curso ou listaEstEquipe vazia
            self.limite.mostraJanela('Erro', 'Não é possível criar uma equipe sem curso ou sem membros.')
        else:
            equipe = Equipe(self.cursoSel, self.listaEstEquipe)#cria objeto da classe Equipe
            self.listaEquipe.append(equipe)#add na listaEquipe
            self.limite.mostraJanela('Sucesso', 'Equipe criada com sucesso!')
            self.clearHandlerEquipe(event)
            self.listaEstEquipe = []
    
    def salvaEquipe(self):
        if len(self.listaEquipe) != 0:
            with open("equipe.pickle", "wb") as f:
                pickle.dump(self.listaEquipe, f)
    
    def consultarEquipe(self):
        self.limite = LimiteInsereConsulta(self)

    def consultar(self, event):
        cursoSigla = self.limite.inputSigla.get().upper()#pega a sigla do curso maiúscula
        curso = self.getCursoSigla(cursoSigla)#curso recebe a sigla do curso correspondente
        self.clearHandlerConsulta(event)
        if curso == None:#se não existir curso com a sigla correspondente
            self.limite.mostraJanela('Erro', 'Esta sigla de curso não existe!')
        else:
            if len(self.listaEquipe) == 0:#se o nro de estudantes na lista for 0
                self.limite.mostraJanela('Aviso', 'Não existe equipe desse curso!')
            else:
                msg = ''
                for equipe in self.listaEquipe:
                    if equipe.curso.sigla == curso.sigla:
                        msg += 'Nome dos estudantes da equipe:' + '\n'
                        for estudante in equipe.listaEstEquipe:
                                msg += estudante.nome + '\n'
            self.limite.mostraJanela('Equipe consultada', msg)

    def getCursoSigla(self, siglaCurso):#pega o curso pela sigla
        sig = None
        for curso in self.listaCurso:
            if curso.sigla == siglaCurso:
                sig = curso
        return sig #usado para a consulta

    def imprimirDados(self):
        if len(self.listaEquipe) == 0:#se não existirem equipes
            LimiteInsereDados(self, 'Não existem equipes!')
        else:
            dados = ''
            NroEquipes = len(self.listaEquipe)
            NroEst = sum(len(equipe.listaEstEquipe) for equipe in self.listaEquipe)
            if NroEquipes > 0:
                MediaEst = NroEst / NroEquipes
                dados += 'Número de equipes: {}\nNúmero total de estudantes: {}\nMédia de estudantes por equipe: {}'.format(NroEquipes, NroEst, MediaEst)
                self.limite = LimiteInsereDados(self, dados)

    def closeHandler(self, event):
        self.limite.destroy()
            
    def clearHandlerEquipe(self, event):
        self.limite.inputNroMatric.delete(0, len(self.limite.inputNroMatric.get()))

    def clearHandlerConsulta(self, event):
        self.limite.inputSigla.delete(0, len(self.limite.inputSigla.get()))