# Calcolo di Integrali di Funzioni Polinomiali

Questo progetto in Python permette di calcolare l'integrale di una funzione polinomiale definita dall'utente su un intervallo specificato. Viene fornita una stima dell'integrale utilizzando sia il **metodo dei rettangoli** che il **metodo dei trapezi**. Inoltre, il programma genera un grafico della funzione sull'intervallo scelto.

## Funzionalità

- Calcolo dell'integrale definito di una funzione polinomiale su un intervallo `[a, b]`.
- Scelta della funzione polinomiale tramite input dell'utente.
- Stima dell'integrale con il **metodo dei rettangoli** e il **metodo dei trapezi**.
- Visualizzazione grafica della funzione.

## Requisiti

- Python 3.x
- Librerie:
  - `matplotlib` per la generazione del grafico
  - `numpy` per la gestione di intervalli e calcoli

Puoi installare le librerie richieste eseguendo:  

```text pip install matplotlib numpy```  

## Utilizzo

1. **Avvio del programma**: Esegui il file `.py` nel tuo ambiente Python.
2. **Inserimento della funzione**: Quando richiesto, inserisci la funzione polinomiale in termini di `x`. Ad esempio:
   
   ```text
   Inserisci la funzione in termini di x (es. 'x**4 + 3*x**3 + 10*x + 1'):

3. **Definizione dell'intervallo**: Inserisci i valori di a e b per definire l'intervallo [a, b] su cui calcolare l'integrale.
4. **Risultati** : Il programma calcola e visualizza i risultati dell'integrale stimato con entrambi i metodi.
5. **Visualizzazione grafica**: Un grafico della funzione sull'intervallo selezionato viene mostrato in una finestra separata.

## Esempio di Esecuzione
Ecco un esempio di input e output: 
```text
Inserisci la funzione in termini di x (es. 'x**4 + 3*x**3 + 10*x + 1'): x**4 + 3*x**3 + 10*x + 1
Intervallo [a;b] a =  0
Intervallo [a;b] b =  5

Il valore di Sn è 4070.83335
Il valore di Sn1 è 4070.83334
Il valore di Tn (valore integrale con metodo trapezi) è 4070.83334
```
## Grafico della Funzione
Il programma genera un grafico della funzione sull'intervallo specificato dall'utente, con l'etichetta f(x) = [funzione] per indicare la funzione scelta.

## Note
Il programma usa un numero elevato di suddivisioni (100.000) per migliorare la precisione del calcolo. Per modificare questa precisione, cambia il valore della variabile d nella sezione principale del codice.
