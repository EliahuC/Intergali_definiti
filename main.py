import matplotlib.pyplot as plt
import numpy as np

#programma per calcolare l'integrale di una funzione in un intervallo scelto (F puo essere una qualunque funzione polinomiale, basta cambiare la funzione del def funz)


#funzione che mi da il valore della funzione F in un punto x
def funz(x, expr):
    return eval(expr)


# main
# richiesta della funzione all'utente
expr = input(
    "Inserisci la funzione in termini di x (es. 'x**4 + 3*x**3 + 10*x + 1'): ")

#creazione dell'intervallo dall'utente
v = 0
while (v == 0):
    a = int(input("intervallo [a;b] a =  "))
    b = int(input("intervallo [a;b] b =  "))
    #controllo parametri
    if a < b:
        v = 1
    else:
        v = 0
        print("i valori non sono validi")
#creazione parametri che mi servono (100000 per correggere l'errode di metodo)
#Sn e Sn1 parametri del metodo rettangoli, Tn del metodo trapezi
d = (b - a) / 100000
Sn1 = funz(a, expr)
Tn = Sn1
Sn = 0
#calcolo integrali fino a b non compreso
while (a < b):
    a = a + d
    c = funz(a, expr)
    Sn1 = Sn1 + c
    Tn = Tn + 2 * c
    Sn = Sn + c
#calcolo integrale con b
c = funz(b, expr)
Tn = Tn + 2 * c
Sn = Sn + c
#moltiplico per la costante d
Sn1 = Sn1 * d
Sn = Sn * d
Tn = Tn * (d / 2)
#stampa risultati
print("il valore di Sn è ", Sn)
print("il valore di Sn1 è ", Sn1)
print("il valore di Tn (valore integrale con metodo trapezi) è ", Tn)

#disegno grafico
xlist = np.linspace(-10, 10, num=1000)
plt.xlabel("asse x ")
plt.ylabel("asse y")
plt.plot(xlist, funz(xlist, expr))
plt.show()
