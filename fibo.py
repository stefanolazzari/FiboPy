def fibonacci(n):
    """
    Genera la sequenza di Fibonacci fino al n-esimo termine.
    :param n: Numero di termini da generare
    :return: Lista contenente i primi n termini della sequenza di Fibonacci
    """
    if n <= 0:
        return []  # Nessun termine se n è minore o uguale a 0
    elif n == 1:
        return [0]  # Il primo termine è 0
    elif n == 2:
        return [0, 1]  # I primi due termini sono 0 e 1

    # Genera la sequenza per n > 2
    sequenza = [0, 1]
    for i in range(2, n):
        successivo = sequenza[i - 1] + sequenza[i - 2]
        sequenza.append(successivo)

    return sequenza

# Input dall'utente
num_termini = int(input("Quanti termini della sequenza di Fibonacci vuoi generare? "))

# Chiamata della funzione e output
if num_termini > 0:
    risultato = fibonacci(num_termini)
    print(f"La sequenza di Fibonacci con {num_termini} termini è:\n{risultato}")
else:
    print("Inserisci un numero positivo.")
