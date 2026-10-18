from espositore import Espositore
from stand import Stand,PreseAggiuntive,Premium
from operator import attrgetter
class LingottoFiere: #classe principale del programma
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome= nome
        self.__lista_espositori = [] #lista con all'interno tutti gli espositori, gestiti come oggetti
        self.__lista_stand = [] #lista con all'interno tutti gli stand, gestiti come oggetti

    def is_codice_in_lista(self,tipo,codice): #questo metodo controlla se il codice in input è presente nella lista corrispondente
        #tipo può essere o "E" (espositore) o "S" (stand)
        presente = False
        if tipo == "E":
            lista = self.lista_espositori
        else:
            lista = self.lista_stand

        for i in range(len(lista)):
            if lista[i].id == codice:
                presente = True

        return presente

    def stand_assegnato(self,id_espositore): #metodo per returnare lo stand assegnato a un dato espositore
        id_stand = ""
        for i in range(len(self.lista_espositori)):
            if self.lista_espositori[i].id == id_espositore:
                id_stand = self.lista_espositori[i].stand
        return id_stand

    def espositore_assegnato(self,id_stand): #metodo per returnare l'espositore assegnato a un dato stand
        id_espositore = ""
        for i in range(len(self.lista_stand)):
             if self.lista_stand[i].id == id_stand:
                 id_espositore = self.lista_stand[i].espositore
        return id_espositore




    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self): #possibilità di accedere all'attributo privato
        return self.__nome

    @nome.setter
    def nome(self, nome_nuovo): # mi dà la possibilità di modificare il valore dell'attributo nome
        self.__nome = nome_nuovo

    @property
    def lista_espositori(self): #possibilità di accedere all'attributo privato
        return self.__lista_espositori

    @lista_espositori.setter
    def lista_espositori(self, nuova_lista_espositori): # mi dà la possibilità di modificare il valore dell'attributo lista espositori
        self.__lista_espositori = nuova_lista_espositori

    @property
    def lista_stand(self): #possibilità di accedere all'attributo privato
        return self.__lista_stand

    @lista_stand.setter
    def lista_stand(self, nuova_lista_stand): # mi dà la possibilità di modificare il valore dell'attributo lista stand
        self.__lista_stand = nuova_lista_stand





    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        with open(file_path, 'r', encoding='utf-8') as infile:
            lista_espositori= [] #creo una lista in cui aggiungo tutti gli espositori
            lista_stand=[] #creo una lista in cui aggiungo tutti gli stand
            for line in infile:
                line= line.rstrip("\n")
                line= line.split(",")
                if len(line)== 3: # verifico che è un espositore
                    lista_espositori.append(Espositore(line[0],line[1],line[2])) #ho aggiunto l'oggetto espositore alla lista espositori
                else:
                    if len(line)== 4: # verifico che sia uno stand base
                        lista_stand.append(Stand(line[0],line[1],line[2],line[3])) #ho aggiunto l'oggetto stand base alla lista degli stand
                    elif line[4].isdigit(): #verifico che sia uno stand con delle prese aggiuntive
                        lista_stand.append(PreseAggiuntive(line[0], line[1], line[2], line[3],line[4]))#ho aggiunto l'oggetto con prese aggiuntive stand base alla lista degli stand
                    else:
                        lista_stand.append(Premium(line[0], line[1], line[2], line[3], line[4])) #ho aggiunto l'oggetto stand premium alla lista degli stand

            self.lista_espositori = lista_espositori # assegno la lista all'attributo della classe
            self.lista_stand = lista_stand # assegno la lista all'attributo della classe


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        if self.is_codice_in_lista("S",codice_stand) and self.is_codice_in_lista("E",codice_espositore) and self.stand_assegnato(codice_espositore) == "" and  self.espositore_assegnato(codice_stand) == "":
            #controllo se il codice dello stand richiesto è presente nella lista degli stand, lo stesso faccio per gli espositori
            #controllo che lo stand richiesto sia disponibile e che l'espositore non sia già stato assegnato
            for i in range(len(self.lista_espositori)): #ciclo sulla lista espositori per assegnare lo stand all'espositore
                if self.lista_espositori[i].id == codice_espositore:
                    self.lista_espositori[i].stand = codice_stand

            for j in range(len(self.lista_stand)): #ciclo sulla lista degli stand per assegnare l'espositore allo stand
                if self.lista_stand[j].id == codice_stand:

                    self.lista_stand[j].espositore = codice_espositore
        else:
            raise ValueError("Stand non assegnato a causa di un errore") #nel caso mi viene generato un False nell'if solleva un errore generico


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        for i in range(len(self.lista_espositori)):
            if self.lista_espositori[i].stand != "":
                print(f"{self.lista_espositori[i].id:8s} {self.lista_espositori[i].nome:10s} {self.lista_espositori[i].cognome:10s} {self.lista_espositori[i].stand:8s}") #stampa solo gli espositori assegnati
            else:
                print(
                    f"{self.lista_espositori[i].id:8s} {self.lista_espositori[i].nome:10s} {self.lista_espositori[i].cognome:10s} {"---"}") #stampa gli espositori senza stand assegnato
    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        self.lista_stand.sort(key= attrgetter("prezzo")) #lista ordinata per prezzo crescente
        return self.lista_stand #returno l'attributo della lista stand

