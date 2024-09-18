entrada = input()
X = float(entrada.split()[0])
Y = float(entrada.split()[1])
if(X==0 and Y==0):
    print("Origem")
elif(X > 0 and Y > 0):
    print("Q1")
elif(X==0 and Y!=0):
    print("Eixo Y")
elif(Y==0 and X!=0):
    print("Eixo X")
elif(X>0 and Y<0):
    print("Q4")
elif(X<0 and Y>0):
    print("Q2")
else:
    print("Q3")