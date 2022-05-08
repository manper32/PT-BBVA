import pandas as pd
import collections

class englishDeck():
    def __init__(self):
        self.deck = self.deck()[0]

    def deck(self):
        """
        Método para creación de baraja inglesa
        """
        numbers = list(map(lambda x: str(x),range(1,11)))+['J', 'Q', 'K']
        cards = [(i, i, i, i) for i in numbers]
        return (pd.DataFrame(cards, columns=['C', 'T', 'P', 'D']), numbers)

    def combination(self):
        """
        Método para crear todas las posibles combinaciones
        """
        comb = [(c, t, p, d) for c in self.deck['C'] for t in self.deck['T'] for p in self.deck['P'] for d in self.deck['D']]
        return comb

    def permutation(self, id):
        """
        Método para buscar las posibles permutaciones para una tupla especifica
        Parametros de entrada
        id: id de la tupla a comparar
        """
        perm = [i for i in self.combination() if collections.Counter(self.combination()[id]) == collections.Counter(i)]
        perm = [''.join(i) for i in perm]
        return tuple([i for i in min(perm)])


if __name__ == '__main__':
    print(englishDeck().combination())
    # print(englishDeck().permutation(5))
