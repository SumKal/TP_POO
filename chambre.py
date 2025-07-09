import json
chambres=[]

class Chambre:
    def __init__(self,numeroChambre=0,type="",capacite="",prixParNuit="",statut=""):
        self._numeroChambre=numeroChambre
        self._type=type
        self._capacite=capacite
        self._prixParNuit=prixParNuit
        self._statut=statut
        self.chargementJSON()

    @property
    def numeroChambre(self):
        return self._numeroChambre

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self,newType):
        self._type=newType

    @property
    def capacite(self):
        return self._capacite

    @capacite.setter
    def capacite(self,newCapacite):
        self._capacite=newCapacite

    @property
    def prixParNuit(self):
        return self._prixParNuit

    @prixParNuit.setter
    def prixParNuit(self,newPrix):
        self._prixParNuit=newPrix

    @property
    def statut(self):
        return self._statut

    @statut.setter
    def statut(self,newStatut):
        self._statut=newStatut


    def chargementJSON(self):
        """Fonction du chargement du fichier client.json"""
        global chambres
        try:
            with open('chambre.json', 'r') as f:
                chambres = json.load(f)
        except FileNotFoundError:
            chambres = []

    def getId(self):
        """Récupération du dernier id du client enregistré dans la base de données"""
        lastId = 0
        for i in chambres:
            lastId = i["numeroChambre"]

        return lastId


    def saveChambre(self,ell):
        """Enregistrement du fichier JSON dans la base de données"""
      
        with open('chambre.json', 'w') as f:
            json.dump(ell, f)


    def ajoutChambre(self):
        """Fonction d'ajour d'un client dans la base de donnée mais avant vérification des informations entreée"""
        # Incrémentation du dernier id récupéré
        self._numeroChambre =  self.getId() + 1
        chambre = {'numeroChambre': self._numeroChambre, 'type': self._type, "capacite":self._capacite, 'prixParNuit': self._prixParNuit, 'statut': self._statut}
        chambres.append(chambre)
        self.saveChambre(chambres)
        print("La chambre enregistré avec succès !!!")


    def rechercherChambre(self,numeroChambre=""):
        if (numeroChambre == ""):
            numeroChambre = int(input("Entrez le numéro de la chambre à rechercher: "))
        cli = []
        for sub in chambres:
            if sub["numeroChambre"] == numeroChambre:
                cli.append(sub)
        return cli

    def suppressionChambre(self):
        numeroChambre = int(input("Entrer le numéro de la chambre à supprimer: "))
        prod = []
        for sub in chambres:
            if sub["numeroChambre"] != numeroChambre:
                prod.append(sub)
        self.saveChambre(prod)

    def modificationInformationChambre(self, numeroChambre=""):
        """Modification de la quantité d'un produit après la falidation de son achat"""
        if (numeroChambre == ""):
            numeroChambre = int(input("Entrez le numéro de la chambre: "))

        if (len(self.rechercherChambre(numeroChambre)) > 0):
            cli = self.rechercherChambre(numeroChambre)[0]
            self._numeroChambre = int(input("Entrer le nouveau numéro de la chambre : "))
            self._type = input("Entrer le nouvel type pour la chambre (Simple, Double, Suite): ")
            self._capacite = input("Entrez la nouvelle capacité pour la chambre : ")
            self._prixParNuit = input("Entrez le nouveau prix par nuit pour la chambre: ")
            self._statut=input('Entrez le nouveau statut pour la chambre (Disponible, Occupée, En maintenance): ')
            position = chambres.index(self.rechercherChambre(numeroChambre)[0])
            chambres.remove(self.rechercherChambre(numeroChambre)[0])
            cli['numeroChambre'] = self._numeroChambre
            cli['type'] = self._type
            cli['capacite'] = self._capacite
            cli['prixParNuit'] = self._prixParNuit
            cli["statut"]=self._statut

            chambres.insert(position, cli)
            self.saveChambre(chambres)
        else:
            print("Aucune chambre ne porte ce numéro.")