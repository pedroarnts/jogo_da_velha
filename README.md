# 🎮 Jogo da Velha (Tic-Tac-Toe)

[![CI](https://github.com/pedroarnts/joga_da_velha/actions/workflows/ci.yml/badge.svg)](https://github.com/pedroarnts/joga_da_velha/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Jogo da velha clássico para dois jogadores, jogado no terminal. Este projeto começou como um exercício em **Portugol** (disciplina de lógica de programação) e foi reescrito em **Python**, com o código organizado em módulos, testes automatizados e integração contínua.

```
#####################################################
Este é o nosso tabuleiro, por favor, inicie a jogada!
#####################################################
[   ][   ][   ]
[   ][   ][   ]
[   ][   ][   ]

Você é o jogador 1. Por favor, escolha sua jogada:
Digite a linha (0-2):
```

## ✨ Funcionalidades

- Dois modos de jogo: **2 jogadores** (X e O) ou **1 jogador contra o computador**.
- IA baseada no algoritmo **minimax**, que joga de forma ótima e nunca perde — no máximo empata.
- Validação de jogadas: impede posições fora do tabuleiro ou já ocupadas.
- Detecção de vitória em linha, coluna ou diagonal, e detecção de empate ("deu velha").
- Opção de jogar várias partidas seguidas sem reiniciar o programa.
- Suíte de testes unitários cobrindo as regras do tabuleiro e o comportamento da IA.
- Pipeline de CI (GitHub Actions) rodando os testes em várias versões do Python a cada push.

## 📂 Estrutura do projeto

```
joga_da_velha/
├── src/
│   └── jogo_da_velha/
│       ├── __init__.py
│       ├── __main__.py      # permite `python -m jogo_da_velha`
│       ├── tabuleiro.py      # regras e estado do tabuleiro
│       ├── ia.py             # IA do computador (algoritmo minimax)
│       └── jogo.py           # loop do jogo e interação com o jogador
├── tests/
│   ├── test_tabuleiro.py     # testes unitários das regras
│   └── test_ia.py            # testes unitários da IA (minimax)
├── portugol_original/        # versão original em Portugol (histórico do aprendizado)
├── .github/workflows/ci.yml  # integração contínua
├── pyproject.toml
├── LICENSE
└── README.md
```

## 🚀 Como jogar

Pré-requisito: Python 3.10 ou superior.

```bash
# 1. Clone o repositório
git clone https://github.com/pedroarnts/joga_da_velha.git
cd joga_da_velha

# 2. Rode o jogo
python -m src.jogo_da_velha
# ou, se instalar o pacote (veja abaixo):
jogo-da-velha
```

### Instalação como pacote (opcional)

```bash
pip install -e .
jogo-da-velha
```

## 🧪 Rodando os testes

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

## 🕹️ Como jogar uma partida

1. Ao iniciar, escolha o modo: **2 jogadores** ou **contra o computador**.
2. O jogador 1 usa `X` e o jogador 2 (ou o computador) usa `O`.
3. Em cada turno, digite a linha e a coluna da jogada (números de `0` a `2`).
4. O tabuleiro é reimpresso após cada jogada.
5. O jogo termina quando alguém completa uma linha, coluna ou diagonal, ou quando todas as 9 casas são preenchidas (empate).

### 🤖 Sobre a IA

No modo contra o computador, a IA usa o algoritmo **minimax**: ela simula todas as jogadas possíveis até o fim da partida e escolhe sempre a melhor opção, assumindo que você também joga bem. Isso significa que ela **nunca perde** — o melhor resultado possível contra ela é o empate. É uma ótima forma de estudar como decisões podem ser exploradas de forma recursiva em uma árvore de jogo.

## 📜 Do Portugol ao Python

A pasta [`portugol_original/`](portugol_original) guarda os quatro estágios em que este jogo foi desenvolvido originalmente em Portugol, como exercício de lógica de programação:

1. `01_desenho_tabuleiro.por` — desenho do tabuleiro de referência.
2. `02_indicando_jogador_e_jogada.por` — alternância de jogadores e leitura de jogadas.
3. `03_verifica_vencedor.por` — lógica de verificação de vencedor.
4. `04_completo_final.por` — jogo completo e funcional em Portugol.

A versão em Python reorganiza essa mesma lógica em módulos reutilizáveis (`Tabuleiro` e `jogo`), adiciona validação de entrada mais robusta e testes automatizados.

## 🛣️ Possíveis melhorias futuras

- [x] Modo de um jogador contra o computador (IA com minimax).
- [ ] Níveis de dificuldade (ex.: IA "fácil" que erra de propósito às vezes).
- [ ] Interface gráfica (ex.: com `tkinter` ou `pygame`).
- [ ] Placar de vitórias entre partidas.

## 📄 Licença

Este projeto está sob a licença MIT — veja o arquivo [LICENSE](LICENSE) para mais detalhes.
