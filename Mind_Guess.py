import random
import json
from colorama import init, Fore, Style

init()

def cargar_ranking():
    try:
        with open("ranking.json", "r") as archivo:
            ranking = json.load(archivo)
    except FileNotFoundError:
        ranking = []
    return ranking

def guardar_ranking(ranking):
    with open("ranking.json", "w") as archivo:
        json.dump(ranking, archivo)

def ver_ranking():
    ranking = cargar_ranking()
    if ranking:
        ranking_ordenado = sorted(ranking, key=lambda x: x["intentos"])
        print(f"\n{Fore.YELLOW}Mejores puntuaciones:{Style.RESET_ALL}")
        for i, puntuacion in enumerate(ranking_ordenado, 1):
            print(f"{i}. {Fore.CYAN}{puntuacion['nombre']}{Style.RESET_ALL}: {Fore.GREEN}{puntuacion['intentos']}{Style.RESET_ALL} intentos")
    else:
        print(f"{Fore.YELLOW}Aún no hay puntuaciones en el ranking.{Style.RESET_ALL}")

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos_realizados = 0
    max_intentos = 10

    print(f"{Fore.CYAN}¡Bienvenido a 'Adivina el número'!{Style.RESET_ALL}")
    print("Estoy pensando en un número entre 1 y 100.")
    print(f"Tienes que adivinarlo en menos de {max_intentos} intentos.")

    nombre_jugador = input("Ingresa tu nombre: ")
    ranking = cargar_ranking()

    while intentos_realizados < max_intentos:
        intento = int(input("Introduce tu número: "))
        intentos_realizados += 1

        if intento < numero_secreto:
            print(f"{Fore.RED}Demasiado bajo.{Style.RESET_ALL}")
        elif intento > numero_secreto:
            print(f"{Fore.RED}Demasiado alto.{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}¡Felicitaciones, {nombre_jugador}! Adivinaste el número en {intentos_realizados} intentos!{Style.RESET_ALL}")
            ranking.append({"nombre": nombre_jugador, "intentos": intentos_realizados})
            guardar_ranking(ranking)
            ver_ranking()
            return

    print(f"{Fore.RED}¡Agotaste tus intentos! El número secreto era {numero_secreto}.{Style.RESET_ALL}")
    ver_ranking()

adivina_el_numero()
