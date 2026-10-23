from cls_Stack import cls_Stack

def revisar_expresion(expresion: str)-> bool:
    pila = cls_Stack()
    if not pila.isempty():
        print("La pila debe estar vacia antes de usar")
        return False

    inicio = "({["
    final  = ")}]"
    pares  = {")": "(", "}": "{", "]": "["}

    for char in expresion:
        if char in inicio:
            if pila.isfull():
                while not pila.isempty():
                    pila.pop()
                return False
            pila.push(char)
        elif char in final:
            if pila.isempty():
                return False
            tope = pila.pop()
            if tope != pares[char]:
                while not pila.isempty():
                    pila.pop()
                return False
    resultado = pila.isempty()
    while not pila.isempty():
        pila.pop()

    return resultado
print()
expresion = input("Ingrese la expresion: ")
print("=======================")
if revisar_expresion(expresion):
    print(f"La expresion '{expresion}' esta bien escrita")
else:
    print(f"La expresion '{expresion}' esta mal escrita")
