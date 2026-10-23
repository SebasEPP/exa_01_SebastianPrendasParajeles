import time
from cls_Stack import cls_Stack
from Subrutinas import baraja, repartirCartas


class Jugador:
    def __init__(self, nombre):
        self._nombre = nombre
        self._partida = cls_Stack()

    @property
    def nombre(self):
        return self._nombre

    @property
    def partida(self):
        return self._partida


print()
print("Buscando a la Reina de Corazones")
print("=================================")

jugadores = [
    Jugador("Merlina"),
    Jugador("Pericles"),
    Jugador("Tio Lucas"),
    Jugador("Homero")
]

repartirCartas(jugadores)

ancho = 12
naipes_vistos = {j.nombre: [] for j in jugadores}
ganador = None

print()
print("".join(j.nombre.ljust(ancho) for j in jugadores))
print("-" * (ancho * len(jugadores)))

hay_naipes = True
while hay_naipes and ganador is None:
    hay_naipes = False
    fila = ""

    for jugador in jugadores:
        if not jugador.partida.isempty():
            hay_naipes = True
            naipe = jugador.partida.pop()
            naipes_vistos[jugador.nombre].append(naipe)
            fila += naipe.ljust(ancho)
            if naipe == "QC":
                ganador = jugador
        else:
            fila += "".ljust(ancho)

    print(fila)

    if ganador is not None:
        break

    time.sleep(2)

for jugador in jugadores:
    while not jugador.partida.isempty():
        jugador.partida.pop()

print()
if ganador is not None:
    print(f"¡{ganador.nombre} encontró la Reina de Corazones y ganó!")
    corazones = list(filter(lambda n: n.endswith("C"), naipes_vistos[ganador.nombre]))
    print(f"Naipes de Corazon de {ganador.nombre}: {corazones}")
else:
    print("El juego terminó sin ganador.")