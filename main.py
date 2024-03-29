import tkinter as tk
from tkinter import messagebox
import equipe as eqp

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)
        self.equipeMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)

        self.equipeMenu.add_command(label='Criar Equipe', \
                command=self.controle.criarEquipe)
        self.equipeMenu.add_command(label='Consultar Equipe', \
                command=self.controle.consultarEquipe)
        self.equipeMenu.add_command(label='Imprimir dados', \
                command=self.controle.imprimirDados)
        self.menubar.add_cascade(label="Campeonato", \
                menu=self.equipeMenu)
        
        self.sairMenu.add_command(label="Salva", \
                    command=self.controle.salvaEquipe)
        self.menubar.add_cascade(label="Sair", \
                    menu=self.sairMenu)
        
        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlEquipe = eqp.CtrlEquipe(self)
        self.limite = LimitePrincipal(self.root, self)
        self.root.title("Equipe")
        self.root.mainloop()

    def criarEquipe(self):
        self.ctrlEquipe.criarEquipe()

    def consultarEquipe(self):
        self.ctrlEquipe.consultarEquipe()

    def imprimirDados(self):
        self.ctrlEquipe.imprimirDados()

    def salvaEquipe(self):
        self.ctrlEquipe.salvaEquipe()
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()