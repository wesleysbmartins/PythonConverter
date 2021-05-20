dadosPessoais=[]


def Cadastro(dados):

        resposta =input("Se deseja se cadastrar digite \"S\" : ").upper()
        while resposta == "S":
                cadastro=[input("Digite seu nome:\n"),
                        input("Digite sua nacionalidade:\n"),
                        input("Digite sua data de nascimento:\n"),
                        input("Digite seu CPF:\n")]
                dadosPessoais.append(cadastro)
                resposta = input("Digite \"S\" para refazer o Cadastro, ou Pressione ENTER para proseguir:").upper()
        print(dadosPessoais)


def Conversor(moedas):
    
    resposta="S"
    
    resposta=input("Deseja realizar uma conversão? \n\"S\" ou \"N\" : ").upper()
    
    if resposta=="S":
        resp="Nada"
        resp=input("Qual sua moeda?\n").upper()
        if resp=="DOLAR":
            valor = input("Quantos Dolares você tem?\n")
            valor2 = float(valor)
            outraMoeda="NADA"
            outraMoeda=input("Que moeda deseja comprar?\n").upper()
            if outraMoeda=="EURO":
                dolar = float
                dolar = 0.82
                total = float
                total = valor2 * dolar
                print("O total adquirido na conversão é de : ", total," Euros")
                print("________Obrigado por utilizar o PythonConverter!_________")
            elif outraMoeda=="REAL":
                dolar = float
                dolar = 5.37
                total = float
                total = valor2 * dolar
                print("O total adquirido na conversão é de : ", total, " Reais")
                print("________Obrigado por utilizar o PythonConverter!_________")
            else:
                print("******Selecione a Moeda Correta******\n",
                      "           EURO ou REAL\n",
                      "*************************************\n")
        elif resp=="EURO":
            valor = input("Quantos Euros você tem?\n")
            valor2 = float(valor)
            outraMoeda="NADA"
            outraMoeda=input("Que moeda deseja comprar?\n").upper()
            if outraMoeda=="DOLAR":
                euro = float
                euro = 1.21
                total = float
                total = valor2 * euro
                print("O total adquirido na conversão é de : ", total," Dolares")
                print("________Obrigado por utilizar o PythonConverter!_________")
            elif outraMoeda=="REAL":
                euro = float
                euro = 6.53
                total = float
                total = valor2 * euro
                print("O total adquirido na conversão é de : ", total, " Reais")
                print("________Obrigado por utilizar o PythonConverter!_________")
            else:
                print("******Selecione a Moeda Correta******\n",
                      "           DOLAR ou REAL\n",
                      "*************************************\n")
        elif resp=="REAL":
            valor = input("Quantos Reais você tem?\n")
            valor2 = float(valor)
            outraMoeda="NADA"
            outraMoeda=input("Que moeda deseja comprar?\n").upper()
            if outraMoeda=="EURO":
                real = float
                real = 0.15
                total = float
                total = valor2 * real
                print("O total adquirido na conversão é de : ", total," Euros")
                print("________Obrigado por utilizar o PythonConverter!_________")
            elif outraMoeda=="DOLAR":
                real = float
                real = 0.19
                total = float
                total = valor2 * real
                print("O total adquirido na conversão é de : ", total, " Dolares")
                print("________Obrigado por utilizar o PythonConverter!_________")
            else:
                print("******Selecione a Moeda Correta******\n",
                      "             DOLAR ou EURO\n",
                      "*************************************\n")
        elif resp != "DOLAR" or "EURO" or "REAL":
            print("!!!!!!!!!!!Moeda Inválida!!!!!!!!!!!!!",
                 "******Selecione a Moeda Correta******\n",
                 "             DOLAR ou EURO\n",
                 "*************************************\n")
        
        else:
            print("Obrigado por utilizar o PythonConverter!")

    elif resposta=="N":

        print("Tudo bem, quando quiser realizar uma conversão, estarei a disposição! :)")
        
    else:
        print("Lembrando que só trabalhamos com : Dolares, Reais e Euros.")