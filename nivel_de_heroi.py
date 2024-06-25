print("Olá nobre aventureiro!\n")
print("Estou aqui para guia-lo nessa nova jornada!")
nome = input("Digite seu nome: ")
print(f"Bem-Vindo ao desafio do héroi: \n" + nome )
print("\nAgora vamos descobrir a sua força!")
print("\nVocê sabia que medimos a experiência de nossos aventureiros pela quantidade de Goblins vencidos?\n")
xp = int(input(f"Então me diga: Quantos Goblins você já enfrentou nessas terras, {nome}?\n"))
if xp < 1000:
        nivel = "Ferro"
elif xp < 2001:
            nivel = "Bronze"
elif xp < 5001:
        nivel = "Prata"
elif xp < 7001:
        nivel = "Ouro"
elif xp < 8001:
        nivel = "Platina"
elif xp < 9001:
        nivel = "Ascendente"
elif xp < 10001:
        nivel = "Imortal"
else:
        nivel = "Radiante"
print(f"\nO Herói de nome {nome} está no nível \n"  + nivel )

print("\nAgora volte ao trabalho!")
