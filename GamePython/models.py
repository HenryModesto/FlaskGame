import random

class Carta:
    def __init__(self, simbolo):
        self._simbolo = simbolo
        self._virada = False

    @property
    def simbolo(self):
        return self._simbolo

    @property
    def virada(self):
        return self._virada

    @virada.setter
    def virada(self, valor):
        self._virada = valor

class JogoMemoria:
    def __init__(self):
        self._cartas = []
        self._pares_encontrados = 0
        self._cartas_selecionadas = []
        self.iniciar_jogo()

    def iniciar_jogo(self):
        simbolos = ['🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼']
        self._cartas = [Carta(simbolo) for simbolo in simbolos for _ in range(2)]
        random.shuffle(self._cartas)

    def selecionar_carta(self, indice):
        if len(self._cartas_selecionadas) < 2:
            carta = self._cartas[indice]
            if not carta.virada:
                carta.virada = True
                self._cartas_selecionadas.append(carta)

        if len(self._cartas_selecionadas) == 2:
            return self.verificar_par()

    def verificar_par(self):
        c1, c2 = self._cartas_selecionadas
        if c1.simbolo == c2.simbolo:
            self._pares_encontrados += 1
            self._cartas_selecionadas.clear()
            return True  
        else:
            return False  

    def desvirar_cartas(self):
        for carta in self._cartas_selecionadas:
            carta.virada = False
        self._cartas_selecionadas.clear()

    def jogo_completo(self):
        return self._pares_encontrados == len(self._cartas) // 2

    @property
    def cartas(self):
        return self._cartas
