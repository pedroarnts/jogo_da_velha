"""Loop principal do Jogo da Velha (dois jogadores ou 1 jogador vs. IA)."""

from __future__ import annotations

from . import ia
from .tabuleiro import Tabuleiro

SIMBOLOS = {1: "X", 2: "O"}
TOTAL_CASAS = 9

MODO_DOIS_JOGADORES = 1
MODO_CONTRA_COMPUTADOR = 2
JOGADOR_COMPUTADOR = 2  # o computador sempre joga como jogador 2 ('O')


def mostrar_boas_vindas() -> None:
    print("Olá! Este é o Jogo da Velha!\n")
    print("Digite a posição da sua jogada na forma: linha e coluna (de 0 a 2).")
    print("Ou seja, a primeira linha e primeira coluna será: (0, 0)\n")
    print("Antes de começarmos, veja as posições possíveis:")
    print("[ (0,0) ]\t[ (0,1) ]\t[ (0,2) ]")
    print("[ (1,0) ]\t[ (1,1) ]\t[ (1,2) ]")
    print("[ (2,0) ]\t[ (2,1) ]\t[ (2,2) ]\n")
    print("O primeiro jogador usa (X) e o segundo usa (O).")
    print("Ganha quem completar uma linha, coluna ou diagonal. Bom jogo!\n")


def escolher_modo() -> int:
    """Pergunta se a partida será entre duas pessoas ou contra o computador."""
    while True:
        print("Escolha o modo de jogo:")
        print(f"  {MODO_DOIS_JOGADORES} - Dois jogadores")
        print(f"  {MODO_CONTRA_COMPUTADOR} - Um jogador contra o computador (IA)")
        escolha = input("Digite sua opção: ").strip()
        if escolha in (str(MODO_DOIS_JOGADORES), str(MODO_CONTRA_COMPUTADOR)):
            return int(escolha)
        print("Opção inválida. Tente novamente.\n")


def ler_numero(mensagem: str) -> int:
    """Lê um inteiro do teclado, pedindo novamente em caso de entrada inválida."""
    while True:
        valor = input(mensagem).strip()
        if valor.lstrip("-").isdigit():
            return int(valor)
        print("Entrada inválida. Digite apenas um número inteiro.")


def pedir_jogada(tabuleiro: Tabuleiro, jogador: int) -> tuple[int, int]:
    """Pede linha e coluna ao jogador até que a jogada seja válida."""
    while True:
        print(f"\nVocê é o jogador {jogador}. Por favor, escolha sua jogada:")
        linha = ler_numero("Digite a linha (0-2): ")
        coluna = ler_numero("Digite a coluna (0-2): ")

        if tabuleiro.casa_livre(linha, coluna):
            return linha, coluna

        print("#################################")
        print("Jogada inválida: posição fora do tabuleiro ou já ocupada!")
        print("#################################")


def obter_jogada(tabuleiro: Tabuleiro, jogador: int, modo: int) -> tuple[int, int]:
    """Obtém a próxima jogada: de um humano, ou da IA quando for a vez dela."""
    if modo == MODO_CONTRA_COMPUTADOR and jogador == JOGADOR_COMPUTADOR:
        simbolo_ia = SIMBOLOS[JOGADOR_COMPUTADOR]
        simbolo_humano = SIMBOLOS[1]
        linha, coluna = ia.escolher_jogada(tabuleiro, simbolo_ia, simbolo_humano)
        print(f"\nO computador jogou em ({linha}, {coluna}).")
        return linha, coluna

    return pedir_jogada(tabuleiro, jogador)


def jogar_partida(modo: int) -> None:
    """Executa uma partida completa do Jogo da Velha no modo escolhido."""
    tabuleiro = Tabuleiro()
    jogador = 1

    print("#####################################################")
    print("Este é o nosso tabuleiro, por favor, inicie a jogada!")
    print("#####################################################")
    print(tabuleiro)

    for jogada_atual in range(1, TOTAL_CASAS + 1):
        linha, coluna = obter_jogada(tabuleiro, jogador, modo)
        simbolo = SIMBOLOS[jogador]

        tabuleiro.jogar(linha, coluna, simbolo)
        print(f"\nA posição ({linha}, {coluna}) foi preenchida com ({simbolo}).\n")
        print(tabuleiro)

        vencedor = tabuleiro.vencedor()
        if vencedor is not None:
            if modo == MODO_CONTRA_COMPUTADOR and vencedor == SIMBOLOS[JOGADOR_COMPUTADOR]:
                print("\nO computador venceu! Tente novamente. 🤖\n")
            else:
                print(f"\nA pessoa que escolheu ({vencedor}) venceu! 🎉\n")
            return

        if jogada_atual == TOTAL_CASAS:
            break

        jogador = 2 if jogador == 1 else 1

    print("\nDeu velha! Ninguém venceu desta vez. Jogue novamente!\n")


def jogar_novamente() -> bool:
    resposta = input("Quer jogar novamente? (s/n): ").strip().lower()
    return resposta in ("s", "sim")


def main() -> None:
    """Ponto de entrada: joga partidas até o usuário decidir parar."""
    mostrar_boas_vindas()
    modo = escolher_modo()

    continuar = True
    while continuar:
        jogar_partida(modo)
        continuar = jogar_novamente()
    print("\nObrigado por jogar! Até a próxima. 👋")


if __name__ == "__main__":
    main()
