import os 

# LOGIN 
def login():
    user = input("Login: ")
    senha = input("Senha: ")
    if user == "admin" and senha == "123":
        print("Login feito com sucesso")
        os.system("cls")
        calculadora()
    else:
        print("Login ou senha inválidos.")
        return login()

def principal():
    msg_inicial = input("[1] Login\n")

    while True:
        if msg_inicial == "1":
            login()
            break
        else:
            print("Opção inválida.")
            msg_inicial = input("[1] Login;   [2] Criar conta] \n")

def calculadora():
    # Operações básicas da calculadora
    def adicao(a, b):
        return a + b

    def subtracao(a, b):
        return a - b

    def multiplicacao(a, b):
        return a * b

    def divisao(a, b):
        if b == 0:
            return "Erro: divisão por zero"
        else:
            return a / b

    
    while True:
        # Coloque os numeros aqui
        operacao = input("Digite a operação desejada (+, -, *, /) ou 'q' para sair: ")
        if operacao == "q":
            break
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Aqui as operações serão executadas 
        if operacao == "+":
            resultado = adicao(num1, num2)
        elif operacao == "-":
            resultado = subtracao(num1, num2)
        elif operacao == "*":
            resultado = multiplicacao(num1, num2)
        elif operacao == "/":
            resultado = divisao(num1, num2)
        else:
            resultado = "Operação inválida"

        # Saída de dados
        print(f"Resultado: {resultado}\n")

principal()
