import random

# crea la matriz de n columnas

def new_game(n):
    i=0
    matrix = []
    return aux_new_game(n,i,matrix)

def aux_new_game(n,i,matrix):
    if (n==i):
        return matrix
    else:
        matrix.append([0] * n)
        i=i+1
    return aux_new_game(n,i,matrix)

#Agrega los dos si hay campos vacios
def add_two(mat):
    a = random.randint(0, len(mat)-1)
    b = random.randint(0, len(mat)-1)
    c = random.randint(0, 10)
    if(c==1):
        if(mat[a][b]==0):
            mat[a][b] = 4
            return mat
    if(mat[a][b]==0):
        mat[a][b] = 2
        return mat
    if(revisar_matriz(mat,0,0)):
        return add_two(mat)
    else:
        return mat

def revisar_matriz(mat,i,j):
    
    if(j==3):
        if(mat[i][j]==0):
            return True
        else:
            j=0
            return revisar_matriz(mat,i+1,j)
    if(i==3 and j==3):
        if(mat[i][j]==0):
            return True
        else:
            return False
    if(i<4 and j<4):
        if(mat[i][j]==0):
            return True
        else:
            return revisar_matriz(mat,i,j+1)

#estado del juego
def estado_juego(mat):
    i=0
    j=0
    k=0
    l=0
    return aux_estado(mat,i,j,k,l)

#i,j = 3,k =2,l=2
def aux_estado(mat,i,j,k,l):
    if(l==3):
        l=2
    if(i==3 and j==3):
        if (mat[i][j] == 0):
            return 'not over'
        else:
            return 'lose'
    if(j==3):
        j=0
        k=0
        return aux_estado(mat,i+1,j,k,l+1)
    
    if (mat[i][j] == 0):
        return 'not over'
    if (mat[i][j] == 2048):
        return 'win'
    if(k==2):
        return aux_estado(mat,i,j+1,k,l)
    if(l==2 and j==3):
        return aux_estado(mat,i+1,j,k,l)
    
    if (mat[l][k] == mat[l+1][k] or mat[l][k+1] == mat[l][k]):
        return 'not over'
    if (mat[len(mat)-1][k] == mat[len(mat)-1][k+1]):
            return 'not over'
    if (mat[l][len(mat)-1] == mat[l+1][len(mat)-1]):
            return 'not over'
    if(j==3 and k==2):
        j=0
        k=0
        
        return aux_estado(mat,i+1,j,k,l+1)
    else:
        return aux_estado(mat,i,j+1,k+1,l)

# SELECCIONA LA CELDA DE LA IZQUIERDA

def reversa(mat):
    new=[[],[],[],[]]
    i=0
    j=0
    return aux_rev(mat,i,j,new)

def aux_rev(mat,i,j,new):
    if(j==4):
        j=0
        return aux_rev(mat,i+1,j,new)
    if(i==3 and j==3):
        new[i].append(mat[i][len(mat[0])-j-1])
        return new
    else:
        new[i].append(mat[i][len(mat[0])-j-1])
        return aux_rev(mat,i,j+1,new)
        
# TRANSPUESTA

def transpuesta(mat):
    new=[[],[],[],[]]
    i=0
    j=0
    return aux_trans(mat,i,j,new)

def aux_trans(mat,i,j,new):
    if(j==4):
        j=0
        return aux_trans(mat,i+1,j,new)
    if(i==3 and j==3):
        new[i].append(mat[j][i])
        return new
    else:
        new[i].append(mat[j][i])
        return aux_trans(mat,i,j+1,new)
    
# Revisar si tiene ceros para mover hasta el final


def revisar(mat):
    new = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    i=0
    j=0
    count=0
    r=False
    return aux_revisar(mat,new,i,j ,count,r)

def aux_revisar(mat,new,i,j,count,r):
    if(j==4):
        j=0
        count=0
        
        return aux_revisar(mat,new,i+1,j,count,r)
    if(i==4):
        
        
        return (new, r)
    
    if(i==3 and j==3):
        if(mat[i][j] != 0):
            new[i][count] = mat[i][j]
            
            if (j != count):
                r=True
                
                return (new, r)
            return (new, r)
        
    if(mat[i][j] != 0):
        new[i][count] = mat[i][j]
        if (j != count):
            r=True
            return aux_revisar(mat,new,i,j+1,count+1,r)
        
        return aux_revisar(mat,new,i,j+1,count+1,r)
    
    else:
        return aux_revisar(mat,new,i,j+1,count,r)


#VERIFICA QUE LA CELDA DE LA DERECHA SEA INGUAL PARA PODER UNIR MULTIPLICAR POR 2 Y DEJAR LA OTRA EN CERO
punt=0
def op_der(mat):
    i=0
    j=0
    r=False
    res=0
    return aux_op_der(mat,i,j,r)

def aux_op_der(mat,i,j,r):
    global punt
    if(j==3):
        j=0
        return aux_op_der(mat,i+1,j,r)
    if(i==3 and j==2):
        if (mat[i][j] == mat[i][j+1] and mat[i][j] != 0):
            mat[i][j] *= 2
            mat[i][j+1] = 0
            punt=punt+mat[i][j]
            r=True
        return (mat,r,punt)
    if (mat[i][j] == mat[i][j+1] and mat[i][j] != 0):
            mat[i][j] *= 2
            mat[i][j+1] = 0
            r=True
            punt=punt+mat[i][j] 
            return aux_op_der(mat,i,j+1,r)
    else:
        return aux_op_der(mat,i,j+1,r)
    
#ARMA LA MATRIZ

def up(game):
    print("up")
    # return matrix after shifting up
    game = transpuesta(game)
    game, done = revisar(game)
    temp = op_der(game)
    game = temp[0]
    done = done or temp[1]
    game = revisar(game)[0]
    game = transpuesta(game)
    return (game, done)


def down(game):
    print("down")
    game = reversa(transpuesta(game))
    game, done = revisar(game)
    temp = op_der(game)
    game = temp[0]
    done = done or temp[1]
    game = revisar(game)[0]
    game = transpuesta(reversa(game))
    return (game, done)


def left(game):
    print("left")
    # return matrix after shifting left
    game, done = revisar(game)
    temp = op_der(game)
    game = temp[0]
    done = done or temp[1]
    game = revisar(game)[0]
    return (game, done)


def right(game):
    print("right")
    # return matrix after shifting right
    game = reversa(game)
    game, done = revisar(game)
    temp = op_der(game)
    game = temp[0]
    done = done or temp[1]
    game = revisar(game)[0]
    game = reversa(game)
    return (game, done)




def actualizar(game):
    puntos= op_der(game)
    puntos1= puntos[2]
    return puntos1

def fileW(com):
        com=str(com)
        newfile=open("puntaje final.txt","w")
        newfile.write(com)
        newfile.close()

def octal(x):
    if(x<8):
        return x
    return str(octal(x//8))+str((x%8))


def binario(x):
    if(x<2):
        return x
    return str(binario(x//2))+str((x%2))

def hexadecimal(x):
    if(x<10):
        return x
    if(x==10):
        return 'A'
    if(x==11):
        return 'B'
    if(x==12):
        return 'C'
    if(x==13):
        return 'D'
    if(x==14):
        return 'E'
    if(x==15):
        return 'F'
    
    return str(hexadecimal(x//16))+str(hexadecimal((x%16)))


