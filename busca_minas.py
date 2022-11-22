import random
import copy

#LECTURA FICHERO
def leer_archivo():

    f = open('configuracion.txt')
    f = f.read()
    f = f.split('\n')

    dimension = int(f[0])
    minas = int(f[1])

    return dimension, minas

#CREAR TABLERO
def crear_tableros(dimension):

    tablero = []
    for i in range(0,dimension):
        tablero.append(['##']*dimension)


    tablero_actualizado = copy.deepcopy(tablero)

    return tablero, tablero_actualizado


#IMPRIMIR TABLERO
def pintar_tablero(tablero, dimension):

    for i in range(0,dimension):
        print(' '.join(tablero[i]))


#COLORCAR MINAS
def colocar_minas(tablero, dimension, minas):
    
    tablero_minas = copy.deepcopy(tablero)

    for i in range(0,minas):
        x = random.randint(0,dimension-1)
        y = random.randint(0,dimension-1)
        tablero_minas[x][y] = '**'

    #CELDAS CENTRALES

    for i in range(1,dimension-1):
        for j in range(1,dimension-1):
            if tablero_minas[i][j] != '**':
                numero = 0
                if tablero_minas[i][j+1] == '**':
                    numero += 1
                if tablero_minas[i][j-1] == '**':
                    numero += 1
                if tablero_minas[i-1][j] == '**':
                    numero += 1
                if tablero_minas[i+1][j] == '**':
                    numero += 1
                if tablero_minas[i-1][j-1] == '**':
                    numero += 1
                if tablero_minas[i-1][j+1] == '**':
                    numero += 1
                if tablero_minas[i+1][j-1] == '**':
                    numero += 1
                if tablero_minas[i+1][j+1] == '**':
                    numero += 1
                tablero_minas[i][j] = str(numero) + (' ')

    #ARRIBA IZQUIERDA

    if tablero_minas[0][0] != '**':
        numero = 0
        if tablero_minas[0][1] == '**':
            numero += 1
        if tablero_minas[1][1] == '**':
            numero += 1
        if tablero_minas[1][0] == '**':
            numero += 1
        tablero_minas[0][0] = str(numero) + (' ')

    #ARRIBA DERECHA

    if tablero_minas[0][dimension-1] != '**':
        numero = 0
        if tablero_minas[0][dimension-2] == '**':
            numero += 1
        if tablero_minas[1][dimension-1] == '**':
            numero += 1
        if tablero_minas[1][dimension-2] == '**':
            numero += 1
        tablero_minas[0][dimension-1] = str(numero) + (' ')

    #ABAJO IZQUIERDA

    if tablero_minas[dimension-1][0] != '**':
        numero = 0
        if tablero_minas[dimension-1][1] == '**':
            numero += 1
        if tablero_minas[dimension-2][1] == '**':
            numero += 1
        if tablero_minas[dimension-2][0] == '**':
            numero += 1
        tablero_minas[dimension-1][0] = str(numero) + (' ')


    #ABAJO DERECHA

    if tablero_minas[dimension-1][dimension-1] != '**':
        numero = 0
        if tablero_minas[dimension-1][dimension-2] == '**':
            numero += 1
        if tablero_minas[dimension-2][dimension-1] == '**':
            numero += 1
        if tablero_minas[dimension-2][dimension-2] == '**':
            numero += 1
        tablero_minas[dimension-1][dimension-1] = str(numero) + (' ')

    #FILA ARRIBA

    for i in range(1,dimension-1):
        if tablero_minas[0][i] != '**':
            numero = 0
            if tablero_minas[0][i-1] == '**':
                numero += 1
            if tablero_minas[0][i+1] == '**':
                numero += 1
            if tablero_minas[1][i-1] == '**':
                numero += 1
            if tablero_minas[1][i+1] == '**':
                numero += 1
            if tablero_minas[1][i] == '**':
                numero += 1
            tablero_minas[0][i] = str(numero) + ' '

    #FILA ABAJO

    for i in range(1,dimension-1):
        if tablero_minas[dimension-1][i] != '**':
            numero = 0
            if tablero_minas[dimension-1][i-1] == '**':
                numero += 1
            if tablero_minas[dimension-1][i+1] == '**':
                numero += 1
            if tablero_minas[dimension-2][i-1] == '**':
                numero += 1
            if tablero_minas[dimension-2][i+1] == '**':
                numero += 1
            if tablero_minas[dimension-2][i] == '**':
                numero += 1
            tablero_minas[dimension-1][i] = str(numero) + ' '


    #COLUMNA IZQUIERDA

    for i in range(1,dimension-1):
        if tablero_minas[i][0] != '**':
            numero = 0
            if tablero_minas[i-1][0] == '**':
                numero += 1
            if tablero_minas[i+1][0] == '**':
                numero += 1
            if tablero_minas[i-1][1] == '**':
                numero += 1
            if tablero_minas[i+1][1] == '**':
                numero += 1
            if tablero_minas[i][1] == '**':
                numero += 1
            tablero_minas[i][0] = str(numero) + ' '


    #COLUMNA DERECHA

    for i in range(1,dimension-1):
        if tablero_minas[i][dimension-1] != '**':
            numero = 0
            if tablero_minas[i-1][dimension-1] == '**':
                numero += 1
            if tablero_minas[i+1][dimension-1] == '**':
                numero += 1
            if tablero_minas[i-1][dimension-2] == '**':
                numero += 1
            if tablero_minas[i+1][dimension-2] == '**':
                numero += 1
            if tablero_minas[i][dimension-2] == '**':
                numero += 1
            tablero_minas[i][dimension-1] = str(numero) + ' '

    return tablero_minas

