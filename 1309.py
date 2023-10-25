class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ''

        length = len(s)

        i = 0

        while length > i:
            if i < length - 2 and s[i+2] == '#':
                ans += self.getJtoZ(s[i:i+3])
                i += 3
            else:
                c = s[i]
                match c:
                    case '1':
                        ans += 'a'
                    case '2':
                        ans += 'b'
                    case '3':
                        ans += 'c'
                    case '4':
                        ans += 'd'
                    case '5':
                        ans += 'e'
                    case '6':
                        ans += 'f'
                    case '7':
                        ans += 'g'
                    case '8':
                        ans += 'h'
                    case '9':
                        ans += 'i'
                i += 1
        return ans

    def getJtoZ(self, s: str) -> str:
        match s:
            case '10#':
                return 'j'
            case '11#':
                return 'k'
            case '12#':
                return 'l'
            case '13#':
                return 'm'
            case '14#':
                return 'n'
            case '15#':
                return 'o'
            case '16#':
                return 'p'
            case '17#':
                return 'q'
            case '18#':
                return 'r'
            case '19#':
                return 's'
            case '20#':
                return 't'
            case '21#':
                return 'u'
            case '22#':
                return 'v'
            case '23#':
                return 'w'
            case '24#':
                return 'x'
            case '25#':
                return 'y'
            case '26#':
                return 'z'
