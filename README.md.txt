# Sistema de Login e Cadastro de Pacientes

Este projeto é uma aplicação de login de usuários e cadastro de pacientes utilizando a biblioteca Tkinter para a interface gráfica e SQLite para o banco de dados. O sistema permite criar novos usuários, fazer login, registrar logs de login e realizar operações CRUD (Create, Read, Update, Delete) para cadastros de pacientes.

## Índice

1. [Pré-requisitos](#pré-requisitos)
2. [Instalação](#instalação)
3. [Como Utilizar](#como-utilizar)
4. [Instruções de Execução](#instruções-de-execução)
5. [Estrutura do Projeto](#estrutura-do-projeto)
6. [Contribuições](#contribuições)
7. [Licença](#licença)

## Pré-requisitos

Antes de iniciar, certifique-se de ter os seguintes pré-requisitos instalados:

- Python 3.x
- Biblioteca Tkinter (normalmente incluída na instalação padrão do Python)
- Biblioteca SQLite3 (normalmente incluída na instalação padrão do Python)
- Biblioteca `tkcalendar`

Para instalar o `tkcalendar`, utilize o comando:
```bash
pip install tkcalendar

Interface de Login
Execute o script principal para iniciar a interface de login:

bash
Copiar código
python Tela_Login.py
Na interface de login, você pode:

Criar um novo usuário: Digite um login e senha e clique em "Novo Usuário".
Fazer login: Digite seu login e senha e clique em "Fazer Login".
Sair do aplicativo: Clique em "Sair".
Interface de Cadastro de Pacientes
Após fazer login, a interface de cadastro de pacientes será aberta. Nessa interface, você pode:

Inserir um novo paciente: Preencha os campos e clique em "Inserir".
Atualizar as informações de um paciente: Selecione o paciente na tabela, modifique os campos e clique em "Atualizar".
Deletar um paciente: Selecione o paciente na tabela e clique em "Deletar".
Sair do sistema: Clique em "Sair".
Instruções de Execução
Para executar o projeto, utilize o seguinte comando:



Estrutura do Projeto
Uma visão geral da estrutura do diretório do projeto:

plaintext
Copiar código
nome-do-projeto/
├── main.py
├── Banco.py
├── Interface.py
├── funções.py
├── banco.db
├── README.md
├── login_log.txt
└── requirements.txt
main.py: Contém a função create_tabbed_interface que é chamada após o login bem-sucedido.
Banco.py: Contém a criação das tabelas no banco de dados SQLite.
Interface.py: Contém a classe Interface que define a interface de login e chama a interface de cadastro de pacientes.
funções.py: Contém as funções inserir_info, mostrar_info, atualizar_info e deletar_info para manipulação dos dados no banco de dados.
banco.db: Arquivo do banco de dados SQLite contendo as informações dos pacientes.
login_log.txt: Arquivo de log para registrar os logins realizados.
README.md: Arquivo com informações sobre o projeto.
requirements.txt: Arquivo com a lista de dependências do projeto (se necessário).