#COMPROBAR NO HAY MINAS REPETIDAS
def comprobar_minas(tablero_minas, minas):

    num_minas = 0
    for i in range(0,dimension):
        for j in range(0,dimension):
            if tablero_minas[i][j] == '**':
                num_minas += 1
    if num_minas == minas:
        correcto = True
    return correcto

#PEDIR COORDENADAS
def coordenadas(dimension):

    x = int(input(f'Introduce la fila (1,{dimension}): '))
    y = int(input(f'Introduce la columna (1,{dimension}): '))
    x = x-1
    y = y-1
    return x, y

#ACTUALIZAR TABLERO
def actualizar_tablero(tablero_minas, x, y):

    #CELDAS CENTRALES
    if  x > 0 and y > 0 and x < (dimension-1) and y < (dimension-1):

        tablero_actualizado[x][y] = tablero_minas[x][y]
        tablero_actualizado[x+1][y] = tablero_minas[x+1][y]
        tablero_actualizado[x-1][y] = tablero_minas[x-1][y]
        tablero_actualizado[x][y+1] = tablero_minas[x][y+1]
        tablero_actualizado[x][y-1] = tablero_minas[x][y-1]
        tablero_actualizado[x+1][y+1] = tablero_minas[x+1][y+1]
        tablero_actualizado[x+1][y-1] = tablero_minas[x+1][y-1]
        tablero_actualizado[x-1][y+1] = tablero_minas[x-1][y+1]
        tablero_actualizado[x-1][y-1] = tablero_minas[x-1][y-1]

    #ESQUINA ARRIBA IZQUIERDA
    if x == 0 and y == 0:

        tablero_actualizado[0][0] = tablero_minas[0][0]
        tablero_actualizado[0][1] = tablero_minas[0][1]
        tablero_actualizado[1][0] = tablero_minas[1][0]
        tablero_actualizado[1][1] = tablero_minas[1][1]

    #ESQUINA ARRIBA DERECHA
    if x == 0 and y == (dimension-1):

        tablero_actualizado[0][dimension-1] = tablero_minas[0][dimension-1]
        tablero_actualizado[0][dimension-2] = tablero_minas[0][dimension-2]
        tablero_actualizado[1][dimension-1] = tablero_minas[1][dimension-1]
        tablero_actualizado[1][dimension-2] = tablero_minas[1][dimension-2]

    #ESQUINA ABAJO IZQUIERDA
    if x == (dimension-1) and y == 0:

        tablero_actualizado[dimension-1][0] = tablero_minas[dimension-1][0]
        tablero_actualizado[dimension-1][1] = tablero_minas[dimension-1][1]
        tablero_actualizado[dimension-2][0] = tablero_minas[dimension-2][0]
        tablero_actualizado[dimension-2][1] = tablero_minas[dimension-2][1]

    #ESQUINA ABAJO DERECHA
    if x == (dimension-1) and y == (dimension-1):

        tablero_actualizado[dimension-1][dimension-1] = tablero_minas[dimension-1][dimension-1]
        tablero_actualizado[dimension-2][dimension-1] = tablero_minas[dimension-2][dimension-1]
        tablero_actualizado[dimension-2][dimension-2] = tablero_minas[dimension-2][dimension-2]
        tablero_actualizado[dimension-1][dimension-2] = tablero_minas[dimension-1][dimension-2]

    #PRIMERA FILA
    if x == 0 and y > 0 and y < (dimension-1):

        tablero_actualizado[0][y] = tablero_minas[0][y]
        tablero_actualizado[0][y+1] = tablero_minas[0][y+1]
        tablero_actualizado[0][y-1] = tablero_minas[0][y-1]
        tablero_actualizado[1][y] = tablero_minas[1][y]
        tablero_actualizado[1][y+1] = tablero_minas[1][y+1]
        tablero_actualizado[1][y-1] = tablero_minas[1][y-1]

    #ÚLTIMA FILA
    if x == (dimension-1) and y > 0 and y < (dimension-1):

        tablero_actualizado[dimension-1][y] = tablero_minas[dimension-1][y]
        tablero_actualizado[dimension-1][y-1] = tablero_minas[dimension-1][y-1]
        tablero_actualizado[dimension-1][y+1] = tablero_minas[dimension-1][y+1]
        tablero_actualizado[dimension-2][y-1] = tablero_minas[dimension-2][y-1]
        tablero_actualizado[dimension-2][y] = tablero_minas[dimension-2][y]
        tablero_actualizado[dimension-2][y+1] = tablero_minas[dimension-2][y+1]

    #PRIMERA COLUMNA
    if x > 0 and x < (dimension-1) and y == 0:

        tablero_actualizado[x][0] = tablero_minas[x][0]
        tablero_actualizado[x+1][0] = tablero_minas[x+1][0]
        tablero_actualizado[x-1][0] = tablero_minas[x-1][0]
        tablero_actualizado[x][1] = tablero_minas[x][1]
        tablero_actualizado[x+1][1] = tablero_minas[x+1][1]
        tablero_actualizado[x-1][1] = tablero_minas[x-1][1]

    #ÚLTIMA COLUMNA
    if x > 0 and x < (dimension-1) and y == dimension-1:

        tablero_actualizado[x][dimension-1] = tablero_minas[x][dimension-1]
        tablero_actualizado[x-1][dimension-1] = tablero_minas[x-1][dimension-1]
        tablero_actualizado[x+1][dimension-1] = tablero_minas[x+1][dimension-1]
        tablero_actualizado[x][dimension-2] = tablero_minas[x][dimension-2]
        tablero_actualizado[x+1][dimension-2] = tablero_minas[x+1][dimension-2]
        tablero_actualizado[x-1][dimension-2] = tablero_minas[x-1][dimension-2]

    return tablero_actualizado

