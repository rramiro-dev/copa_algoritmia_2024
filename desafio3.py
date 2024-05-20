import random

def ingreso_datos(mensaje, tipo_dato=int):
    '''
        Validar con exepciones el ingreso de datos, segun el tipo de dato dado como argumento
    '''
    flag = True
    while flag:
        try:
            opcion = tipo_dato(input(mensaje))
            flag = False
        except ValueError:
            print(f'El tipo de dato es incorrecto, por favor ingrese un valor de tipo {tipo_dato}')
    return opcion

# Variables
ARCO = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
)

marcador = {
    'usuario': [0]*5, # [0, 0, 0, 0, 0]
    'pc': [0]*5 # [0, 0, 0, 0, 0]
}

tanda_desempate = list() # [0, 0]

indice_tiros = 0
for i in range(10): # 0 - 9
    # Va incrementando el indice de tiros, para agregar el gol o atajada correspondiente a la lista del usuario/pc segun corresponda en el marcador
    if i >= 1 and i % 2 == 0:
        indice_tiros += 1

    # Patea el usuario, ataja la pc
    if i % 2 == 0:
        usuario = ingreso_datos('Elegi donde patear [1-9]: ')
        pc = random.randint(1,len(ARCO))
    
    # Patea la pc, ataja el usuario
    else:
        usuario = ingreso_datos('Elegi donde atajar [1-9]: ')
        pc = random.randint(1,len(ARCO))
    
    # Otorgamos los puntos en el marcador

    # Validamos si el usuario/pc patean/atajan en cualquiera de las posiciones 2, 5, y/u 8
    if usuario in (2,5,8) and pc in (2,5,8):
        if i % 2 == 0: # Usuario patea
            marcador['usuario'][indice_tiros] = 'N'
            punto = 'pc'
        else:
            marcador['pc'][indice_tiros] = 'N'
            punto = 'usuario'
    
    else:
        if i % 2 == 0: # Usuario patea
            if usuario != pc:
                marcador['usuario'][indice_tiros] = 'Y'
                punto = 'usuario'
            else:
                marcador['usuario'][indice_tiros] = 'N'
                punto = 'pc'
        else: # PC patea
            if usuario != pc:
                marcador['pc'][indice_tiros] = 'Y'
                punto = 'pc'
            else:
                marcador['pc'][indice_tiros] = 'N'
                punto = 'pc'
    
    print(f'Ronda: {indice_tiros + 1}', 
          f'Usuario patea: {usuario}' if i % 2 == 0 else f'Usuario ataja: {usuario}', 
          f'PC Ataja: {pc}' if i % 2 == 0 else f'PC patea: {pc}', 
          f'Gana: {punto}', sep='\n')

print(marcador['usuario'])
print(marcador['pc'])


# Rondas para definir un empate de penales
if marcador['usuario'] == marcador['pc']:
    flag = True
    indice_tiros = 0
    while flag:
        indice_tiros += 1
        pos = 0 if not indice_tiros % 2 == 0 else 1

        # Patea usuario
        usuario = ingreso_datos('Elegi donde patear [1-9]: ' if not indice_tiros % 2 == 0 else 'Elegi donde atajar [1-9]: ')
        pc = random.randint(1,len(ARCO))
        
        
        # Validamos si el usuario/pc patean/atajan en cualquiera de las posiciones 2, 5, y/u 8
        if usuario in (2,5,8) and pc in (2,5,8):
            if not i % 2 == 0: # Usuario patea
                tanda_desempate[pos] = 'N'
                punto = 'pc'
            else: # Ataja usuario
                tanda_desempate[pos] = 'Y'
                punto = 'usuario'
        else:
            if not i % 2 == 0: # Usuario patea
                if usuario != pc:
                    tanda_desempate[pos] = 'Y'
                    punto = 'usuario'
                else:
                    tanda_desempate[pos] = 'N'
                    punto = 'pc'
            else: # Ataja usuario
                if usuario != pc:
                    tanda_desempate[pos] = 'N'
                    punto = 'pc'
                else:
                    tanda_desempate[pos] = 'Y'
                    punto = 'usuario'
        
        if tanda_desempate[0] == tanda_desempate[1]:
            if tanda_desempate[0] == 'Y':
                ganador = 'usuario'
            else:
                ganador = 'pc'

            flag = False

print(ganador)