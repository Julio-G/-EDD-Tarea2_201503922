from graphviz import Source
def crearLista(N):
    global cont
    L = [ ]
    for i in range(N):
        L.append(cont)
        cont=cont+1
    return L
 
def CreaMatriz(N,M):
    Matriz = [ ]
    for i in range(N):
        Matriz.append(crearLista(M))
    for i in range(N):
        Fila = ""
        for j in range(M):
            Espacios = ' ' * (5-len(str(Matriz[i][j])))
            Fila = Fila + Espacios + str(Matriz[i][j])
        print (Fila)
    return Matriz

n1=0
n2=0
n3=0
if __name__ == '__main__':
    while(n1!=3):
   
        print(".: Menu :.");
        print("1) Mapeo por filas");
        print("2) Mapeo por columnas");
        print("3) Salir");
        n1=int(input("Ingrese el numero: "));
        if n1==1:
            cont=0
            print(".: Ingrese el tamaño del arreglo:.");
            n2 = int(input("Ingrese X: "));
            n3 = int(input("Ingrese Y: "));
            pot= CreaMatriz(n3,n2)
            print(".: Ingrese las posicion a linealizar:.");
            n4 = int(input("Ingrese X: "));
            n5 = int(input("Ingrese Y: "));
            print("Resultado= Posicion "+str(n5*n2+n4))

            temp="digraph G{\n"
            temp+="label=\"Matriz\";\n"
            temp+="node [shape=record, color=blue]\n"
            temp+="tabla [label=<\n"
            temp+="<table>\n"
            for y in range(n3):
                temp+="<tr>\n"
                for x in range(n2):

                    if(pot[y][x]!=n5*n2+n4):
                        temp+="\t<td bgcolor=\"blue\">"+str(pot[y][x])+"</td>\n"
                    else:
                        temp+="\t<td bgcolor=\"yellow\">"+str(pot[y][x])+"</td>\n"

                temp+="</tr>\n"
            temp+="</table> >,]; \n"
            cont2=0
            temp+="tabla2 [label=<\n"
            temp+="<table>\n"
            temp+="<tr>\n"
            for y in range(n3):
                for x in range(n2):
                    if(pot[y][x]!=n5*n2+n4):
                        temp+="\t<td bgcolor=\"blue\">("+str(cont2)+")"+str(pot[y][x])+"</td>\n"
                    else:
                        temp+="\t<td bgcolor=\"yellow\">("+str(cont2)+")"+str(pot[y][x])+"</td>\n"
                    cont2=cont2+1
            temp+="</tr>\n"
            temp+="</table> >,]; }"
            sp = Source(temp, filename="mapeo por filas", format="png")
            sp.view()

            
        elif n1==2:
            cont=0
            print(".: Ingrese el tamaño del arreglo:.");
            n2 = int(input("Ingrese X: "));
            n3 = int(input("Ingrese Y: "));
            pot= CreaMatriz(n3,n2)
            print(".: Ingrese las posicion a linealizar:.");
            n4 = int(input("Ingrese X: "));
            n5 = int(input("Ingrese Y: "));
            print("Resultado= Posicion "+str(n4*n3+n5))

            temp="digraph G{\n"
            temp+="label=\"Matriz\";\n"
            temp+="node [shape=record, color=blue]\n"
            temp+="tabla [label=<\n"
            temp+="<table>\n"
            for y in range(n3):
                temp+="<tr>\n"
                for x in range(n2):
                    if(pot[y][x]!=n5*n2+n4):
                        temp+="\t<td bgcolor=\"blue\">"+str(pot[y][x])+"</td>\n"
                    else:
                        temp+="\t<td bgcolor=\"yellow\">"+str(pot[y][x])+"</td>\n"
                temp+="</tr>\n"
            temp+="</table> >,];\n"

            cont2=0
            temp+="tabla2 [label=<\n"
            temp+="<table>\n"
            temp+="<tr>\n"
            for y in range(n2):
                for x in range(n3):
                    if(pot[x][y]!=n5*n2+n4):
                        temp+="\t<td bgcolor=\"blue\">("+str(cont2)+")"+str(pot[x][y])+"</td>\n"
                    else:
                        temp+="\t<td bgcolor=\"yellow\">("+str(cont2)+")"+str(pot[x][y])+"</td>\n"
                    cont2=cont2+1
            temp+="</tr>\n"
            temp+="</table> >,]; }"
            sp = Source(temp, filename="mapeo por columnas", format="png")
            sp.view()

        