#COMPROBAR ESTADO DE LA PARTIDA
def final(x, y, tablero_minas, tablero_actualizado, minas):
    
    fin = False
    if tablero_minas[x][y] == '**':
        print('TOCASTE UNA MINA, FIN DE LA PARTIDA')
        fin = True
    else:
        num_hastaghs = 0
        for i in range(0,dimension):
            for j in range(0,dimension):
                if tablero_actualizado[i][j] == '##':
                    num_hastaghs += 1

        if num_hastaghs <= 5:
            print('FELICIDADES: HAS GANADO')
            fin = True

        num_minas_reveladas = 0
        for i in range(0,dimension):
            for j in range(0,dimension):
                if tablero_actualizado[i][j] == '**':
                    num_minas_reveladas += 1
        
        if num_minas_reveladas == minas:
            print('FELICIDADES: HAS GANADO')
            fin = True

    return fin


if __name__ == "__main__":

    dimension, minas = leer_archivo()
    tablero, tablero_actualizado = crear_tableros(dimension)
    pintar_tablero(tablero, dimension)

    correcto = False
    while correcto == False:
        tablero_minas = colocar_minas(tablero, dimension, minas)
        correcto = comprobar_minas(tablero_minas, minas)

    fin = False
    while fin == False:

        x, y = coordenadas(dimension)
        tablero_actualizado = actualizar_tablero(tablero_minas, x, y)

        pintar_tablero(tablero_actualizado, dimension)
        print('\n')

        fin = final(x, y, tablero_minas, tablero_actualizado, minas)

