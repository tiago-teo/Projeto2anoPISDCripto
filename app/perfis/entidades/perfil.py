class Perfil:
    def __init__(self, nome, foto, curriculo):
        self.__nome = nome
        self.foto = foto
        self.curriculo = curriculo

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    @property
    def foto(self):
        return self.__foto
    @foto.setter
    def foto(self, foto):
        self.__foto = foto


    @property
    def curriculo(self):
        return self.__curriculo
    @curriculo.setter
    def curriculo(self, curriculo):
        self.__curriculo = curriculo