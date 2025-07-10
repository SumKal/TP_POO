from clients import *
from chambre import *
from datetime import date

reservations=[]

class Reservation:
    def __init__(self,idReservation="",dateArrivee="",dateDepart="",dateCreation="",statut="",montantTotal="",idClient="",numeroChambre=""):
        self._idReservation=idReservation
        self._dateArrivee=dateArrivee
        self._dateDepart=dateDepart
        self._dateCreation=dateCreation
        self._statut=statut
        self._montantTotal=montantTotal
        self._idClient=idClient
        self._numeroChambre=numeroChambre
        self.chargementJSON()

    @property
    def idRservation(self):
        return self._idReservation

    @idRservation.setter
    def idRservation(self,newIdRervation):
        self._idReservation=newIdRervation

    @property
    def dateArrivee(self):
        return self._dateArrivee

    @dateArrivee.setter
    def dateArrivee(self,newDateArrivee):
        self._dateArrivee=newDateArrivee

    @property
    def dateDepart(self):
        return self._dateDepart

    @dateDepart.setter
    def dateDepart(self,newDateDepart):
        self._dateDepart=newDateDepart

    @property
    def dateCreation(self):
        return self._dateCreation

    @dateCreation.setter
    def dateCreation(self,newDateCreation):
        self._dateCreation=newDateCreation

    @property
    def statut(self):
        return self._statut

    @statut.setter
    def statut(self,newStatut):
        self._statut=newStatut


    @property
    def montantTotal(self):
        return self._montantTotal

    @montantTotal.setter
    def montantTotal(self,newMontantTotal):
        self._montantTotal=newMontantTotal

    @property
    def idClient(self):
        return self._idClient

    @idClient.setter
    def idClient(self,newIdClient):
        self._idClient=newIdClient

    @property
    def numeroChambre(self):
        return self._numeroChambre

    @numeroChambre.setter
    def numeroChambre(self,newNumeroChambre):
        self._numeroChambre=newNumeroChambre


    def chargementJSON(self):
        """Fonction du chargement du fichier client.json"""
        global reservations
        try:
            with open('reservation.json', 'r') as f:
                reservations = json.load(f)
        except FileNotFoundError:
            reservations = []

    def getId(self):
        """Récupération du dernier id du client enregistré dans la base de données"""
        lastId = 0
        for i in chambres:
            lastId = i["idReservation"]

        return lastId

    def saveReservation(self, ell):
        """Enregistrement du fichier JSON dans la base de données"""

        with open('reservation.json', 'w') as f:
            json.dump(ell, f)

    def ajoutReservation(self):
        """Fonction d'ajour d'un client dans la base de donnée mais avant vérification des informations entreée"""
        # Incrémentation du dernier id récupéré
        self._dateArrivee = input("Entrez la date d'arrivée (JJ/MM/AAAA) : ")
        self._dateDepart = input("Entrez la date de départ (JJ/MM/AAAA): ")
        self._dateCreation = date.today()
        self._statut = input("Entrez le statut de la réservation (Confirmée, Annulée, En cours): ")
        self._montantTotal = int(input("Entrez le montant total: "))

        self._idClient = int(input("Entrez l'ID du client: "))
        while (self.verificationClient(self._idClient)==False):
            print("Client introuvable !!!")
            self._idClient = int(input("Entrez l'ID du client: "))

        self._numeroChambre = int(input("Entrez le numéro de la chambre: "))
        while (self.verificationChambre(self._numeroChambre)==False):

            self._numeroChambre = int(input("Entrez le numéro d'une chambre valide: "))

        #Changement du statut de la chambre
        Chambre().modificationDisponibliteChambre(self._numeroChambre)

        self._idReservation = self.getId() + 1
        reservation = {'idReservation': self._idReservation, 'dateArrivee': self._dateArrivee, "dateDepart": self._dateDepart,
                   'dateCreation': str(self._dateCreation), 'statut': self._statut, "montantTotal":self._montantTotal, "idClient":self._idClient,"numeroChambre":self._numeroChambre}

        reservations.append(reservation)
        self.saveReservation(reservations)
        print("\nLa réservation a été faite avec succès !!!")


    def verificationClient(self,idClient):
        valeur=Client().rechercheById(idClient)
        if (len(valeur)==0):
            return False
        else:
            return True

    def verificationChambre(self,idChambre):
        valeur=Chambre().rechercherChambre(idChambre)

        if (len(valeur)==0):
            print("La chambre n'existe pas")
            return False
        else:
            if(Chambre().verificationDisponibiliteChambre(idChambre)==False):
                print("La chambre non disponible")
                return False
            else:
                return True