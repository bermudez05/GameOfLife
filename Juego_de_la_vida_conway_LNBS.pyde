
# Juego de la vida - Version final (LNBS)
# some ideas where extract form 'Game of Life' By Joan Soler-Adillon (Processing3+ Java)

pause = False
copCells = []
cells = []
cellSize = 20

def setup():
    default = 15
    size(800, 400)
    stroke('#989674')
    background(0)
    strokeWeight(1)
    noSmooth()
    frameRate(4)
    
    for i in range(width/cellSize):
        columna = []
        for j in range(height/cellSize):
            if random(100) < default:                  # de manera aleatoria establecemos las celulas vivas y las muertas
                columna.append(1)
            else:
                columna.append(0)
        cells.append(columna)
        copCells.append (columna)

def draw():
    
    for i in range(width/cellSize):                     # dibujo de las condiciones iniciales de la matriz
        for j in range (height/cellSize):
            if cells[i][j] == 1:
                fill ('#BFD400')
            else:
                fill(0)
            rect(i*cellSize,j*cellSize,cellSize,cellSize)

    if pause == False:
        estados()
        
    if ((mousePressed == True) and (pause == True)):    # manipular la matriz con el mouse mientras el juego esta en pausa
        x_cell = int(map(mouseX, 0, width, 0, width/cellSize))  # (Game of Life By Joan Soler-Adillon (Processing3+ Java))
        x_cell = constrain(x_cell, 0, width/cellSize)
        y_cell = int(map(mouseY, 0, height, 0, height/cellSize))
        y_cell = constrain(y_cell, 0, height/cellSize)

        if (copCells[x_cell][y_cell] == 1):            
            cells[x_cell][y_cell] = 0 
            fill (30)
        else:
            cells[x_cell][y_cell] = 1
            fill ('#BFD400')
            
    elif ((pause == True) and (mousePressed == False)): # guarda cambios introducidos con el mouse
        for i in range(width/cellSize):                 # deep copy
            copCells[i] = list(cells[i])
    
def estados():
    
    for i in range(width/cellSize):                     # deep copy
        copCells[i] = list(cells[i])
        
            
    for i in range(width/cellSize):
        for j in range(height/cellSize):
            neighbours = 0 
            for m in range(i-1,i+2):                     # rango establecido para verificar vecinos en las columnas
                for n in range(j-1,j+2):                 # rango establecido para verificar vecinos en las filas
                    
                    if ((m>=0) and (m<(width/cellSize))):
                        if ((n>=0) and (n<(height/cellSize))):
                            if (i,j) != (m,n):           # verifica que no se cuente a si mismo 
                                if copCells[m][n] == 1:
                                    neighbours += 1      # PRIMER TEORIA: el problema se puede deber a la manera en la que recorremos las matriz dado que iniciamos desde 
            if copCells[i][j] == 1:                      # el origen y recorremos las filas de manera horizontal y no vertical, tecnicamente este si era un problema, sin embargo
                if (neighbours<2) or (neighbours>3):     # para algunas figuras no resulta (hipotesis: presiento que hay algo mal con la copia de las matrices)
                    cells[i][j] = 0                      # the copy i was making was a shallow copy so they'll be the same for any change i make to any of them.
            else:
                if neighbours == 3:
                    cells [i][j] = 1


def keyPressed():
    global pause
    
    if (key == 'p') or (key == 'P'):                     # pausa 
        pause = not(pause)
        
    if (key == 's') or (key == 'S'):                     # restablecer los valores de la matriz a 0
        for i in range(width/cellSize): 
           for j in range(height/cellSize):
                copCells[i][j] = 0
                cells[i][j] = 0
                
