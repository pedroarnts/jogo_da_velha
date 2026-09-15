"""IA do Jogo da Velha usando o algoritmo minimax.

O minimax explora todas as jogadas possíveis até o fim da partida e escolhe
a jogada que maximiza a chance de vitória da IA, assumindo que o adversário
também joga sempre da melhor forma possível. Como o Jogo da Velha é um jogo
pequeno (no máximo 9 jogadas), é possível calcular a árvore completa sem
nenhuma otimização extra — o resultado é uma IA que nunca perde: ela vence
sempre que o adversário erra, e empata quando o adversário também joga bem.
"""

from __future__ import annotations

import math

from .tabuleiro import VAZIO, Tabuleiro


def _minimax(tabuleiro: Tabuleiro, simbolo_ia: str, simbolo_humano: str,
             profundidade: int, maximizando: bool) -> int:
    """Retorna a pontuação da posição atual do ponto de vista da IA.

    Pontuações mais altas são melhores para a IA. A profundidade é usada
    para preferir vitórias mais rápidas e derrotas mais lentas.
    """
    vencedor = tabuleiro.vencedor()
    if vencedor == simbolo_ia:
        return 10 - profundidade
    if vencedor == simbolo_humano:
        return profundidade - 10
    if tabuleiro.cheio():
        return 0

    simbolo_da_vez = simbolo_ia if maximizando else simbolo_humano
    melhor_pontuacao = -math.inf if maximizando else math.inf

    for linha, coluna in tabuleiro.casas_vazias():
        tabuleiro.jogar(linha, coluna, simbolo_da_vez)
        pontuacao = _minimax(tabuleiro, simbolo_ia, simbolo_humano, profundidade + 1, not maximizando)
        tabuleiro.jogar(linha, coluna, VAZIO)  # desfaz a jogada simulada

        if maximizando:
            melhor_pontuacao = max(melhor_pontuacao, pontuacao)
        else:
            melhor_pontuacao = min(melhor_pontuacao, pontuacao)

    return int(melhor_pontuacao)


def escolher_jogada(tabuleiro: Tabuleiro, simbolo_ia: str, simbolo_humano: str) -> tuple[int, int]:
    """Escolhe a melhor jogada disponível para a IA no tabuleiro atual."""
    melhor_pontuacao = -math.inf
    melhor_jogada: tuple[int, int] | None = None

    for linha, coluna in tabuleiro.casas_vazias():
        tabuleiro.jogar(linha, coluna, simbolo_ia)
        pontuacao = _minimax(tabuleiro, simbolo_ia, simbolo_humano, profundidade=1, maximizando=False)
        tabuleiro.jogar(linha, coluna, VAZIO)  # desfaz a jogada simulada

        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_jogada = (linha, coluna)

    assert melhor_jogada is not None  # só é None se o tabuleiro já estiver cheio
    return melhor_jogada
