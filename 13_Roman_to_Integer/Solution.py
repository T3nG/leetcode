class Solution:
    @staticmethod
    def romanToInt(s):
        # I, V, X, L, C, D , M
        # s: str
        # return: int
        num = 0
        ten = 0
        hundred = 0
        thousand = 0

        if 'IV' in s:
            num = 4
            s = s.replace('IV', '')
        elif 'IX' in s:
            num = 9
            s = s.replace('IX', '')
        else:
            if 'V' in s:
                num = 5
                num += s.count('I') * 1
                s = s.replace('V', '')
                for i in range(s.count('I')):
                    s = s.replace('I', '')
            else:
                num = s.count('I') * 1
                for i in range(s.count('I')):
                    s = s.replace('I', '')

        if 'XL' in s:
            ten = 40
            s = s.replace('XL', '')
        elif 'XC' in s:
            ten = 90
            s = s.replace('XC', '')
        else:
            if 'L' in s:
                ten = 50
                ten += s.count('X') * 10
                s = s.replace('L', '')
                for i in range(s.count('X')):
                    s = s.replace('X', '')
            else:
                ten = s.count('X') * 10
                for i in range(s.count('X')):
                    s = s.replace('X', '')

        if 'CD' in s:
            hundred = 400
            s = s.replace('CD', '')
        elif 'CM' in s:
            hundred = 900
            s = s.replace('CM', '')
        else:
            if 'D' in s:
                hundred = 500
                hundred += s.count('C') * 100
                s = s.replace('D', '')
                for i in range(s.count('C')):
                    s = s.replace('C', '')
            else:
                hundred = s.count('C') * 100
                for i in range(s.count('C')):
                    s = s.replace('C', '')

        if 'M' in s:
            thousand = 1000
            thousand *= s.count('M')
        return num + ten + hundred + thousand
