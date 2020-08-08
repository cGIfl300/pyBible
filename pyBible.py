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

from tkinter import *
from creer_bouton import creer_bouton
from image_set import image_set
from configuration import *
from peewee import *
from db_model import *
import pygame
from class_pyBible import pyBible_Global
from class_autobutton import creer_autobutton
from app_selecttranslation import SelectTranslation
from app_rechercher import AppRechercher
from app_bookmark import AppBookmark
from app_Iamreading import AppIamReading
import gettext
import codecs
import os

fr = gettext.translation("base", localedir=repertoire_script + "locales", languages=[langue_appli], fallback=False)
fr.install()
_ = fr.gettext
ngettext = fr.ngettext

pygame.init()


class pyBible(Tk):
    """ Interface graphique ...
    """

    def __init__(self, debug=False):
        Tk.__init__(self)
        self.debug = debug
        self.langue = "FRE"
        self.traduction = "French Louis Segond"
        self.magic_system = pyBible_Global()
        self.book = 1
        self.chapitre = 1

    def interface(self):
        """ Interface de la fenêtre
        """
        self.title(_("pyBible"))
        self.panel_menu = Canvas(self, bg=couleur_fond)
        self.panel_selection = Canvas(self, bg=couleur_fond)
        self.panel_contenu = Canvas(self, bg=couleur_fond)
        self.panel_menu_bas = Canvas(self, bg=couleur_fond)

        self.menu_marque_pages = creer_autobutton(self.panel_menu, texte=_("Marque\nPage"))
        self.menu_rechercher = creer_autobutton(self.panel_menu, texte=_("Rechercher"))

        self.menu_precedent = creer_autobutton(self.panel_menu_bas, texte="<")
        self.menu_suivant = creer_autobutton(self.panel_menu_bas, texte=">")

        nom_complet = f"{self.magic_system.traduction}\n{self.magic_system.bookname}"

        self.menu_selection = creer_autobutton(self.panel_selection, texte=nom_complet)

        self.SCROLL_001 = Scrollbar(self.panel_contenu, bg=couleur_fond, orient=VERTICAL)
        self.contenu = Text(self.panel_contenu, bg=couleur_fond, fg=couleur_texte, wrap=WORD, yscrollcommand=self.SCROLL_001.set)

        self.SCROLL_001.config(command=self.contenu.yview)
        self.contenu.config(state=DISABLED)

        """ Implantation des composants
        """
        self.panel_menu.pack(fill=BOTH, expand=True)
        self.panel_selection.pack(fill=BOTH, expand=True)
        self.panel_contenu.pack(fill=BOTH, expand=True)
        self.panel_menu_bas.pack(fill=BOTH, expand=True)
        self.SCROLL_001.pack(side=RIGHT, fill=Y)
        self.contenu.pack(fill=BOTH, expand=True)

        """ Binding
        """
        self.menu_suivant.btn.bind("<Button-1>", self.do_MenuSuivant)
        self.menu_precedent.btn.bind("<Button-1>", self.do_MenuPrecedent)
        self.menu_selection.btn.bind("<Button-1>", self.do_SelectionTraduction)
        self.menu_rechercher.btn.bind("<Button-1>", self.do_MenuRechercher)
        self.menu_marque_pages.btn.bind("<Button-1>", self.do_bookmark)

        self.restaurer_lecture()

    def do_bookmark(self, event):
        app = AppBookmark(master=self, chapitre=self.chapitre, book=self.book)
        app.run()

    def do_SelectionTraduction(self, event):
        """ Sélection d'une nouvelle traduction et / ou chapitre
        """
        app = SelectTranslation(self)
        app.run()

    def do_MenuRechercher(self, event):
        """ Recherche d'un mot ou d'une phrase
        """
        app = AppRechercher(langue=self.langue, traduction=self.traduction)
        app.run()

    def do_MenuSuivant(self, event):
        if self.chapitre < self.max_chapitre():
            self.chapitre += 1
        else:
            if self.book < 66:
                self.book += 1
                self.chapitre = 1
        self.nouveau_chapitre(self.book, self.chapitre)

    def do_MenuPrecedent(self, event):
        if self.chapitre > 1:
            self.chapitre -= 1
        else:
            if self.book > 1:
                self.book -= 1
                self.chapitre = self.max_chapitre()

        self.nouveau_chapitre(self.book, self.chapitre)

    def max_chapitre(self):
        total = 0
        l = Livres.get(
            Livres.ID_Bible == Bibles.get(Bibles.titre == self.traduction, Bibles.langue == self.langue),
            Livres.N_Livres == self.book,
        )
        v = Versets.select().where(
            Versets.ID_Bible == Bibles.get(Bibles.titre == self.traduction, Bibles.langue == self.langue), Versets.ID_Livre == l
        )
        ancien_chapitre = ""
        for liste in v:
            if ancien_chapitre != liste.N_Chapitre:
                total += 1
                ancien_chapitre = liste.N_Chapitre
        return total

    def restaurer_lecture(self):
        fichier = codecs.open(repertoire_script + "data/bookmarks.dat", "r", "utf-8")
        contenu = fichier.readlines()
        fichier.close()
        print(f"{repertoire_script}data/bookmarks.dat\n{contenu}")
        for l in contenu:
            l = l.replace("\n", "")
            l = l.split(",")
            if l[0] == "o":
                print(f"{l}\nRestauration : {l[1]} - {l[2]}")
                self.book = int(l[1])
                self.chapitre = int(l[2])
                self.nouveau_chapitre(self.book, self.chapitre)

    def nouveau_chapitre(self, book, chapitre):
        """ Affiche un chapitre
        """
        App = AppIamReading(book=book, chapitre=chapitre)
        App.run()
        self.contenu.config(state=NORMAL)
        self.contenu.delete("0.0", "end")
        temporaire = self.magic_system.chapitre_found(book=book, chapitre=chapitre)
        temporaire2 = ""
        for l in temporaire:
            temporaire2 = temporaire2 + f"{l[1]}:{l[2]} - {l[3]}\n"
        self.contenu.insert("0.0", temporaire2)
        self.contenu.config(state=DISABLED)
        nom_complet = f"{self.traduction}\n{self.magic_system.bookname.upper()}"
        self.menu_selection.btn.config(text=nom_complet)

    def run(self):
        self.interface()
        self.mainloop()


if __name__ == "__main__":
    App = pyBible(debug=True)
    App.run()
