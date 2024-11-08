import random

# Classe base Carta
class Carta:
    def __init__(self, simbolo):
        self._simbolo = simbolo
        self._virada = False

    # Métodos acessores
    @property
    def simbolo(self):
        return self._simbolo

    @property
    def virada(self):
        return self._virada

    @virada.setter
    def virada(self, valor):
        self._virada = valor

    def __str__(self):
        return self.simbolo if self.virada else "?"


# Classe com Polimorfismo
class CartaVirada(Carta):
    def __init__(self, simbolo):
        super().__init__(simbolo) 
        self.virada = True 

    def __str__(self):
        return self.simbolo 


# Classe Herança
class CartaNormal(Carta):
    pass


# Classe base Jogo
class Jogo:
    def __init__(self):
        self._cartas = []  
        self._pares_encontrados = 0  
        self._cartas_selecionadas = []  

    def iniciar_jogo(self):
        raise NotImplementedError("Método 'iniciar_jogo' precisa ser implementado")

    def selecionar_carta(self, indice):
        raise NotImplementedError("Método 'selecionar_carta' precisa ser implementado")

    def verificar_par(self):
        raise NotImplementedError("Método 'verificar_par' precisa ser implementado")


    def desvirar_cartas(self):
        for carta in self._cartas_selecionadas:
            carta.virada = False  
        self._cartas_selecionadas.clear()  

    def jogo_completo(self):
        return self._pares_encontrados == len(self._cartas) // 2

    @property
    def cartas(self):
        return self._cartas


# Classe com Herança
class JogoMemoria(Jogo):
    def __init__(self):
        super().__init__()  
        self.iniciar_jogo()  

    def iniciar_jogo(self):
        simbolos = ['🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼']
        self._cartas = [CartaNormal(simbolo) for simbolo in simbolos for _ in range(2)]
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

