"""
Zadanie

Dane jest słowo składające się z małych liter alfabetu angielskiego. Słowo to tniermy na co najmniej dwa kawałki, tak aby każdy kawałek zawierał co najmniej jedną samogłoskę. Proszę napisać program, który zwraca liczbę sposobów pocięcia słowa na kawałki. Można założyć, że słowie są co najmniej 2 samogłoski.

Wejście
Pierwszy i jedyny wiersz zawiera ciąg małych liter o długości 3 ≤ N ≤ 100.

Wyjście
W pierwszym i jedynym wierszu standardowego wyjścia program powinien wypisać liczbę możliwych podziałów.

Przykład
Dla danych wejściowych:
ocena

Poprawna odpowiedzią jest:
8

Możliwe podziały to: o-cena, o-ce-na, o-cen-a, oc-ena, oc-e-na, ocen-a, oce-na, ocen-a
"""
from typing import List, Set


class Slowo_1:
    samogloski = {'a', 'ą', 'e', 'ę', 'u', 'i', 'o', 'y'}

    def __init__(self, word: str):
        self.word = word.lower()
        self._check_samogloska()
        self._find_samogloski()

    @property
    def possibilites(self) -> Set[str]:
        return {}

    @property
    def number_of_divisions(self) -> int:
        return 0

    def _check_samogloska(self):
        if not self._has_samogloska(self.word):
            raise ValueError(f"'{self.word}' nie ma samoglosek.")

    def _has_samogloska(self, word_to_check):
        set_of_letters = {litera for litera in word_to_check}
        return bool(set_of_letters.intersection(self.samogloski))

    def _find_samogloski(self):
        self.indexes = []

        for i, letter in enumerate(self.word):
            if letter in self.samogloski:
                self.indexes.append(i)


        print(self.indexes)
        print('------------')

        for i in self.indexes:
            if i < len(self.word) - 1:
                print(i, self.word[:i+1], self.word[i+1:])
            if i > 1:
                print(i, self.word[:i], self.word[i:])

    # def _split_word(self) -> List[str]:
    #     # print('_split_word', self.word)
    #     self.divided_word = []
    #     self.counter = 0
    #
    #     for litera in self.word:
    #
    #         if litera in self.samogloski:
    #             self._append_item(litera)
    #             self.counter += 1
    #         else:
    #             self._append_item(litera)
    #
    #     if self._has_samogloska(self.divided_word[-1]):
    #         print('has samogloska')
    #     else:
    #         last_item = self.divided_word.pop(-1)
    #         # print(last_item)
    #         self.divided_word[-1] += last_item
    #     print('divided: ', self.divided_word)
    #     return [self.word]
