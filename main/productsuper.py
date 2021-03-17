# EXERCISE 3.3

def product():
    "Dado cuatro numeros esta funcion devuelve el mayor producto de dos de ellos."
    "Gracias 'deque' podemos sacar el primer elemento en entrar, como una cola."
    from collections import deque

    #  Defino la cola 'numbers'.
    numbers = deque()

    # Creo una tupla para poner los valores y asignarle el producto como clave.
    final = {}
    
    # Itero en la cola e introduzco valores por teclado.
    print("Welcome, please indroducing four number.")
    for i in range(4):
        num = int(input(f"{i+1}. Please input a number: "))
        numbers.append(num)
    
    # De esta manera podemos mutar valores de la cola
    for i in list(numbers):
        for x in list(numbers):
            if (x != i):
                product = i * x
                
                # Uso mi tupla, le asigno como clave el producto y como valor un String
                final[product] = f"{i} * {x} = {product}"
        # Eliminamos por cada salto en i un elemento de la izquierda
        numbers.popleft()

    # Esto devuelve la clave con valor maximo de la tupla
    maximo = max(final)

    # Magic!
    for clave in final:
        if clave == maximo:
            print(final[clave])