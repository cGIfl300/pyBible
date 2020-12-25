# -*- coding:utf-8 -*-
#
# Copyright © 2020 cGIfl300
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the “Software”),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import xml.etree.ElementTree as ET

from peewee import *

from db_model import *


class acquiert_bible:
    """ Permet l'ajout d'une bible dans la base de donnée principale
    """

    def __init__(self, fichier_xml, debug=False):
        self.fichier_xml = fichier_xml
        self.debug = debug

    def run(self):
        self.enregistrer_bible()

    def enregistrer_bible(self):
        db_link = connexion_db()
        if self.debug:
            print("Conversion de {}".format(self.fichier_xml))
        arbre = ET.parse(self.fichier_xml)
        racine = arbre.getroot()
        livre_nbr = 0

        langue = racine.find("./INFORMATION/language").text
        langue = langue.upper()
        if self.debug:
            print("Langue: {}".format(langue))

        # Vérifier si la langue existe dans la base de données
        # Si elle n'existe pas, demander à l'utilisateur la langue en fonction de l'abréviation
        if Langues.get_or_none(Langues.langue == langue) == None:
            if self.debug:
                print("La langue n'existe pas!")
            record = Langues(langue=langue, description="")
            lignes = record.save()

        titre = racine.find("./INFORMATION/title").text
        if self.debug:
            print("Titre: {}".format(titre))

        # Vérifier si une Bible existe déjà avec ce titre dans cette langue.
        if Bibles.get_or_none(Bibles.langue == langue, Bibles.titre == titre) != None:
            # Oui: Ignorer cette bible
            if self.debug:
                print("La bible est déjà dans la base, on l'ignore.")
        else:
            # Non: Enregistrer cette nouvelle bible
            if self.debug:
                print("La bible n'est pas dans la base, ajoutons la!")

            description = racine.find("./INFORMATION/description").text

            if description == None:
                description = " "

            if self.debug:
                print("Description: {}".format(description))

            # Ajouter la Bible à la base de donnée
            record = Bibles(langue=langue, titre=titre, description=description)
            lignes = record.save()

            for livre in racine.findall("BIBLEBOOK"):
                livre_nbr = livre_nbr + 1
                chapitre_nbr = 0
                # Ajouter un nouveau numéro de livre
                record = Livres(
                    ID_Bible=Bibles.get(langue=langue, titre=titre, description=description),
                    N_Livres=livre_nbr,
                    Nom_Livre=" ",
                    Shortcut=" ",
                )
                lignes = record.save()

                Ref_Bibles = Bibles.get(langue=langue, titre=titre, description=description)
                Ref_Livres = Livres.get(ID_Bible=Ref_Bibles, N_Livres=livre_nbr)

                for chapitre in livre:
                    chapitre_nbr = chapitre_nbr + 1
                    verset_nbr = 0
                    for verset in chapitre:
                        verset_nbr = verset_nbr + 1
                        # ATTENTION: L'affichage de tous les versets ralenti considérablement
                        # le temps de traitement.
                        # if self.debug:
                        #    print('{} {} {}: {}'.format(livre_nbr, chapitre_nbr, verset_nbr, verset.text))
                        # Enregistrer les versets dans la base de données
                        if verset.text == None:
                            verset_text = "_"
                        else:
                            verset_text = verset.text

                        record = Versets(
                            ID_Livre=Ref_Livres,
                            ID_Bible=Ref_Bibles,
                            N_Chapitre=chapitre_nbr,
                            N_Verset=verset_nbr,
                            Texte=verset_text,
                        )
                        lignes = record.save()
