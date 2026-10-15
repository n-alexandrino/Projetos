from colorama import Fore, Style, init

init()

niveis = ["Muito baixo (crítico)", "Baixo", "Médio", "Alto", "Muito alto (alerta)"]


def cor_do_nivel(nivel):
    cores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE]
    return cores[nivel - 1]


def mostrar_nivel(nivel):
    print(cor_do_nivel(nivel) + "Nível " + str(nivel) + ": " + niveis[nivel - 1] + Style.RESET_ALL)


print("Controle de níveis de água")
print("-------------------------")

# Simulação dos cinco níveis do reservatório
for nivel in range(1, 6):
    mostrar_nivel(nivel)
