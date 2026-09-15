import unittest

from jogo_da_velha import ia
from jogo_da_velha.tabuleiro import Tabuleiro


class TestIA(unittest.TestCase):
    def test_ia_completa_vitoria_quando_possivel(self) -> None:
        """Se a IA (O) já tem duas em linha, deve jogar na terceira e vencer."""
        tabuleiro = Tabuleiro()
        tabuleiro.jogar(0, 0, "O")
        tabuleiro.jogar(0, 1, "O")
        tabuleiro.jogar(1, 0, "X")
        tabuleiro.jogar(1, 1, "X")

        jogada = ia.escolher_jogada(tabuleiro, simbolo_ia="O", simbolo_humano="X")
        self.assertEqual(jogada, (0, 2))

    def test_ia_bloqueia_vitoria_do_adversario(self) -> None:
        """Se o humano (X) está prestes a vencer, a IA deve bloquear."""
        tabuleiro = Tabuleiro()
        tabuleiro.jogar(0, 0, "X")
        tabuleiro.jogar(0, 1, "X")
        tabuleiro.jogar(1, 0, "O")

        jogada = ia.escolher_jogada(tabuleiro, simbolo_ia="O", simbolo_humano="X")
        self.assertEqual(jogada, (0, 2))

    def test_ia_nunca_perde_contra_jogadas_aleatorias_otimas(self) -> None:
        """A IA jogando contra si mesma (dois lados ótimos) deve sempre empatar."""
        tabuleiro = Tabuleiro()
        simbolos = {"X": "O", "O": "X"}
        vez = "X"

        while tabuleiro.vencedor() is None and not tabuleiro.cheio():
            adversario = simbolos[vez]
            linha, coluna = ia.escolher_jogada(tabuleiro, simbolo_ia=vez, simbolo_humano=adversario)
            tabuleiro.jogar(linha, coluna, vez)
            vez = adversario

        self.assertIsNone(tabuleiro.vencedor())
        self.assertTrue(tabuleiro.cheio())

    def test_ia_nao_deixa_tabuleiro_alterado_apos_escolher(self) -> None:
        """escolher_jogada não deve ter efeitos colaterais no tabuleiro."""
        tabuleiro = Tabuleiro()
        tabuleiro.jogar(1, 1, "X")
        estado_antes = str(tabuleiro)

        ia.escolher_jogada(tabuleiro, simbolo_ia="O", simbolo_humano="X")

        self.assertEqual(estado_antes, str(tabuleiro))


if __name__ == "__main__":
    unittest.main()
