import random

regra = {
    1: 'Pedra',
    2: 'Papel',
    3: 'Tesoura'
}

APRESENTACAO = "Bem vindo ao jogo de Jokenpo!\n\nEscolha uma jogada:\n\n1-) Pedra\n2-) Papel\n3-) Tesoura"
print(APRESENTACAO)

player1 = int(input())
player2 = random.randint(1, 3)

jogada = regra[player2]
print(f'Jogada do computador: {jogada}')

if player1 == player2:
    print("Empate")
elif player1 == 1 and player2 == 3:
    print("Player 1 venceu")
elif player1 == 2 and player2 == 1:
    print("Player 1 venceu")
elif player1 == 3 and player2 == 2:
    print("Player 1 venceu")
else:
    print("Player 2 venceu")