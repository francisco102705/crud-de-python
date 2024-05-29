import sqlite3 as lite

#estabelencendo conexão
con = lite.connect('banco.db')



#função inserir paciente
def inserir_info(i):
    with con:
        cur=con.cursor()
        query = "INSERT INTO Paciente(nome,email,telefone,dia,motivo) VALUES(?,?,?,?,?)"
        cur.execute(query,i)


#função mostrar todos os pacientes
def mostrar_info():
    lista=[]
    with con:
        cur=con.cursor()
        query="SELECT * FROM Paciente"
        cur.execute(query)
        info=cur.fetchall()
        for i in info:
            lista.append(i)
    return lista




#atualizar
def atualizar_info(i):
    with con:
        cur=con.cursor()
        query="UPDATE Paciente SET nome=?,email=?,telefone=?,dia=?,motivo=? WHERE id=?"
        cur.execute(query,i)

#função que vai deletar as informações
def deletar_info(i):
    with con:
        cur=con.cursor()
        query="DELETE FROM Paciente WHERE id=?"
        cur.execute(query,i)
