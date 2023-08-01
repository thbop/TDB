import aes


class Encryption:
    def __init__(self, master_key: str):
        self.chars = '`~1!2@3#4$5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpP[{}]\\|aAsSdDfFgGhHjJkKlL;:\'"zZxXcCvVbBnNmM,<.>/? ' # safe guard

        self.mk = self.tothex(master_key)['hex']
        self.cipher = aes.aes(self.mk, 192)

    def tothex(self, text: str):
        intarr = []
        for c in text:
            intarr.append(self.chars.find(c))
        return {'hex':aes.utils.arr8bit2int(intarr), 'len':len(text)}

    def fromthex(self, data):
        intarr = aes.utils.int2arr8bit(int(data['hex'], 16), data['len'])
        text = ''
        for i in intarr:
            text += self.chars[i]
        return text


if __name__ == '__main__':
    key = 'passwordpasswordpassword'
    enc = Encryption(key)