import random

def get_computer_choice():
    choices = ['pedra', 'papel', 'tesoura']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Empate!"
    
    if (player_choice == 'pedra' and computer_choice == 'tesoura') or \
       (player_choice == 'papel' and computer_choice == 'pedra') or \
       (player_choice == 'tesoura' and computer_choice == 'papel'):
        return "Você ganhou!"
    
    return "Computador ganhou!"

def main():
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")
    
    while True:
        player_choice = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()
        
        if player_choice == 'sair':
            print("Obrigado por jogar!")
            break
        
        if player_choice not in ['pedra', 'papel', 'tesoura']:
            print("Escolha inválida. Tente novamente.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computador escolheu: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()
