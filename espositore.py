class Espositore:
    def __init__(self,id_espositore,nome_espositore, cognome_espositore):
        self.__id_espositore= id_espositore
        self.__nome_espositore= nome_espositore
        self.__cognome_espositore= cognome_espositore
        self.__stand = ""

    @property
    def id(self):
        return self.__id_espositore

    @property
    def nome(self):
        return self.__nome_espositore

    @property
    def cognome(self):
        return self.__cognome_espositore

    @property
    def stand(self):
        return self.__stand

    @stand.setter
    def stand(self,nuovo_stand):
        self.__stand = nuovo_stand



    def __str__(self):
        return f"{self.__id_espositore} {self.__nome_espositore} {self.__cognome_espositore}"

