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
from typing import List


class Slowo_1:


    def __init__(self, word: str):
        self.word = word

    @property
    def possibilites(self) -> str:
        return ''

    @property
    def number_of_divisions(self) -> int:
        return 0

    def _spit_word(self) -> List[str]:
        self.word

