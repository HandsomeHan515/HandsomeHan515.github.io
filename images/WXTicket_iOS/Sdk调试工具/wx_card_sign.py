import hashlib

class WxCardSign(object):
    def __init__(self):
        self.__data = []

    def add_data(self, data):
        self.__data.append(str(data))

    def get_signature(self):
        self.__data.sort()
        str_to_sign = ''.join(self.__data)
        print 'str_to_sign: ', str_to_sign
        return hashlib.sha1(str_to_sign).hexdigest()



if __name__ == '__main__':
    signer = WxCardSign()
    signer.add_data(456456)
    signer.add_data(1231231)
    signer.add_data("aaaaa")
    signer.add_data("xxxx")
    print signer.get_signature()
