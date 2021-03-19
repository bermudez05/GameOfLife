
lastTime = 0
pause = False
copCells = []
cells = []
cellSize = 10

def setup():
    default = 10
    size(400, 200)
    stroke('#989674')
    background(0)
    strokeWeight(1)
    noSmooth()
        
    for i in range(height/cellSize):
        fila = []
        for j in range(width/cellSize):
            if random(0,100) < default:
                fila.append(1)
            else:
                fila.append(0)
        cells.append(fila)
        copCells.append(fila)

def draw():
    global lastTime
    for i in range(height/cellSize):
        for j in range (width/cellSize):
            if cells[i][j] == 1:
                fill('#FCF408')
            else:
                fill(0)
            rect(j*cellSize,i*cellSize,cellSize,cellSize)
    if ((millis()-lastTime)>100) and (pause==False):
        estados()
        lastTime = millis()
            
def estados():
    for i in range(height/cellSize):  # (deep copy) != (copCells=list(cells))
        for j in range(width/cellSize):
            copCells[i][j] = cells[i][j]
    for i in range(height/cellSize):
        for j in range(width/cellSize):
            neighbours = 0 
            for m in range(i-1,i+2): # como la funcion rango de phyton no incluye el ultimo numero del rango debes sumarse 2
                for n in range(j-1,j+2):
                    if ((m>=0) and (m<(height/cellSize)-1)):
                        if ((n>=0) and (n<(width/cellSize)-1)):
                            if (i,j) != (m,n):  # verifica que no se cuente a si mismo 
                                if copCells[m][n] == 1:
                                    neighbours += 1
            if copCells[i][j] == 1:
                if (neighbours<2) or (neighbours>3):
                    cells[i][j] = 0
            elif copCells[i][j] == 0:
                if neighbours == 3:
                    cells [i][j] = 1

def keyPressed():
    global pause
    if (key == 'p') or (key == 'P'):
        pause = not(pause)
