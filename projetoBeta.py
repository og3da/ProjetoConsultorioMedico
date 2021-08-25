#dados de login
pacientes = {
    1:"Davi",
    1.1:"123",
    2:"",
    2.1:"",
    3:"",
    3.1:"",
    4:"",
    4.1:"",
}
 
medicos = {
    1: "Josue",
    1.1: "123",
    2:"",
    2.1:"",
    3:"",
    3.1:"",
    4:"",
    4.1:"",
}
 
gestor = {
    1: "Joao",
    1.1: "123",
    2:"",
    2.1:"",
    3:"",
    3.1:"",
    4:"",
    4.1:"",
}
 
adm = {
    "01": "Ogeda",
    "S1": "111",
}
i=1

#agendamentos
agendaMedico = {
    "medico": "",
    "dataDisponivel": "",
    "horaEntrada": "",
    "horaSaida": "",
}

agendaPaciente = {
    'nome': '',
    'medico': '',
    'especialidade': '',
    'data': '',
    'hora': '',
}

consultaMedico = {
    'paciente': '',
    'medico': '',
    'especialidade': '',
    'data': '',
    'hora': '',
}


# FUNÇÕES #
def programaMedico():
#Programa Medico
    print(consultaMedico)
    
    agendaMedico["medico"] = str(input("Digite seu nome: "))
    agendaMedico["dataDisponivel"] = str(input("Digite uma data para disponibilizar horários: "))
    agendaMedico["horaEntrada"] = str(input("Digite seu horário de entrada para este dia: "))
    agendaMedico["horaSaida"] = str(input("Digite seu horário de saída para este dia: "))

    print(agendaMedico)
    print("Agenda cadastrada com sucesso!")

def programaPaciente():
#Programa Paciente
    print(agendaMedico)

    agendaPaciente['nome'] = str(input("digite seu nome: "))
    agendaPaciente['medico'] = str(input("digite o nome do medico que deseja marcar consulta: "))
    agendaPaciente['especialidade'] = str(input("digite a especialidade do medico: "))
    agendaPaciente['data'] = str(input("digite a data desejada para consulta: "))
    agendaPaciente['hora'] = str(input("digite a hora desejada para consulta: "))

    print(agendaPaciente)
    print("Solicitação de consulta concluída!")

def programaGestor():
#programa Gestor
    print(agendaMedico)
    print(agendaPaciente)

    consultaMedico["paciente"] = str(input("Digite o nome do paciente da consulta a marcar: "))
    consultaMedico["medico"] = str(input("Digite o nome do médico que fará a consulta: "))
    consultaMedico["especialidade"] = str(input("Digite a especialidade do médico que fará a consulta: "))
    consultaMedico["data"] = str(input("Digite a data da consulta: "))
    consultaMedico["hora"] = str(input("Digite a hora da consulta: "))

    print(consultaMedico)
    print("Consulta marcada com sucesso!")
    
# Login
def login():
    i=1
    print('     * Login *     ')
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

# Login de cada usuário
def loginPaciente():
    i=1
    x = input('Usuário: ')
    y = input('Senha: ')
    for i in range(i,4,1):
        if(x == pacientes[i]) and (y == pacientes[i+0.1]):
            print('Bem vindo(a)!')
            programaPaciente()
        else:
            if i==4:
                if(x != pacientes[i]) and (y != pacientes[i+0.1]):
                    print('usuário ou senha incorretos!')
                else:
                    print('Bem vindo(a)!')
                    programaPaciente()
            else:
                continue

def loginMedico():
    i=1
    x = input('Usuário: ')
    y = input('Senha: ')
    for i in range(i,4,1):
        if(x == medicos[i]) and (y == medicos[i+0.1]):
            print('Bem vindo(a)!')
            programaMedico()
        else:
            if i==4:
                if(x != medicos[i]) and (y != medicos[i+0.1]):
                    print('usuário ou senha incorretos!')
                else:
                    print('Bem vindo(a)!')
                    programaMedico()
            else:
                continue

def loginGestor():
    i=1
    x = input('Usuário: ')
    y = input('Senha: ')
    for i in range(i,4,1):
        if(x == gestor[i]) and (y == gestor[i+0.1]):
            print('Bem vindo(a)!')
            programaGestor()
        else:
            if i==4:
                if(x != gestor[i]) and (y != gestor[i+0.1]):
                    print('usuário ou senha incorretos!')
                else:
                    print('Bem vindo(a)!')
                    programaGestor()
            else:
                continue

def loginAdm():
    x = input('Usuário: ')
    y = input('Senha: ')
    if(x == adm["01"]) and (y == adm["S1"]):
        print('Bem vindo(a) {} !'.format(adm["01"]))
        cadastrar()
    else:
        print("Usuário ou senha incorretos!")

# Cadastrar paciente,medico,gestor
def cadastrar():
    i=1
    escolhaAdm()
    arm = input("Escolha o usuário a cadastrar: ")
    #cadastro Paciente
    if arm == '1':
        nome = input("Digite um nome para o usuário: ")
        senha = input("Digite uma senha para o usuário: ")
        if ((pacientes[i] != "") and (pacientes[i+0.1] != "")):
            while ((pacientes[i] != "") and (pacientes[i+0.1] != "")):
                i=i+1
                if ((pacientes[i] == "") and (pacientes[i+0.1] == "")):
                    pacientes[i] = nome
                    pacientes[i+0.1] = senha             
                    print("Cadastro realizado com sucesso!!!")
                    print(pacientes)
                    break
        continuarOUsair()
            
    #cadastro Médico
    elif arm == '2':
        nome = input("Digite um nome para o usuário: ")
        senha = input("Digite uma senha para o usuário: ")
        if ((medicos[i] != "") and (medicos[i+0.1] != "")):
            while ((medicos[i] != "") and (medicos[i+0.1] != "")):
                i=i+1
                if ((medicos[i] == "") and (medicos[i+0.1] == "")):
                    medicos[i] = nome
                    medicos[i+0.1] = senha             
                    print("Cadastro realizado com sucesso!!!")
                    print(medicos)
                    break
        continuarOUsair()

    #cadastro Gestor
    elif arm == '3':
        nome = input("Digite um nome para o usuário: ")
        senha = input("Digite uma senha para o usuário: ")
        if ((gestor[i] != "") and (gestor[i+0.1] != "")):
            while ((gestor[i] != "") and (gestor[i+0.1] != "")):
                i=i+1
                if ((gestor[i] == "") and (gestor[i+0.1] == "")):
                    gestor[i] = nome
                    gestor[i+0.1] = senha             
                    print("Cadastro realizado com sucesso!!!")
                    print(gestor)
                    break
        continuarOUsair()
             
    else:
        print('usuário ou senha incorretos!')

# continuar cadastrando ou sair 
def continuarOUsair():
    arm2=int(input("Digite 1 para continuar cadastrando ou 2 para sair: "))
    if arm2== 1:
        cadastrar()
    elif arm2== 2:
        login()
    else:
        print('Escolha a opção 1 ou 2!!!')

#exibir opções de Login
def escolha():
    print('')
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
# FIM FUNÇÕES #

#Inicio do programa
login()


                # DESENVOLVIMENTO
#Programa Medico
    #disponibiliza sua agenda (horario entrada/saida) -
    #visualiza consultas marcadas em seu nome


#Programa Paciente
    #pode ver os horários/médicos disponiveis
    #faz o pedido de consulta (atribuido pelo gestor) com os dados:
    #                               data,hora,medico,especialidade


#Programa Gestor
    #exibir tabelas do medico e paciente
    #atribui horário do paciente ao medico
