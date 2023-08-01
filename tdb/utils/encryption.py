import aes


class Encryption:
    def __init__(self, master_key: str):
        self.chars = '`~1!2@3#4$5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpP[{}]\\|aAsSdDfFgGhHjJkKlL;:\'"zZxXcCvVbBnNmM,<.>/? ' # Prevent invalid characters

        self.mk = self.tothex(master_key)['hex']
        self.cipher = aes.aes(self.mk, 192)

    def tothex(self, text: str):
        intarr = []
        for c in text:
            loc = self.chars.find(c)
            if loc == -1:
                return False
            intarr.append(loc)
        return {'hex':aes.utils.arr8bit2int(intarr), 'len':len(text)}

    def fromthex(self, data):
        intarr = aes.utils.int2arr8bit(data['hex'], data['len'])
        text = ''
        for i in intarr:
            text += self.chars[i]
        return text
    
    def enc(self, thex):
        return {'hex':aes.utils.arr8bit2int(self.cipher.enc_once(thex['hex'])), 'len':thex['len']}
    
    def dec(self, thex):
        return {'hex':aes.utils.arr8bit2int(self.cipher.dec_once(thex['hex'])), 'len':thex['len']}
    
    def split_text(self, text, n=16):
        '''
        Splits the text every nth character
        source: https://stackoverflow.com/questions/9475241/split-string-every-nth-character
        '''
        return [text[i:i+n] for i in range(0, len(text), n)]
    
    def q_enc(self, text):
        tct = []
        for t in self.split_text(text):
            thex = self.tothex(t)
            if not thex: return False # Pass on the invalid character error
            tct.append(self.enc(thex))
        return tct
    
    def q_dec(self, tct):
        text = ''
        for thex in tct:
            d_thex = self.dec(thex)
            text += self.fromthex(d_thex)
        return text


if __name__ == '__main__':
    key = 'passwordpasswordpassword'
    enc = Encryption(key)
    json_user = '{"name":"Thbop","auth":"475132571695214935672513"}'
    e_data = enc.q_enc(json_user)
    print(e_data)
    d_data = enc.q_dec(e_data)
    print(d_data)
    
