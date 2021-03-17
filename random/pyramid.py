blocks = int(input("Ingrese numero de bloques: "))
height = 0
block = []

for i in range(blocks):
    block.append("*")

    while(len(block) < 20):
        print(block)
        height = i
        break

print(f"La altura de la piramide es: {height+1}")