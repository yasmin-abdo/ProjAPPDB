# principal.py
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import subprocess


root = Tk()
menubar = Menu(root)
root.config(menu=menubar)
root.state("zoomed")

root.title('Programa')


filemenu = Menu(menubar)
filemenu2 = Menu(menubar)
filemenu3 = Menu(menubar)

menubar.add_cascade(label='Arquivo', menu=filemenu)
menubar.add_cascade(label='Cadastros', menu=filemenu2)
menubar.add_cascade(label='Ajuda', menu=filemenu3)

def Quit():
    root.destroy()
def cadusuarios():
    subprocess.run(['python',"cadusuarios.py"])
def cadcidades():
    subprocess.run(['python',"cadcidades.py"])
def cadclientes():
    subprocess.run(['python',"cadclientes.py"])
def Help():
    text = Text(root)
    text.pack();
    text.insert('insert', 'Ao clicar no botão da\n'
                          'respectiva cor, o fundo da tela\n'
                          'aparecerá na cor escolhida.')


filemenu.add_separator()
filemenu.add_command(label='Sair', command=Quit)
filemenu2.add_command(label='Usuários', command=cadusuarios)
filemenu2.add_command(label='Cidades', command=cadcidades)
filemenu2.add_command(label='Clientes', command=cadclientes)
filemenu3.add_command(label='Ajuda', command=Help)
root.mainloop()

def iniciar():
    root.mainloop()


