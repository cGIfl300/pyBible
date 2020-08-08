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
from peewee import *
from db_model import *
from configuration import *
from class_autobutton import creer_autobutton
from image_set import image_set
from class_pyBible import pyBible_Global
import codecs
import os
import gettext

fr = gettext.translation("base", localedir=repertoire_script + "locales", languages=[langue_appli], fallback=False)
fr.install()
_ = fr.gettext
ngettext = fr.ngettext


class AppBookmark(Toplevel):
    """ Interface graphique ...
    """

    def __init__(self, master, debug=False, langue="FRE", traduction="French Louis Segond", book=1, chapitre=1):
        Toplevel.__init__(self)
        self.debug = debug
        self.langue = langue
        self.traduction = traduction
        self.book = book
        self.chapitre = chapitre
        self.master = master
        self.bookmarks = []
        self.moteur = pyBible_Global(langue=self.langue, traduction=self.traduction)

    def interface(self):
        """ Interface de la fenêtre
        """
        self.title(_("Marque Pages"))

        self.panel_menu = Canvas(self, bg=couleur_fond)
        self.panel_contenu = Canvas(self, bg=couleur_fond)

        self.menu_delete = creer_autobutton(self.panel_menu, texte=_("Supprimer"))
        self.menu_go = creer_autobutton(self.panel_menu, texte=_("Aller"))

        self.SCROLL_001 = Scrollbar(self.panel_contenu, bg=couleur_fond, orient=VERTICAL)
        self.LSTBookmarks = Listbox(
            self.panel_contenu,
            selectmode=SINGLE,
            bg=couleur_fond_saisie,
            fg=couleur_texte_saisie,
            yscrollcommand=self.SCROLL_001.set,
        )
        """ Implantation des composants
        """
        self.SCROLL_001.config(command=self.LSTBookmarks.yview)

        """ Binding
        """
        self.panel_menu.pack(fill=BOTH, expand=True)
        self.panel_contenu.pack(fill=BOTH, expand=True)
        self.decoration = image_set(self.panel_contenu, image_locale="images/vertical_spacer")
        self.LSTBookmarks.pack(fill=BOTH, expand=True, side=LEFT)
        self.SCROLL_001.pack(side=RIGHT, fill=Y)

        self.menu_go.btn.bind("<Button-1>", self.do_MenuGo)
        self.menu_delete.btn.bind("<Button-1>", self.do_MenuDelete)

        self.bookmarks_refresh()
        self.bookmark()
        self.bookmarks_refresh()

    def do_MenuDelete(self, event):
        """ Suppression d'un bookmark
        """
        try:
            selection = self.LSTBookmarks.curselection()
            livre = int(self.bookmarks[selection[0] + 1][1])
            chapitre = int(self.bookmarks[selection[0] + 1][2])
            if self.debug:
                print(f"Livre: {livre} Chapitre: {chapitre}")
        except:
            return 0
        fichier = codecs.open(repertoire_script + "data/bookmarks.dat", "w", "utf-8")

        for l in self.bookmarks:
            if l[0] == "o":
                fichier.write(f"o,{l[1]},{l[2]}\n")

            if l[0] == "s":
                if not ((int(l[1]) is livre) and (int(l[2]) is chapitre)):
                    if self.debug:
                        print(f"Livre: {livre} is {l[1]} | Chapitre: {chapitre} is {l[2]}")
                    fichier.write(f"s,{l[1]},{l[2]}\n")

        fichier.close()

        self.bookmarks_refresh()

    def do_MenuGo(self, event):
        try:
            selection = self.LSTBookmarks.curselection()
            livre = self.bookmarks[selection[0] + 1][1]
            chapitre = self.bookmarks[selection[0] + 1][2]
            self.master.nouveau_chapitre(livre, chapitre)
        except:
            pass

    def bookmark(self):
        """ Bookmarks a chapiter
        emplacement:
        data/bookmarks.dat
        format:
        o,1,1
        
        Le premier caractère correspond au type de bookmark:
        o origin: c'est le bookmark qui est récupéré au lancement de l'application
        s second: c'est un bookmark classique
        """
        livre = self.book
        chapitre = self.chapitre
        for l in self.bookmarks:
            if l[0] == "s":
                if (int(l[1]) == livre) and (int(l[2]) == chapitre):
                    return 0
        # Si le chapitre n'est pas encore dans les bookmarks, l'ajouter.
        fichier = codecs.open(repertoire_script + "data/bookmarks.dat", "a", "utf-8")
        fichier.write(f"s,{livre},{chapitre}\n")
        fichier.close()

    def bookmarks_refresh(self):
        """ Rafraîchir la liste des bookmarks
        """
        self.bookmarks = []
        self.LSTBookmarks.delete("0", "end")
        fichier = codecs.open(repertoire_script + "data/bookmarks.dat", "r", "utf-8")
        contenu = fichier.readlines()
        fichier.close()
        for l in contenu:
            l = l.replace("\n", "")
            self.bookmarks.append(l.split(","))
            l = l.split(",")
            if l[0] == "s":
                nom_livre = self.moteur.chapitre_found(l[1], l[2])
                nom_livre = self.moteur.bookname.upper()
                self.LSTBookmarks.insert(END, f"{nom_livre} {l[1]}:{l[2]}")

    def run(self):
        self.interface()


if __name__ == "__main__":
    w = Tk()
    w.after(30000, w.destroy)
    w.wm_state("icon")
    App = AppBookmark(w)
    App.run()
    w.mainloop()
