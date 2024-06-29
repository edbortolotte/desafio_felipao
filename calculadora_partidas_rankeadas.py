#vitorias - derrotas#
#"O Herói tem saldo de **{saldo de vitória}" está no nível de {nível}"

print("Olá nobre aventureiro!\n")
print("Estou aqui para guia-lo nessa nova jornada!\n")
nome = input("Digite seu nome:\n ")
print(f"Bem-Vindo ao desafio do héroi: \n" + nome )
print("\nAgora vamos descobrir o seu rank!\n")


def calcular_resultado():
    while True:
        try:
            vitorias = int(input("Digite o número de vitórias:\n"))
            if vitorias >= 0: 
                break
            else:
                print("O número de derrotas deve ser maior ou igual a 0.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
   
    while True:
        try:
            derrotas = int(input("Digite o número de derrotas:\n"))
            if derrotas >= 0: 
                break
            else:
                print("O número de derrotas deve ser maior ou igual a 0.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

   
    venceu = 10
    perdeu = -5
    pontos_de_vitoria:int = vitorias * venceu
    pontos_de_derrota:int  = derrotas * abs(perdeu)

    saldo_vitorias = pontos_de_vitoria - pontos_de_derrota
    

    if saldo_vitorias < 10:
        nivel = "Ferro"
    elif saldo_vitorias <= 20:
        nivel = "Bronze"
    elif saldo_vitorias <= 50:
        nivel = "Prata"
    elif saldo_vitorias <= 80:
        nivel = "Ouro"
    elif saldo_vitorias <= 90:
        nivel = "Diamante"
    elif saldo_vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "imortal"
   


    print(f"O Herói {nome.upper()} tem saldo de: {saldo_vitorias} e está no nível de: {nivel.upper()}")

calcular_resultado()