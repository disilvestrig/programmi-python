print("Benvenuto al risolutore di sistemi a 2 o 3 equazioni")
a = int(input("Cosa vuoi risolvere?"+
    " 1) Sistemi a 2 equazioni "+
    "2) Sistemi a 3 equazioni"+
    " >>> "))
var = []
coef = []
tnoto = []
if a == 1:
    for i in range(2):
        c = i + 1
        c = str(c)
        var.append(input("Inserisci nome "+c+"° variabile >>> "))
    for i in range(4):
        if i == 0:
            coef.append(int(input("Inserisci coefficiente della variabile "+var[0]+" nella prima equazione >>> ")))
        elif i == 1:
            coef.append(int(input("Inserisci coefficiente della variabile "+var[1]+" nella prima equazione >>> ")))
        elif i == 2:
            coef.append(int(input("Inserisci coefficiente della variabile "+var[0]+" nella seconda equazione >>> ")))
        elif i == 3:
            coef.append(int(input("Inserisci coefficiente della variabile "+var[1]+" nella seconda equazione >>> ")))
    for i in range(2):
        b = i + 1
        b = str(b)
        tnoto.append(int(input("Inserisci termine noto della "+b+"° equazione")))
    det1 = (coef[0]*coef[3])-(coef[1]*coef[2])
    detx = (tnoto[0]*coef[3])-(tnoto[1]*coef[1])
    dety = (tnoto[0]*coef[0])-(tnoto[1]*coef[2])
    x = detx / det1
    y = dety / det1
    print(var[0],"=",x)
    print(var[1],"=",y)
elif a == 2:
    for i in range(3):
        c = i+1
        c = str(c)
        var.append(input("Inserisci nome "+c+"° variabile >>> "))
    for i in range(9):
        if i == 0:
            coef.append(int(input("Inserisci coefficiente della variabile "+var[0]+" nella prima equazione >>> ")))
        elif i == 1:
            coef.append(int(input("Inserisci coefficiente della variabile "+var[1]+" nella prima equazione >>> ")))
        elif i == 2:
            coef.append(int(input("Inserisci coefficiente della variabile "+var[2]+" nella prima equazione >>> ")))
        elif i == 3:
            coef.append(int(input("Inserisci coefficiente della variabile "+var[0]+" nella seconda equazione >>> ")))
        elif i == 4:
            coef.append(int(input("Inserisci coefficiente della variabile "+var[1]+" nella seconda equazione >>> ")))
        elif i == 5:
            coef.append(int(input("Inserisci coefficiente della variabile "+var[2]+" nella seconda equazione >>> ")))
        elif i == 6:
            coef.append(int(input("Inserisci coefficiente della variabile "+var[0]+" nella terza equazione >>> ")))
        elif i == 7:
            coef.append(int(input("Inserisci coefficiente della variabile "+var[1]+" nella terza equazione >>> ")))
        elif i == 8:
            coef.append(int(input("Inserisci coefficiente della variabile "+var[2]+" nella terza equazione >>> ")))
    for i in range(3):
        b = i+1
        b = str(b)
        tnoto.append(int(input("Inserisci termine noto della "+b+"° equazione >>> ")))
    det1 = (coef[0]*coef[4]*coef[8])+(coef[1]*coef[5]*coef[6])+(coef[2]*coef[3]*coef[7])-(coef[2]*coef[4]*coef[6])-(coef[1]*coef[3]*coef[8])-(coef[0]*coef[5]*coef[7])
    detx = (tnoto[0]*coef[4]*coef[8])+(coef[1]*coef[5]*tnoto[2])+(coef[2]*tnoto[1]*coef[7])-(coef[2]*coef[4]*tnoto[2])-(coef[1]*tnoto[1]*coef[8])-(tnoto[0]*coef[5]*coef[7])
    dety = (coef[0]*tnoto[1]*coef[8])+(tnoto[0]*coef[5]*coef[6])+(coef[2]*coef[3]*tnoto[2])-(coef[2]*tnoto[1]*coef[6])-(tnoto[0]*coef[3]*coef[8])-(coef[0]*coef[5]*tnoto[2])
    detz = (coef[0]*coef[4]*tnoto[2])+(coef[1]*tnoto[1]*coef[6])+(tnoto[0]*coef[3]*coef[7])-(tnoto[0]*coef[4]*coef[6])-(coef[1]*coef[3]*tnoto[2])-(coef[0]*tnoto[1]*coef[7])
    x = detx/det1
    y = dety/det1
    z = detz/det1
    print(var[0],"=",x)
    print(var[1],"=",y)
    print(var[2],"=",z)
