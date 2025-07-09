import json


clients=[]
class Client:
    def __init__(self,idClient=0,nom="", prenom="",telephone="",email=""):
        print("DEBUG: Création d'un client")
        self._idClient=idClient
        self._nom=nom
        self._prenom=prenom
        self._telephone=telephone
        self._email=email
        self.chargementJSON()

    def AfficheClient(self):
        print(f"Le client {self._nom} {self._prenom} Téléphone: {self.telephone} Email:{self._email} vient d'être créer avec l'ID: {self.getId()+1}")

    def chargementJSON(self):
        """Fonction du chargement du fichier client.json"""
        global clients
        try:
            with open('clients.json', 'r') as f:
                clients = json.load(f)
        except FileNotFoundError:
            clients = []

    @property
    def idClient(self):
        return self._idClient

    @idClient.setter
    def idClient(self,newId):
        self._idClient=newId

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, newNom):
        self._nom = newNom

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, newPrenom):
        self._prenom = newPrenom

    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, newTelephone):
        self._telephone = newTelephone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, newEmail):
        self._email = newEmail

    def getId(self):
        """Récupération du dernier id du client enregistré dans la base de données"""
        lastId = 0
        for i in clients:
            lastId = i["idClient"]

        return lastId

    def afficherClients(self):
        """Chargement des clients et affichage"""
        self.chargementJSON()
        print(clients)


    def saveClient(self,ell):
        """Enregistrement du fichier JSON dans la base de données"""

        with open('clients.json', 'w') as f:
            json.dump(ell, f)


    def ajoutClient(self):
        """Fonction d'ajour d'un client dans la base de donnée mais avant vérification des informations entreée"""
        # Incrémentation du dernier id récupéré
        self._idClient =  self.getId() + 1
        client = {'idClient': self._idClient, 'nom': self._nom, "prenom":self.prenom, 'telephone': self._telephone, 'email': self._email}
        clients.append(client)
        self.saveClient(clients)
        print("Le client enregistré avec succès !!!")


    def modifierRecementAjouter(self):
        """Fonction d'ajour du client récément ajouté dans la base de donnée mais avant vérification des informations entreée"""
        # Incrémentation du dernier id récupéré

        self._idClient =  self.getId() + 1
        while True:
            nom = input("Entrez le nom du client: ")
            if (nom != ""):
                self._nom=nom
                break

        while True:
            prenom = input("Entrez le prenom du client: ")
            if (prenom != ""):
                self._prenom=prenom
                break

        telephone = input("Entrez le numéro de téléphone du client: ")
        self._telephone=telephone
        email = input("Entrez l'email du client: ")
        self._email = email
        client = {'idClient': self._idClient, 'nom': self._nom, "prenom":self._prenom, 'telephone': self._telephone, 'email': self._email}
        clients.append(client)
        self.saveClient(clients)
        print("Le client enregistré avec succès !!!")

    def rechercheNom(self,nomClient=""):
        if (nomClient == ""):
            nomClient = input("Entrez le nom du client à rechercher: ")
        cli = []
        for sub in clients:
            if sub["nom"] == nomClient:
                cli.append(sub)
        return cli

    def modificationInfoClient(self,nomClient=""):
        """Modification de la quantité d'un produit après la falidation de son achat"""
        if(nomClient==""):
            nomClient=input("Entrez le nom du client: ")

        if(len(self.rechercheNom(nomClient))>0):
            cli = self.rechercheNom(nomClient)[0]
            self._nom = input("Entrer le nouveau nom: ")
            self._prenom = input("Entrer le nouvel prénom: ")
            self._telephone = input("Entrez le nouveau numéro: ")
            self._email = input("Entrez le nouvel email")
            position = clients.index(self.rechercheNom(nomClient)[0])
            clients.remove(self.rechercheNom(nomClient)[0])
            cli['nom'] = self._nom
            cli['prenom'] = self._prenom
            cli['telephone'] = self._telephone
            cli['email'] = self._email

            clients.insert(position, cli)
            self.saveClient(clients)
        else:
            print("Aucun client ne porte ce nom.")


    def afficheListeClient(self):
        for i in clients:

            print(f"ID: {i["idClient"]} \t NOM: {i["nom"]} \t PRENOM: {i['prenom']} \t TELEPHONE: {i["telephone"]} \t EMAIL: {i["email"]}")

