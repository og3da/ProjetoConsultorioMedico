#conectando ao MySql 
import mysql.connector 
from conector import Banco 
conexao = mysql.connector.connect(host=Banco.dados['host'],database=Banco.dados['database'],user=Banco.dados['user'],password=Banco.dados['password'])
if conexao.is_connected(): #verificando se conexao foi realizada, se sim:
        db_info = conexao.get_server_info() #busca versao do server
        print("Conexão realizada com sucesso! Servidor versão: ",db_info)
        mycursor = conexao.cursor() #criando variavel "mycursor" para executar comandos sql
        mycursor1 = conexao.cursor() #criando variavel "mycursor1" para executar comandos sql
else:
    print("Problemas em conectar")

#encerrar conexao
def pararConexao():
    conexao.close()
    print("Conexão encerrada com sucesso!") 


#   FUNÇÕES 
# TELA DE BOAS VINDAS
def bemVindo():
    print('')
    print('-- SISTEMA CONSULTÓRIO MÉDICO --')
    print('versão: 1.0')
    print('SEJA BEM VINDO(a)')

# LOGIN
def login():
    escolha()
    F = input('Informe sua posição: ')
    # Login (Paciente,Médico,Gestor,Administrador)
    if(F == '1'):
        loginPaciente()
    elif(F == '2'):
        loginMedico()
    elif(F == '3'):
        loginGestor()
    elif(F == '4'):
        loginAdm()
    else:
        print('Opção invalida!')

# Cadastrar paciente,medico,gestor
def cadastrar():
    escolhaAdm()
    arm = input("Escolha o usuário a cadastrar: ")
    #cadastro Paciente
    if arm == '1':
        nomeUsu = input("Digite um nome para o usuário: ")
        senha = input("Digite uma senha para o usuário: ")
        nomeCompleto = input("Digite o nome completo do Paciente: ")

        sql = ("INSERT INTO tbl_Paciente(nm_Usuario,ds_Senha,nm_Completo) VALUES(%s,%s,%s)") #inserindo credenciais no banco de dados
        val = (nomeUsu,senha,nomeCompleto) 
        mycursor.execute(sql, val)
        conexao.commit()
        print("Cadastro realizado com sucesso!")                
        continuarOUsair()
            
    #cadastro Médico
    elif arm == '2':
        nomeUsu = input("Digite um nome para o usuário: ")
        senha = input("Digite uma senha para o usuário: ")
        nomeCompleto = input("Digite o nome completo do Médico: ")
        especialidade = input("Digite a especialidade do médico: ")

        sql = ("INSERT INTO tbl_Medico(nm_Usuario,ds_Senha,nm_Completo,ds_Especialidade) VALUES(%s,%s,%s,%s)") #inserindo credenciais no banco de dados
        val = (nomeUsu,senha,nomeCompleto,especialidade) 
        mycursor.execute(sql, val)
        conexao.commit()
        print("Cadastro realizado com sucesso!")            
        continuarOUsair()

    #cadastro Gestor
    elif arm == '3':
        nomeUsu = input("Digite um nome para o usuário: ")
        senha = input("Digite uma senha para o usuário: ")
        nomeCompleto = input("Digite o nome completo do Gestor: ")

        sql = ("INSERT INTO tbl_Gestor(nm_Usuario,ds_Senha,nm_Completo) VALUES(%s,%s,%s)") #inserindo credenciais no banco de dados
        val = (nomeUsu,senha,nomeCompleto) 
        mycursor.execute(sql, val)
        conexao.commit()
        print("Cadastro realizado com sucesso!")              
        continuarOUsair()
             
    else:
        print('escolha uma opção válida!')
        cadastrar()

# continuar cadastrando ou sair --adicionar função para limpar tela quando entrar no login()
def continuarOUsair():
    arm2=int(input("Digite 1 para continuar cadastrando ou 2 para sair: "))
    if arm2== 1:
        cadastrar()
    elif arm2== 2:
        login()
    else:
        print('Escolha a opção 1 ou 2!!!')
        continuarOUsair()

# PROGRAMAS DE CADA USUARIO
def programaMedico():
    mycursor.execute("select * FROM tbl_Consulta WHERE sg_Disponibilidade = 'A' ") #exibindo as consultas confirmadas
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    
    codMedico = int(input("Digite seu codigo de usuário: "))
    dataDisponivel = str(input("Digite uma data para disponibilizar horários: "))
    horaEntrada = str(input("Digite seu horário de entrada para este dia: "))
    horaSaida = str(input("Digite seu horário de saída para este dia: "))


    sql = ("INSERT INTO tbl_agendaMedico(cd_Medico, ds_Data, hr_Entrada, hr_Saida) VALUES (%s,%s,%s,%s)")
    val = (codMedico, dataDisponivel, horaEntrada, horaSaida) 
    mycursor.execute(sql, val)
    conexao.commit()
    print("Agenda cadastrada com sucesso!")
    #pensar em como posso exibir a agenda completa do medico sem mostrar a de outros
    #pensar em como posso inserir o codigo do medico automaticamente
    #exibir codigo de usuario para o medico

