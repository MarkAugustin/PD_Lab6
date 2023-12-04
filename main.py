if __name__ == '__main__':
    import eel
    import os
    import aes128
    import rsa
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import dsa
    from cryptography.exceptions import InvalidSignature

    (pubkey, privkey) = rsa.newkeys(512)
    private_key = dsa.generate_private_key(1024)
    public_key = private_key.public_key()
    global crypted_part
    @eel.expose
    def AES(message, key, way):
        if way == "1":
            os.remove('dec_AES.txt')
            input_path = os.path.abspath('dec_AES.txt')
            with open(input_path, 'xb') as ff:
                ff.write(bytes(message.encode('utf-8')))
            with open(input_path, 'rb') as f:
                data = f.read()
            crypted_data = []
            temp = []
            for byte in data:
                temp.append(byte)
                if len(temp) == 16:
                    crypted_part = aes128.encrypt(temp, key)
                    crypted_data.extend(crypted_part)
                    del temp[:]
            else:
                if 0 < len(temp) < 16:
                    empty_spaces = 16 - len(temp)
                    for i in range(empty_spaces - 1):
                        temp.append(0)
                    temp.append(1)
                    crypted_part = aes128.encrypt(temp, key)
                    crypted_data.extend(crypted_part)
            os.remove('cr_AES.txt')
            out_path = os.path.join(os.path.dirname(input_path) , 'cr_AES.txt')

            with open(out_path, 'xb') as ff:
                ff.write(bytes(crypted_data))
            with open(out_path, 'rb') as fff:
                f_data = fff.read()
            f_data=f_data.hex()
            return f_data
        if way == "2":
            os.remove('cr_AES.txt')
            input_path = os.path.abspath('cr_AES.txt')
            with open(input_path, 'x') as ff:
                ff.write(message)
            with open(input_path, 'r') as f:
                data = f.read()
            data = bytes.fromhex(data)
            decrypted_data = []
            temp = []
            for byte in data:
                temp.append(byte)
                if len(temp) == 16:
                    decrypted_part = aes128.decrypt(temp, key)
                    decrypted_data.extend(decrypted_part)
                    del temp[:] 
            else:
                if 0 < len(temp) < 16:
                    empty_spaces = 16 - len(temp)
                    for i in range(empty_spaces - 1):
                        temp.append(0)
                    temp.append(1)
                    crypted_part = aes128.encrypt(temp, key)
                    decrypted_data.extend(crypted_part) 
            os.remove('dec_AES.txt')
            out_path = os.path.join(os.path.dirname(input_path) , 'dec_AES.txt')

            with open(out_path, 'xb') as ff:
                ff.write(bytes(decrypted_data))
            with open(out_path, 'r') as fff:
                f_data = fff.read()
            return f_data[:-1]
    @eel.expose
    def key_gen():
        (pubkey, privkey) = rsa.newkeys(512)
        res = str(pubkey) + "\n" + str(privkey)
        return res;
    @eel.expose
    def RSA(message,key,way):
        if way == "1":
            enc_message = message.encode('utf-8')
            crypto = rsa.encrypt(enc_message,pubkey)
            return str(crypto.hex())
        if way == "2":
            dec_message = bytes.fromhex(message)
            crypto = rsa.decrypt(dec_message, privkey)
            return str(crypto.decode('utf-8'))
    @eel.expose
    def SIGN(message):
        global original_text 
        message = message.encode('utf-8')
        original_text = message
        signature = private_key.sign(message, hashes.SHA256())
        return "Подпись: " + signature.hex()
    @eel.expose
    def VER(message):
        verification = bytes.fromhex(message)
        try:
            public_key.verify(verification, original_text, hashes.SHA256())
            return "Цифровая подпись верна"  
        except:
            return "Цифровая подпись неверна"
eel.init("web")
eel.start("main.html", size=(900,900))