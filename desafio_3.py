'''
Copa algoritmia y programacion 2024
Desafio: 3

Tema: Penales entre Argentina (Usuario) y Paises Bajos (PC)
'''
# Modulos
import random

# Funciones
def ingreso_datos(mensaje: str, tipo_dato=int):
    '''
    Valida el ingreso de datos, segun el tipo de dato. Por defecto, es int.
    '''
    flag: bool = True
    while flag:
        try:
            dato: tipo_dato = tipo_dato(input(mensaje))
            flag: bool = False
        except ValueError:
            print(f'El tipo de dato ingresado es incorrecto. Por favor intente nuevamente...')
    return dato

def es_par(n: int):
    '''
    Devuelve True si el numero n es par, de lo contrario, devuelve False.
    '''
    return n % 2 == 0

def eleccion_usuario(_ronda: int, corte_inicial: int, corte_final: int):
    '''
    Valida que el ingreso del dato este en el rango numerico correspondiente, segun los valores pasados como argumento,
    y luego devuelve el valor ingresado.
    '''
    flag: bool = True
    while flag:
        objetivo: int = ingreso_datos(f'Elegi donde {'patear' if es_par(_ronda) else 'atajar'} ({corte_inicial}-{corte_final}): ')
        if (objetivo >= corte_inicial and objetivo <= corte_final):
            flag: bool = False
        else:
            print(f'El numero ingresado es incorrecto, intente nuevamente...')
    return objetivo

def eleccion_pc(_arco):
    '''
    Devuelve un valor al azar utilizando como base la lista pasada como argumento.
    '''
    return random.choice(_arco)

def es_gol(_eleccion_pateador: int, _eleccion_arquero: int):
    '''
    Valida y devuelve True si el pateador convierte un gol. Las condiciones de conversion de gol son:
    - la eleccion de ambos jugadores NO debe ser cualquiera de estas en la misma jugada: 2, 5, 8
    - Si no se cumple la anterior, la eleccion de ambos jugadores debe ser distinta
    '''
    if _eleccion_pateador in (2, 5, 8) and _eleccion_arquero in (2, 5, 8):
        return False # Atajada
    elif _eleccion_pateador != _eleccion_arquero:
        return True # Gol
    else:
        return False # Atajada

def imprimir_marcador(_ronda, _equipo1, _equipo2, _tiro_equipo1, _tiro_equipo2, _resultado):
    '''
    Imprime por terminal el estado del marcador
    '''
    print(
        f'{'-'*40}',
        f'Ronda: {_ronda}',
        f'{'-'*7}',
        f'Marcador: \n\t{
            f'Argentina: {_equipo1}'
        }\n\t{
            f'Paises bajos: {_equipo2}'
        }',
        f'{'-'*7}',
        f'Coordenadas de tiro: \n\t{
            f'Argentina: {_tiro_equipo1}'
        }\n\t{
            f'Paises Bajos: {_tiro_equipo2}'
        }',
        f'{'-'*7}',
        f'Resultado: {_resultado}',
        f'{'-'*40}',
        sep='\n'
    )

def se_puede_finalizar_adelantado(_lista_jugador_1: list, _lista_jugador_2: list, _finalizar_juego: bool=False):
    '''
    Evalua y retorna True en el caso que los tiros aún pendientes de ambos jugadores no alcancen para un posible empate o dar vuelta el partido,
    caso contrario, devuelve False.

    Ejemplo:
        - Jugador 1 ['N', 'N', 'N', '', '']
        - Jugador 2 ['Y', 'Y', 'Y', '', '']\n
    Resultado: devuelve False porque Jugador 1 no llega a empatar el partido.
    '''
    cant_goles_jugador_1: int = _lista_jugador_1.count('Y')
    cant_goles_jugador_2: int = _lista_jugador_2.count('Y')
    goles_jugador_menos_goles: int = min(cant_goles_jugador_1, cant_goles_jugador_2)
    goles_jugador_mas_goles: int = max(cant_goles_jugador_1, cant_goles_jugador_2)
    
    tiros_pendientes_jugador1: int = _lista_jugador_1.count('')
    tiros_pendientes_jugador2: int = _lista_jugador_2.count('')
    diferencia_goles: int = goles_jugador_mas_goles - goles_jugador_menos_goles
    if not es_par(tiros_pendientes_jugador1 + tiros_pendientes_jugador2):
        total_tiros_pendientes = (tiros_pendientes_jugador1 + tiros_pendientes_jugador2 + 1) // 2
    else:
        total_tiros_pendientes = (tiros_pendientes_jugador1 + tiros_pendientes_jugador2) // 2

    if diferencia_goles > total_tiros_pendientes:
        return True
    else:
        return _finalizar_juego


# Variables
ARCO: tuple = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
)
argentina: list = [''] * 5
paises_bajos: list = [''] * 5

ejecutar_juego: bool = True # Variable que controla la ejecucion del juego
ronda: int = 0 # Variable acumuladora para contar las rondas de penales que van sucediendo 

# Ejecucion de la tanda de penales
for indice in range(len(argentina) + len(paises_bajos)): # 0 - 9
    if es_par(indice):
        ronda += 1
    
    # Pedido de coordenadas de tiro a cada equipo
    jugadora_argentina: int = eleccion_usuario(indice, ARCO[0], ARCO[-1])
    jugadora_paisesbajos: int = eleccion_pc(ARCO)

    # Anotar puntos
    if es_par(indice):
        # En indices pares patea Argentina
        argentina[ronda - 1] = 'Y' if es_gol(jugadora_argentina, jugadora_paisesbajos) else 'N'
        resultado: str = 'Gol' if argentina[ronda - 1] == 'Y' else 'Errado'
    else:
        # En indices impares patea Paises Bajos
        paises_bajos[ronda - 1] = 'Y' if es_gol(jugadora_paisesbajos, jugadora_argentina) else 'N'
        resultado: str = 'Gol' if paises_bajos[ronda - 1] == 'Y' else 'Errado'
    
    # Imprimimos el estado actual del marcador
    imprimir_marcador(ronda, argentina, paises_bajos, jugadora_argentina, jugadora_paisesbajos, resultado)

    # Evaluamos si es necesario seguir jugando rondas, o podemos finalizar de forma anticipada
    if se_puede_finalizar_adelantado(argentina, paises_bajos) and indice != (len(argentina) + len(paises_bajos) - 1):
        print('El juego finaliza de forma adelantada, dado que ya no hay posibilidad de empate o dar vuelta el resultado por parte del equipo perdedor.')
        break