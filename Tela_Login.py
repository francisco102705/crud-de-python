from main import create_tabbed_interface
from Banco import created_table
import tkinter as tk
from tkinter import messagebox
import sqlite3
import os
import datetime

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title('Login de Usuários')

        # Configuração para centralizar a janela na tela
        largura = 400
        altura = 200
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (largura // 2)
        y = (screen_height // 2) - (altura // 2)
        root.geometry(f'{largura}x{altura}+{x}+{y}')

        # Conectar ao banco de dados SQLite e criar tabela se não existir
        self.conn = sqlite3.connect('usuarios.db')
        created_table(self)

        # Criando os widgets
        self.label_login = tk.Label(root, text='Login', font=('Arial', 12))
        self.entry_login = tk.Entry(root, font=('Arial', 12))
        self.label_senha = tk.Label(root, text='Senha', font=('Arial', 12))
        self.entry_senha = tk.Entry(root, show='*', font=('Arial', 12))
        self.button_novo_usuario = tk.Button(root, text='Novo Usuário', font=('Arial', 12), command=self.novo_usuario)
        self.button_fazer_login = tk.Button(root, text='Fazer Login', font=('Arial', 12), command=self.fazer_login)
        self.button_sair = tk.Button(root, text='Sair', font=('Arial', 12), command=self.sair)

        # Posicionando os widgets na tela
        self.label_login.grid(row=0, column=0, padx=5, pady=5)
        self.entry_login.grid(row=0, column=1, padx=5, pady=5)
        self.label_senha.grid(row=1, column=0, padx=5, pady=5)
        self.entry_senha.grid(row=1, column=1, padx=5, pady=5)
        self.button_novo_usuario.grid(row=2, column=0, padx=5, pady=5)
        self.button_fazer_login.grid(row=2, column=1, padx=5, pady=5)
        self.button_sair.grid(row=2, column=2, padx=5, pady=5)

        # Verificar e apagar o log a cada 7 dias se necessário
        self.log_file = 'login_log.txt'
        self.check_and_delete_log()


#cadastrar novo usuario
    def novo_usuario(self):
        login = self.entry_login.get()
        senha = self.entry_senha.get()
        if login == senha:
            messagebox.showerror('Erro', 'Sua senha deve ser diferente do nome do usuário.')
        else:
            try:
                with self.conn:
                    self.conn.execute('INSERT INTO usuarios (login, senha) VALUES (?, ?)', (login, senha))
                messagebox.showinfo('Novo Usuário Aprovado', 'Novo Usuário Aprovado!')
            except sqlite3.IntegrityError:
                messagebox.showerror('Erro', 'Nome de usuário já existe.')
#fazendo login e chamando a função
    def fazer_login(self):
        login = self.entry_login.get()
        senha = self.entry_senha.get()
        if self.buscar_usuario(login, senha):
            messagebox.showinfo('Login realizado', f'Bem Vindo, {login.capitalize()}! Seu login foi realizado com sucesso!')
            self.root.withdraw()
            self.salvar_log(login)
            root.destroy()
            create_tabbed_interface()

        else:
            messagebox.showerror('Erro', 'Você deve ter digitado o nome de usuário e/ou a senha errado. Por favor verifique.')
#procurar o usuario no banco, para fazer a autenticação
    def buscar_usuario(self, login, senha):
        cursor = self.conn.execute('SELECT * FROM usuarios WHERE login = ? AND senha = ?', (login, senha))
        return cursor.fetchone() is not None
#log de entrada
    def salvar_log(self, login):
        with open(self.log_file, 'a') as log:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log.write(f'{now} - Login realizado por: {login}\n')

    def carregar_log(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as log:
                return log.readlines()
        return []
#deletando o log apos 7 dias
    def check_and_delete_log(self):
        if os.path.exists(self.log_file):
            last_modified = datetime.datetime.fromtimestamp(os.path.getmtime(self.log_file))
            now = datetime.datetime.now()
            if (now - last_modified).days > 7:
                os.remove(self.log_file)
#sair da tela de login
    def sair(self):
        self.conn.close()
        self.root.destroy()



# Inicialização da aplicação
root = tk.Tk()
app = Interface(root)
root.mainloop()

