
import sqlite3 as lite

#criando a conexão
con = lite.connect('banco.db')

#criando a tabela paciente no banco de dados
with con:
    cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS Paciente(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT,email TEXT,telefone TEXT,dia DATE,motivo TEXT)')

#creando a tabela usuarios no login
def created_table(self):
    with self.conn:
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                login TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            )
        ''')

