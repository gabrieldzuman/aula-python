def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        return m

def usuario_escolhe_jogada(n, m):
    while True:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada < 1 or jogada > m or jogada > n:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    if n % (m + 1) == 0:
        print("Computador começa!")
        vez_do_computador = True
    else:
        print("Você começa!")
        vez_do_computador = False
        
    while n > 0:
        if vez_do_computador:
            jogada = computador_escolhe_jogada(n, m)
            print("O computador tirou {} peça(s).".format(jogada))
            vez_do_computador = False
        else:
            jogada = usuario_escolhe_jogada(n, m)
            print("Você tirou {} peça(s).".format(jogada))
            vez_do_computador = True
        n -= jogada
        print("Agora restam {} peças no tabuleiro.".format(n))
    
    if vez_do_computador:
        print("Você ganhou!")
    else:
        print("O computador ganhou!")

def campeonato():
    placar_usuario = 0
    placar_computador = 0
    
    for rodada in range(1, 4):
        print("\n**** Rodada {} ****".format(rodada))
        resultado = partida()
        if "Você ganhou" in resultado:
            placar_usuario += 1
        else:
            placar_computador += 1
    
    print("\nPlacar: Você {} X {} Computador".format(placar_usuario, placar_computador))

def main():
    print("Bem-vindo ao jogo do NIM!")
    escolha = int(input("Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n"))

    if escolha == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    elif escolha == 2:
        print("Você escolheu um campeonato!")
        campeonato()
    else:
        print("Opção inválida! Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()
