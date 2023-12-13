import aes



chars = '`~1!2@3#4$5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpP[{}]\\|aAsSdDfFgGhHjJkKlL;:\'"zZxXcCvVbBnNmM,<.>/? ' # Prevent invalid characters

def tothex(text: str):
    intarr = []
    for c in text:
        loc = chars.find(c)
        if loc == -1:
            return False
        intarr.append(loc)
    return {'hex':aes.utils.arr8bit2int(intarr), 'len':len(text)}

def fromthex(data):
    intarr = aes.utils.int2arr8bit(data['hex'], data['len'])
    text = ''
    for i in intarr:
        text += chars[i % 95]
    return text

def split_text(text, n=16):
    '''
    Splits the text every nth character
    source: https://stackoverflow.com/questions/9475241/split-string-every-nth-character
    '''
    return [text[i:i+n] for i in range(0, len(text), n)]

def encrypt(mk, data):
    cipher = aes.aes(tothex(mk)['hex'], 192)
    tct = []
    for t in split_text(data):
        thex = tothex(t)
        if not thex: return False # Pass on the invalid character error
        tct.append({'hex':aes.utils.arr8bit2int(cipher.enc_once(thex['hex'])), 'len':thex['len']})
    return tct

def decrypt(mk, tct):
    cipher = aes.aes(tothex(mk)['hex'], 192)
    text = ''
    for thex in tct:
        d_thex = {'hex':aes.utils.arr8bit2int(cipher.dec_once(thex['hex'])), 'len':thex['len']}
        t = fromthex(d_thex)
        text += t if isinstance(t, str) else ''
    return text



if __name__ == '__main__':
    key = 'passwordpasswordpassword'
    
    text = 'Hi Roger boy, how are you?'
    tct = encrypt(key, text)
    print(tct)


    print(decrypt('passwordpasswordpassword', tct))

    
