import tkinter as tk
from tkinter import Frame,Label,NSEW,NW,Button,Entry,CENTER,ttk,messagebox
from tkcalendar import DateEntry
from funções import deletar_info,inserir_info,mostrar_info,atualizar_info



#usado para chamar a função na tela de login
def create_tabbed_interface():



#criando a tela e colocando para abrir no meio
    janela = tk.Tk()
    janela.title("Sistema de cadastro")

    janela.configure(background='#e9edf5')
    janela.resizable(width=False, height=False)
    largura=1043
    altura=450

    screen_width=janela.winfo_screenwidth()
    screen_height=janela.winfo_screenheight()

    x=(screen_width//2)-(largura//2)
    y=(screen_height//2)-(altura//2)

    janela.geometry(f'{largura}x{altura}+{int(x)}+{int(y)}')






    #######dividindo tela tab1#######
    frame_cima = Frame(janela, width=310, height=50, bg='#4fa882', relief='flat')
    frame_cima.grid(row=0, column=0)

    frame_baixo = Frame(janela, width=310, height=403, bg='#feffff', relief='flat')
    frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

    frame_direita = Frame(janela, width=588, height=403, bg='#feffff', relief='flat')
    frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

    ######label cima tab1#######

    app_nome = Label(frame_cima, text='Cadastro de Paciente', anchor=NW, font=('Ivy 13 bold'), bg='#4fa882',
                     fg='#feffff', relief='flat')
    app_nome.place(x=10, y=20)

    global tree

################inserir######
    def inserir():
        nome=e_nome.get()
        email=e_email.get()
        telefone=e_telefone.get()
        dia=e_date.get()
        motivo=e_motivo.get()
        lista = [nome,email,telefone,dia,motivo]
        if nome == '':
            messagebox.showerror('Error','O nome não pode ser vazio')
        else:
            inserir_info(lista)
            messagebox.showinfo('Sucesso','Os dados foram inseridos com sucesso')
            e_nome.delete(0,"end")
            e_email.delete(0,"end")
            e_telefone.delete(0,"end")
            e_date.delete(0,"end")
            e_motivo.delete(0,"end")
        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()


#####atualiar


    def atualizar():
        try:
            treev_dados=tree.focus()
            treev_dicionario=tree.item(treev_dados)
            tree_lista=treev_dicionario['values']
            valor_id=tree_lista[0]
            e_nome.delete(0, "end")
            e_email.delete(0, "end")
            e_telefone.delete(0, "end")
            e_date.delete(0, "end")
            e_motivo.delete(0, "end")

            e_nome.insert(0, tree_lista[1])
            e_email.insert(0, tree_lista[2])
            e_telefone.insert(0, tree_lista[3])
            e_date.insert(0, tree_lista[4])
            e_motivo.insert(0, tree_lista[5])
            b_inserir.config(state='disabled')


        except IndexError:
            messagebox.showerror('Erro','Selecione um dos dados da tabela')

        def update():
            try:
                nome = e_nome.get()
                email = e_email.get()
                telefone = e_telefone.get()
                dia = e_date.get()
                motivo = e_motivo.get()
                lista = [nome, email, telefone, dia, motivo,valor_id]

                if nome == '':
                    messagebox.showerror('Error', 'O nome não pode ser vazio')


                else:

                    atualizar_info(lista)
                    messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso',)

                    e_nome.delete(0, "end")
                    e_email.delete(0, "end")
                    e_telefone.delete(0, "end")

                    e_date.delete(0, "end")
                    e_motivo.delete(0, "end")

                for widget in frame_direita.winfo_children():
                    b_confirmar.place_forget()
                    b_inserir.config(state='normal')
                    widget.destroy()



                mostrar()

            except:
                messagebox.showerror('erro','selecione um item')


        # botao confirmar
        b_confirmar = Button(frame_baixo, command=update,text='Confirmar', width=10, font=('Ivy 7 bold'), bg='#4fa882',fg='#feffff',relief='raised', overrelief='ridge')

        b_confirmar.place(x=105, y=368)



    #função deletar

    def deletar():
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            tree_lista = treev_dicionario['values']
            valor_id = [tree_lista[0]]
            confimacao=messagebox.askyesno('confirmação','tem certeza que deseja excluir este item?')
            if confimacao:
                deletar_info(valor_id)
                messagebox.showinfo('sucesso', 'Os dados foram deletados da tabela com sucesso')
            for widget in frame_direita.winfo_children():
                widget.destroy()
            mostrar()
        except IndexError:
            messagebox.showerror('Erro','selecione um dos dados na tabela')


#função sair do sistema
    def sair():
        if messagebox.askokcancel('sair','tem certeza que deseja sair'):
            janela.destroy()



    ######configurando frame baixo#######
    # Nome
    l_nome = Label(frame_baixo, text='Nome Paciente', anchor=NW, font=('Ivy 10 bold'), bg='#feffff', fg='#403d3d',
                   relief='flat')
    l_nome.place(x=10, y=10)
    e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
    e_nome.place(x=15, y=40)
    #email
    l_email = Label(frame_baixo, text='Email Paciente', anchor=NW, font=('Ivy 10 bold'), bg='#feffff',
                       fg='#403d3d', relief='flat')
    l_email.place(x=10, y=70)
    e_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
    e_email.place(x=15, y=100)
    # telefone
    l_telefone = Label(frame_baixo, text='Telefone Paciente', anchor=NW, font=('Ivy 10 bold'), bg='#feffff',
                       fg='#403d3d', relief='flat')
    l_telefone.place(x=10, y=130)
    e_telefone = Entry(frame_baixo, width=45, justify='left', relief='solid')
    e_telefone.place(x=15, y=160)
    # date
    l_date = Label(frame_baixo, text='Data da Consulta', anchor=NW, font=('Ivy 10 bold'), bg='#feffff', fg='#403d3d',
                   relief='flat')
    l_date.place(x=10, y=190)
    e_date = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth='2', year=2023)
    e_date.place(x=15, y=220)
    #motivo
    l_motivo = Label(frame_baixo, text='Motivo da consulta', anchor=NW, font=('Ivy 10 bold'), bg='#feffff',
                       fg='#403d3d', relief='flat')
    l_motivo.place(x=10, y=250)
    e_motivo = Entry(frame_baixo, width=45, justify='left', relief='solid')
    e_motivo.place(x=15, y=280)

    #botao inserir
    b_inserir = Button(frame_baixo,command=inserir, text='Inserir',width=10, font=('Ivy 9 bold'), bg='#038cfc', fg='#feffff',
                   relief='raised',overrelief='ridge')
    b_inserir.place(x=12, y=330)

    # botao atualizar
    b_atualizar = Button(frame_baixo, command=atualizar,text='Atualizar', width=10, font=('Ivy 9 bold'), bg='#4fa882', fg='#feffff',
                       relief='raised', overrelief='ridge')
    b_atualizar.place(x=102, y=330)

    # botao deletar
    b_deletar = Button(frame_baixo,command=deletar, text='Deletar', width=10, font=('Ivy 9 bold'), bg='#ef5350', fg='#feffff',
                         relief='raised', overrelief='ridge')
    b_deletar.place(x=190, y=330)

    #botao sair
    b_sair=Button(frame_baixo,text='sair',width=10,font=('Ivy 7 bold'),bg='black',fg='#feffff',relief='raised',overrelief='ridge',command=sair)
    b_sair.place(x=14,y=370)
    #frame direita

    #função que vai mostrar os dados cadastrados do lado
    def mostrar():
        global tree
        lista = mostrar_info()

        tabela_head=['ID','Nome','Email','Telefone','Dia','Motivo']

            #criando a tabela
        tree=ttk.Treeview(frame_direita,selectmode='extended',columns=tabela_head,show="headings")

        vsb= ttk.Scrollbar(frame_direita,orient="vertical",command=tree.yview)

        hsb=ttk.Scrollbar(frame_direita,orient="horizontal",command=tree.xview)

        tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
        tree.grid(column=0,row=0,sticky="nsew")
        vsb.grid(column=1,row=0,sticky="ns")
        hsb.grid(column=0,row=1,sticky="ew")

        frame_direita.grid_rowconfigure(0,weight=12)


        hd=["center", "w", "w", "center", "center", "center"]
        h=[50, 150, 200, 100, 100, 150]
        n=0

        for col in tabela_head:
            tree.heading(col,text=col.title(),anchor=CENTER)
            tree.column(col,width=h[n],anchor=hd[n])
            n+=1

        for item in lista:
            tree.insert('', 'end', values=item)


    mostrar()
    janela.mainloop()





