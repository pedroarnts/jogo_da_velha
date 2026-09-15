import unittest

from jogo_da_velha.tabuleiro import Tabuleiro


class TestTabuleiro(unittest.TestCase):
    def setUp(self) -> None:
        self.tabuleiro = Tabuleiro()

    def test_tabuleiro_comeca_vazio(self) -> None:
        self.assertIsNone(self.tabuleiro.vencedor())
        self.assertFalse(self.tabuleiro.cheio())

    def test_posicao_valida(self) -> None:
        self.assertTrue(self.tabuleiro.posicao_valida(0, 0))
        self.assertTrue(self.tabuleiro.posicao_valida(2, 2))
        self.assertFalse(self.tabuleiro.posicao_valida(3, 0))
        self.assertFalse(self.tabuleiro.posicao_valida(0, -1))

    def test_casa_livre_apos_jogada(self) -> None:
        self.assertTrue(self.tabuleiro.casa_livre(1, 1))
        self.tabuleiro.jogar(1, 1, "X")
        self.assertFalse(self.tabuleiro.casa_livre(1, 1))

    def test_vitoria_em_linha(self) -> None:
        for coluna in range(3):
            self.tabuleiro.jogar(0, coluna, "X")
        self.assertEqual(self.tabuleiro.vencedor(), "X")

    def test_vitoria_em_coluna(self) -> None:
        for linha in range(3):
            self.tabuleiro.jogar(linha, 2, "O")
        self.assertEqual(self.tabuleiro.vencedor(), "O")

    def test_vitoria_em_diagonal_principal(self) -> None:
        for i in range(3):
            self.tabuleiro.jogar(i, i, "X")
        self.assertEqual(self.tabuleiro.vencedor(), "X")

    def test_vitoria_em_diagonal_secundaria(self) -> None:
        self.tabuleiro.jogar(0, 2, "O")
        self.tabuleiro.jogar(1, 1, "O")
        self.tabuleiro.jogar(2, 0, "O")
        self.assertEqual(self.tabuleiro.vencedor(), "O")

    def test_empate_tabuleiro_cheio_sem_vencedor(self) -> None:
        jogadas = [
            (0, 0, "X"), (0, 1, "X"), (0, 2, "O"),
            (1, 0, "O"), (1, 1, "O"), (1, 2, "X"),
            (2, 0, "X"), (2, 1, "O"), (2, 2, "X"),
        ]
        for linha, coluna, simbolo in jogadas:
            self.tabuleiro.jogar(linha, coluna, simbolo)

        self.assertTrue(self.tabuleiro.cheio())
        self.assertIsNone(self.tabuleiro.vencedor())


if __name__ == "__main__":
    unittest.main()
