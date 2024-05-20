# Importa el modulo random
import random

# Inicializa las listas con jugadoras de Argentina
jugadoras_arg=[
    ("Agustina Albertario", 19), 
    ("Cristina Cosentino", 13), 
    ("Julieta Jankunas", 28),
    ("Valentina Marcucci", 31), 
    ("Rocío Sánchez Moccia", 17), 
    ("Victoria Sauze Valdez", 18),
    ("Eugenia Trinchinetti", 22), 
    ("Valentina Costa Biondi", 32), 
    ("Agustina Gorzelany", 3),
    ("María José Granatto", 15), 
    ("Sofia Toccalino", 2), 
    ("Agostina Alonso", 5),
    ("Valentina Raposo", 4), 
    ("Clara Barberi", 14), 
    ("Delfina Thome", 4), 
    ("Sofía Cairo", 8),
    ("María Pilar Campoy", 23)
]

# Inicializa las listas con jugadoras de Australia
jugadoras_aus=[
    ("Ashlee Wells", 5), 
    ("Jocelyn Bartram", 19), 
    ("Rachel Lynch", 27), 
    ("Sophie Taylor", 1),
    ("Karri McMahon", 11), 
    ("Edwina Bone", 13), 
    ("Kaitlin Nobbs", 15), 
    ("Madison Fitzpatrick", 10),
    ("Amy Lawton", 4), 
    ("Karri Somerville", 20), 
    ("Kate Jenner", 22), 
    ("Georgia Wilson", 8),
    ("Lily Brazel", 9), 
    ("Greta Hayes", 12), 
    ("Stephanie Kershaw", 14), 
    ("Jane Claxton", 18)
]

# Generar pases al azar
def generar_pases(jugadoras_arg, jugadoras_aus):
    """Genera y devuelve una lista de 50000 pases al azar realizados por las jugadoras de un equipo (las jugadoras salen de la lista pasada como argumento)"""
    pases = []

    # Iteramos 50000 veces de forma no condicional, y asignamos valores a cada variable, que seran agregados a la lista que devolvera la funcion
    for _ in range(50000):
        equipo = random.choice(["Argentina", "Australia"]) # Random elige entre ambos paises
        jugadoras = jugadoras_arg if equipo == "Argentina" else jugadoras_aus
        jugador = random.choice(jugadoras) #Random elige entre las jugadoras del pais seleccionado al azar
        minutos = random.randint(1, 90) # Se selecciona el minuto del pase al azar entre 1 y 90
        resultado = random.choice([0, 1]) # Indica si el pase fue concretado (1) o si no lo fue (0)
        pases.append(f"{equipo};{jugador[1]};{jugador[0]};{resultado};{minutos}\n")
    return pases

pases = generar_pases(jugadoras_arg, jugadoras_aus)

# Crea el archivo con la funcion open(), y en caso que este ya haya sido creado, lo sobreescribe
with open("pases.txt", "w") as file:
    file.writelines(pases)