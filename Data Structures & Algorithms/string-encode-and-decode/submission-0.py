class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string += f"{len(i)}#{i}"
        return string

    def decode(self, s: str) -> List[str]:
        lista = []
        length = ""
        switch = 0
        kalma = ""
        first = 1
        for i in s:
            if i == "#" and switch == 0:
                switch = int(length)
                length = ""
            else:
                if switch == 0:
                    length += i
                    if first == 1:
                        first = 0
                        continue
                    lista.append(kalma)
                    kalma = ""
                else:
                    kalma += i
                    switch -= 1
        lista.append(kalma)
        return lista