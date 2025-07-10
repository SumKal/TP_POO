from operator import truediv

from clients import *
from chambre import *
from reservations import *
from datetime import date

class Hotel:
    def __init__(self,nom):
        self._nom=nom
        print(f"========BIENVENU A L'HOTEL {self._nom}====================")

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self,newNom):
        self._nom=newNom

    def verifierDate(self,dateDonne):
        if(date.strptime(dateDonne, "%d/%m/%Y")):
            return True
        else:
            return False
)

    def gestion(self):
        orientation = 1
        while True:
            choix=int(input("Entrez (1) pour les clients (2) pour les chambres et (3) pour la réservation et (0) pour quitter le programme: "))
            if (choix==1):
                #Gestion des clients de l'hotel
                while True:
                    desire=int(input("Entrez (1) pour enregistrer un client - (2) pour modifier un client - (3) pour afficher la liste des clients (0) pour revenir en arrière."))
                    if(desire==1):
                        nom=input("Entrez le nom du client: ")
                        prenom=input("Entrez le prénom du client: ")
                        telephone=input("Entrez le numéro de téléphone du client: ")
                        email=input("Entrez l'email du client: ")
                        client=Client(1,nom,prenom,telephone,email)
                        client.AfficheClient()
                        while True:
                            val=int(input("Entrer (1) pour valider et enregistrer les informations (2) pour modifier (3) pour revenir en arrière"))
                            if(val==1):
                                client.ajoutClient()

                            elif (val==2):
                                client.modifierRecementAjouter()

                            elif (val==3):
                                break
                    elif (desire==2):
                        Client().modificationInfoClient()
                    elif (desire==3):
                        Client().afficheListeClient()
                    elif (desire==0):
                        print("Retour")
                        break


            elif (choix==2):
                #Gestion des chambres de l'hôtel
                while True:
                    verification=int(input("Entrez [1] pour l'ajout d'une chambre - [2] pour modifier les informations d'une chambre - [3] pour supprimer une chambre - [4] Afficher la liste des chambres disponibles - [5] Pour quitter: "))
                    if(verification==1):
                        print("Vous saisissez les informations d'une nouvelle chambre")
                        numero=int(input("Numéro de la chambre: "))
                        type=input("Type de la chambre (Simple, Double, Suite): ")
                        capacite=input("Capacité de la chambre: ")
                        prixParNuit=input("Prix par nuit: ")
                        statut=input("Statut de la chambre: ")
                        while True:
                            interro=int(input(f"Entrez [1] pour enregistrer les informations saisies - [2] pour revenir en arrière: "))
                            if(interro==1):
                                chambre=Chambre(numero,type,capacite,prixParNuit,statut)
                                chambre.ajoutChambre()
                            elif(interro==2):
                                break

                    elif(verification==2):
                        Chambre().modificationInformationChambre()

                    elif(verification==3):
                        Chambre().suppressionChambre()

                    elif(verification==4):
                        print("Afficher la liste des chambres disponibles")

                    elif(verification==5):
                        break
            elif (choix==3):
                #Gestion des réservation
                """Gestion de la réservation"""
                while True:
                    print("\nEntrez [1] pour ajouter une réservation")
                    print("Entrez [2] pour modifier une réservation")
                    print("Entrez [3] pour supprimer une réservation")
                    print("Entrez [4] pour marquer un client comme arrivé")
                    print("Entrez [5] pour marquer un client comme parti")
                    print("Entrez [6] pour consulter les réservations")
                    print("Entrez [0] pour quitter\n")
                    question=int(input("REPONSE: "))
                    if(question==1):
                        dateArrivee=input("Entrez la date d'arrivée (JJ/MM/AAAA) : ")
                        dateDepart=input("Entrez la date de départ (JJ/MM/AAAA): ")
                        dateCreation=date.today()
                        statut=input("Entrez le statut de la réservation (Confirmée, Annulée, En cours): ")
                        montantTotal=int(input("Entrez le montant total: "))
                        idClient=int(input("Entrez l'ID du client: "))
                        numeroChambre=int(input("Entrez le numéro de la chambre: "))
                        reservation1=Reservation(0,dateArrivee,dateDepart,dateCreation,statut,montantTotal,idClient,numeroChambre)
                        reservation1.ajoutReservation()
                    elif(question==2):
                        print("Modifier la réservation")
            elif (choix==0):
                break




if __name__=="__main__":
    hot1=Hotel("LOLA")
    hot1.gestion()
