"""Agenda 11 - Desenvolvimento de Sistemas I: Controle de Níveis de Água."""

from colorama import Fore, Style, init

init(autoreset=False)

NIVEIS = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)",
]


def definir_cor(nivel):
    """Retorna a cor correspondente a um nível de 1 a 5."""
    cores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE]
    if 1 <= nivel <= len(cores):
        return cores[nivel - 1]
    raise ValueError("O nível deve estar entre 1 e 5.")


def exibir_situacao(nivel):
    """Exibe a situação do reservatório e restaura a cor do terminal."""
    if not 1 <= nivel <= len(NIVEIS):
        raise ValueError("O nível deve estar entre 1 e 5.")
    mensagem = NIVEIS[nivel - 1]
    print(f"{definir_cor(nivel)}Nível {nivel}: {mensagem}{Style.RESET_ALL}")


def main():
    print("=== MONITORAMENTO DO RESERVATÓRIO ===")
    for nivel in range(1, len(NIVEIS) + 1):
        exibir_situacao(nivel)
    print("Simulação concluída.")


if __name__ == "__main__":
    main()
