"""Création d'une classe utilisateurs """
import re
import string

from tinydb import TinyDB,where
import pathlib


class User:
    #Création d'un attribut pour la base de données
    DB = TinyDB(pathlib.Path(__file__).resolve().parent / "user_data.json", indent=4)
    def __init__(self, first_name:str, last_name:str, phone_number:str="", address:str=""):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    def __str__(self):
        return f"{self.full_name}\n{self.phone_number}\n{self.address}"

    #On crée une propriété pour mettre à jour instantanément le prenom et le nom de l'user
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # On définie une properties qui permet de retourner un utilisateur s'il exist dans la base
    #Suppression d'un user
    def delete_user(self, prenom, nom) :
        """
            Supprimer un utilisateur en passant par son prenom et nom
        Args:
            prenom (): prénom de la personne
            nom (): Nom de la personne
        """
        name = User.DB.get((where("first_name") == prenom) & (where("last_name") == nom))
        if name != None:
            User.DB.remove(doc_ids=[name.doc_id])
            print(f"{prenom} {nom} supprimé de la base !")
        else:
            print("Le nom entrée n'existe pas ")
    #Création d'une méthode pour représenter la classe à l'exterieur
    def __repr__(self):
        return f"{self.first_name} {self.last_name}" #retourne le nom et le prenom seulement
    #Vérification de noms valide
    def _chek_user_name(self):
        caractere_interdit = string.digits+string.punctuation
        for caracteur in caractere_interdit:
            if caracteur in self.full_name:
                raise ValueError(f" {self.full_name} invalide !")
    #Création d'une méthode pour des numéros téléphone valide
    def _check_phone_number(self):
        cararctere_interdit = string.punctuation
        for character in cararctere_interdit:
            if character in self.phone_number:
                self.phone_number = self.phone_number.replace(character,"")
                raise ValueError(f"{self.phone_number} invalide !")
    #On créer ici un autre méthode qui va vérifier les deux autres methodes _chek en même temp
    def _cheks(self):
        #On appel les deux autres fonctions de vérification
        self._chek_user_name()
        self._chek_user_name()
    #Définition d'une méthode pour sauvegarder les données utilisateur dans un base de données
    def data_save(self, validate:bool=False) -> int:
        """
        Sauvegarde les données dans un fichier json
        Args:
            movie (): les données à sauvegarder
            validate (): une variable permettant d'appler la fonction _cheks() chargée de valider
            les données dans la base, par defaut il est à False, si on veut la validation de données
            avant l'insertion, il faudra penser à le marquer en True, lors de l'appell de la fonction
        """
        if validate: #Si on veut verifier que les données entré sont valide
            self._cheks() #On appel la fonction _cheks() qui est chargée de faire la vérif
            return User.DB.insert(self.__dict__) #la variable __dict__ représente le nom de variable et son contenue

'''On definie une fonction pour recuérer tout les instances d'une base de données'''
def get_all_users():
    """
        On recupére tout le contenue de la base, en utilisant le double astérisque
        le double astérique permet de recupérer un key et sa value en même temps
    """
    return [User(**user) for user in User.DB.all()]



if __name__ == "__main__":
    import  faker
    fake = faker.Faker()


    user = User(fake.first_name(), fake.last_name(), fake.phone_number(), fake.address())
    print("-" * 50)
    print(user.data_save(validate=True)) #On Verifie en même temps la validité du  numéro et le  avant de l'insérer dans la base

    #Suppression de données utilisateur
    prenom_a_supprimer = input("Taper votre nom afin de supprimer vos données de la base !")
    nom_a_supprimer  = input("Le prenom")

    user.delete_user(prenom_a_supprimer, nom_a_supprimer) #On supprime la personne ici


#On appel la fonction get_all_users()
print(get_all_users())