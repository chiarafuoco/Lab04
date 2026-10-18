class Stand:
    def __init__(self,id_stand,superficie,padiglione,prezzo_base):
        self.__id_stand = id_stand
        self.__superficie =superficie
        self.__padiglione = padiglione
        self.__prezzo_base = int(prezzo_base)
        self.__prezzo= int(prezzo_base)
        self.__espositore = ""

    @property
    def id(self):
        return self.__id_stand

    @property
    def superficie(self):
        return self.__superficie

    @property
    def padiglione(self):
        return self.__padiglione

    @property
    def prezzo_base(self):
        return self.__prezzo_base

    @property
    def espositore(self):
        return self.__espositore

    @espositore.setter
    def espositore(self, nuovo_espositore):
        self.__espositore = nuovo_espositore

    @property
    def prezzo(self):
        return self.__prezzo

    @prezzo.setter
    def prezzo(self, nuovo_prezzo):
        self.__prezzo= nuovo_prezzo

    def __str__(self):
        return f"{self.__id_stand:8s} {self.__superficie:8s} {self.__padiglione:8s} {self.__prezzo_base:8.0f} {self.__prezzo:8.0f}"

class PreseAggiuntive(Stand): #classe da cui deriva
    def __init__(self, id_stand, superficie, padiglione, prezzo_base,numero_prese):
        super().__init__(id_stand, superficie, padiglione, prezzo_base)
        self.__numero_prese= int(numero_prese)
        self.prezzo= int(prezzo_base) * (1+ 0.07 * int(numero_prese))


    @property
    def numero_prese(self):
        return self.__numero_prese

    def __str__(self):
        return f"{super().__str__()} {self.__numero_prese:12d}"

class Premium(Stand): #classe da cui deriva
    def __init__(self, id_stand, superficie, padiglione, prezzo_base,tipologia):
        super().__init__(id_stand, superficie, padiglione, prezzo_base)
        self.__tipologia= tipologia
        self.prezzo= int(prezzo_base) * 1.30

    @property
    def tipologia(self):
        return self.__tipologia

    def __str__(self):
        return f"{super().__str__()} {self.__tipologia:12s}"

