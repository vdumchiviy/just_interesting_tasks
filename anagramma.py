
from collections import defaultdict
from typing import DefaultDict


class YandexTest():
    def is_anagramma(self, a: str, b: str) -> bool:
        bb = list(b)

        for x in a:
            try:
                bb.remove(x)
            except:
                return False

        return not bool(bb)

    def from_string_to_dic(self, s: str) -> dict:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        return d

    def is_anagramma_yandex(self, a: str, b: str) -> bool:
        return self.from_string_to_dic(a) == self.from_string_to_dic(b)


yandex_test = YandexTest()

a = "ереван"
b = "венера"
print(yandex_test.is_anagramma(a, b))
print(yandex_test.is_anagramma_yandex(a, b))
