"""Representação e regras do tabuleiro do Jogo da Velha."""

from __future__ import annotations

VAZIO = " "
LINHAS_VENCEDORAS = (
    # linhas
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    # colunas
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    # diagonais
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
)


class Tabuleiro:
    """Matriz 3x3 do jogo da velha, com as regras de vitória e empate."""

    TAMANHO = 3

    def __init__(self) -> None:
        self._grade = [[VAZIO] * self.TAMANHO for _ in range(self.TAMANHO)]

    def posicao_valida(self, linha: int, coluna: int) -> bool:
        """Verifica se (linha, coluna) existe dentro do tabuleiro."""
        return 0 <= linha < self.TAMANHO and 0 <= coluna < self.TAMANHO

    def casa_livre(self, linha: int, coluna: int) -> bool:
        """Verifica se a posição existe e ainda está vazia."""
        return self.posicao_valida(linha, coluna) and self._grade[linha][coluna] == VAZIO

    def jogar(self, linha: int, coluna: int, simbolo: str) -> None:
        """Marca `simbolo` ('X' ou 'O') na posição informada."""
        self._grade[linha][coluna] = simbolo

    def cheio(self) -> bool:
        """True quando não há mais casas vazias."""
        return all(casa != VAZIO for linha in self._grade for casa in linha)

    def casas_vazias(self) -> list[tuple[int, int]]:
        """Lista todas as posições (linha, coluna) ainda vazias."""
        return [
            (i, j)
            for i in range(self.TAMANHO)
            for j in range(self.TAMANHO)
            if self._grade[i][j] == VAZIO
        ]

    def vencedor(self) -> str | None:
        """Retorna 'X' ou 'O' se houver um vencedor, senão None."""
        for (l1, c1), (l2, c2), (l3, c3) in LINHAS_VENCEDORAS:
            valores = (self._grade[l1][c1], self._grade[l2][c2], self._grade[l3][c3])
            if valores[0] != VAZIO and valores[0] == valores[1] == valores[2]:
                return valores[0]
        return None

    def __str__(self) -> str:
        linhas = []
        for i, linha in enumerate(self._grade):
            linhas.append("".join(f"[ {casa} ]" for casa in linha))
        return "\n".join(linhas)
