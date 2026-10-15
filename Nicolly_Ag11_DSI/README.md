# Controle de Níveis de Água — Agenda 11 (DS I)

Projeto em Python para simular o monitoramento de um reservatório de água no terminal, com mensagens coloridas usando a biblioteca `colorama`.

## Requisitos

- Python 3
- Biblioteca `colorama`

## Como executar

1. Baixe ou clone este repositório.
2. Abra o terminal na pasta `Nicolly_Ag11_DSI`.
3. Instale a dependência:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Execute o programa:

   ```bash
   python main.py
   ```

> No Windows, caso `python` não funcione, experimente `py`.

## Níveis monitorados

| Nível | Situação | Cor |
|---|---|---|
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

## Funcionamento

A lista `NIVEIS` armazena as cinco situações do reservatório. A função `definir_cor(nivel)` escolhe a cor correspondente. A função `exibir_situacao(nivel)` imprime a mensagem e utiliza `Style.RESET_ALL` para restaurar o estilo do terminal. A função `main()` simula os cinco níveis em sequência, sem precisar digitar dados.

## Exemplo de saída

```text
=== MONITORAMENTO DO RESERVATÓRIO ===
Nível 1: Muito baixo (crítico)
Nível 2: Baixo
Nível 3: Médio
Nível 4: Alto
Nível 5: Muito alto (alerta)
Simulação concluída.
```

No terminal, cada linha de nível aparece com sua cor correspondente.
