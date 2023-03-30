import sys
from time import sleep 
from tkinter import *
import os
from tkinter import ttk
import pygame
from tkinter import messagebox
import tkinter as tk
import sqlite3
import pandas as pd


root = app = janela = Tk()

pygame.init()
pygame.mixer.music.load('ex1.mp3')
pygame.mixer.music.play()
pygame.event.wait()

janela.geometry('500x500')
janela.resizable(True, True) 
root.title('TITANIC OPPER')

pastaApp=os.path.dirname(__file__)
imagem = PhotoImage(file=pastaApp+'\\Titanic2.png')
logo = Label(app, image=imagem)
logo.place(x=10, y=10)

Label(root, text='Usuário:').grid(row=3, column=45, sticky=S)
Label(root, text= 'Senha:').grid(row=4, column=45, sticky=S) #texto

usuario = tk.Entry()
usuario.grid(row=3, column=50, sticky=S,)

senha = tk.Entry(root, show='*')
senha.grid(row=4, column=50, sticky= S)


def login(): 
    user = usuario.get()
    Pass = senha.get()
    
    if usuario.get() == '' and senha.get() == '':
        print('Usuário Logado')
        root.destroy()
        cadastro()
    else:
        print('Usuário ou senha incorreta')

botao_login = Button(root, text='Login', 
command= login).grid(row=5, column=45, sticky=E)


def exportar():
    conexao = sqlite3.connect('banco_clientes.db')

    c = conexao.cursor()

    c.execute("SELECT*, oid FROM clientes")
    cadastrados = c.fetchall()
    cadastrados = pd.DataFrame(cadastrados, columns=['Nome', 'Sobrenome', 'Email', 'Telefone', 'ID_Banco'])
    cadastrados.to_excel('Cadastros.xlsx')

    conexao.commit()

    conexao.close()

def cadastro():

    def cadastrar():

        pass

    root = app = janela = Tk()

    janela.geometry('500x500')
    janela.resizable(True, True) 
    root.title('TITANIC OPPER')

    pastaApp=os.path.dirname(__file__)
    imagem = PhotoImage(file=pastaApp+'\\Titanic2.png')
    logo = Label(app, image=imagem)
    logo.place(x=10, y=10)

    label_nome = tk.Label(janela, text="Nome")
    label_nome.grid(row=3, column=45, sticky=S)

    label_sobrenome = tk.Label(janela, text="Sobrenome")
    label_sobrenome.grid(row=4, column=45, sticky=S)

    label_idade = tk.Label(janela, text="Idade")
    label_idade.grid(row=5, column=45, sticky=S)

    label_telefone = tk.Label(janela, text="Telefone")
    label_telefone.grid(row=6, column=45, sticky=S)


    entry_nome = tk.Entry(janela, text="nome", width=30)
    entry_nome.grid(row=3, column=50, sticky=S,)

    entry_sobrenome = tk.Entry(janela, text="sobrenome", width=30)
    entry_sobrenome.grid(row=4, column=50, sticky= S)

    entry_idade = tk.Entry(janela, text="idade", width=30)
    entry_idade.grid(row=5, column=50, sticky=S,)

    entry_telefone = tk.Entry(janela, text="telefone", width=30)
    entry_telefone.grid(row=6, column=50, sticky= S)


    botao_casdastro = tk.Button(janela, text="cadastrar", command=cadastrar)
    botao_casdastro.grid(row=7, column=45, sticky=E)

    botao_exportar = tk.Button(janela, text="Exportar", command=exportar)
    botao_exportar.grid(row=8, column=45, sticky=E,)    
        
    entry_nome.delete(0, 'end')
    entry_sobrenome.delete(0, 'end')
    entry_idade.delete(0, 'end')
    entry_telefone.delete(0, 'end')    

    
    conexao = sqlite3.connect('banco_clientes.db')

    c = conexao.cursor()

    c.execute(''' CREATE TABLE IF NOT EXISTS clientes (
            nome text,
            sobreno text,
            idade text,
            telefone text
            )
        ''')


    c.execute("INSERT INTO clientes VALUES (:nome, :sobrenome, :idade, :telefone)",
                    {
                    'nome':entry_nome.get(),
                    'sobrenome' :entry_sobrenome.get(),
                    'idade' :entry_idade.get(),
                    'telefone' :entry_telefone.get()
                    }
                    )

    conexao.commit()

    conexao.close()


    janela.mainloop()

janela.mainloop()