def programaPaciente():
    mycursor.execute("select * from vw_mostrarAgendaMedico") #exibindo a agenda dos medicos
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    medico = str(input("digite o nome do medico que deseja marcar consulta: "))
    especialidade = str(input("digite a especialidade do medico: "))
    data = str(input("digite a data desejada para consulta: "))
    hora = str(input("digite a hora desejada para consulta (*a consulta terá tempo máximo de 50min): "))


    sql = ("INSERT INTO tbl_Consulta(nm_Medico,ds_Especialidade,ds_Data,hr_Consulta) VALUES (%s,%s,%s,%s)") #inserindo credenciais no banco de dados
    val = (medico,especialidade,data,hora)
    mycursor.execute(sql, val)
    conexao.commit()
    print("Solicitação de consulta concluída!")

def programaGestor():
    mycursor.execute("select * from vw_mostrarAgendaMedico") #exibindo a agenda dos medicos
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    mycursor1.execute("select * from vw_mostrarSolicitacoesConsulta") #exibindo consultas solicitadas
    myresult1 = mycursor1.fetchall()

    for x in myresult1:
        print(x)

    #gestor deverá escolher o código da consulta a se mudar o status para ATIVO
    alterarStatus = int(input("Digite 1 para Confirmar a consulta ou 2 para manter Inativa: "))
    if alterarStatus == 1:
        mycursor.execute("UPDATE tbl_Consulta SET sg_Disponibilidade = 'A' ")
        conexao.commit()
        print(mycursor.rowcount)
        print("Consulta marcada com sucesso!") 

# Login de cada usuário
def loginPaciente():
    x = input('Usuário: ')
    y = input('Senha: ')
    mycursor.execute("select nm_Usuario, ds_Senha FROM tbl_Paciente WHERE nm_Usuario = '%s' and ds_Senha = '%s'" % (x,y)) #validando login
    verificacao = mycursor.fetchall()

    if verificacao:
        print('Bem vindo(a)!')
        programaPaciente()
    else:
        print("Usuário ou senha incorretos!")
        login()

def loginMedico():
    x = input('Usuário: ')
    y = input('Senha: ')
    mycursor.execute("select nm_Usuario, ds_Senha FROM tbl_Medico WHERE nm_Usuario = '%s' and ds_Senha = '%s'" % (x,y))
    verificacao = mycursor.fetchall()

    if verificacao:
        print('Bem vindo(a)!')
        programaMedico()
    else:
        print("Usuário ou senha incorretos!")
        login()

def loginGestor():
    x = input('Usuário: ')
    y = input('Senha: ')
    mycursor.execute("select nm_Usuario, ds_Senha FROM tbl_Gestor WHERE nm_Usuario = '%s' and ds_Senha = '%s'" % (x,y))
    verificacao = mycursor.fetchall()

    if verificacao:
        print('Bem vindo(a)!')
        programaGestor()
    else:
        print("Usuário ou senha incorretos!")
        login()

def loginAdm():
    x = input('Usuário: ')
    y = input('Senha: ')
    mycursor.execute("select nm_Usuario, ds_Senha FROM tbl_Administrador WHERE nm_Usuario = '%s' and ds_Senha = '%s'" % (x,y))
    verificacao = mycursor.fetchall()

    if verificacao:
        print('Bem vindo(a)!')
        cadastrar()
    else:
        print("Usuário ou senha incorretos!")
        login()

# exibir opções de Login
def escolha():
    print('')
    print('      * Login *    ')
    print('   -- Paciente 1 --  ')
    print('    -- Médico 2 --   ')
    print('    -- Gestor 3 --   ')
    print(' -- Administrador 4 --')
    print('')

def escolhaAdm():
    print('')
    print('    * Cadastro *    ')
    print('   -- Paciente 1 --  ')
    print('    -- Médico 2 --   ')
    print('    -- Gestor 3 --   ')
    print('')
#   FIM FUNÇÕES 

# INICIO PROGRAMA #
bemVindo()
login()

               # DESENVOLVIMENTO
#Programa Medico
    #disponibiliza sua agenda (horario entrada/saida e data) -
    #visualiza consultas marcadas em seu nome


#Programa Paciente
    #pode ver a agenda dos médicos disponiveis
    #faz a solicitação de consulta (confirmada pelo gestor) com os dados:
    #                               data,hora,medico,especialidade


#Programa Gestor
    #exibir agenda dos medicos e solicitações dos pacientes
    #confirma ou mantém inativa a solicitação de consulta. 
    # Se confirmar,a consulta passará a aparcer p/o respectivo medico