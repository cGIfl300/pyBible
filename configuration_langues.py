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

from configuration import *
from peewee import *
from db_model import *
from tkinter import *
import gettext

fr = gettext.translation("base", localedir=repertoire_script + "locales", languages=[langue_appli], fallback=False)
fr.install()
_ = fr.gettext
ngettext = fr.ngettext


class Configuration_Langues(Toplevel):
    """ Interface graphique configuration des langues.
    Ce module permet de configurer les langues de pyBible.
    ENG = Anglais; FRA = Français... en fonction des Bibles présentes dans la base de donnée.
    """

    def __init__(self, debug=False):
        Toplevel.__init__(self)
        self.debug = debug

    def interface(self):
        """ Interface de la fenêtre
        """
        self.title(_("pyBible - Editeur de langues"))
        self.geometry("300x400")
        self.panel0 = Canvas(self, bg=couleur_fond)
        self.panel1 = Canvas(self, bg=couleur_fond)
        self.liste_langue()
        self.WDG_Langues = []
        self.SCROLL_LST = Scrollbar(self, orient=VERTICAL)
        self.LSTLangues = Listbox(
            self.panel0, selectmode=SINGLE, bg=couleur_fond_saisie, fg=couleur_texte_saisie, yscrollcommand=self.SCROLL_LST.set
        )
        self.SCROLL_LST.config(command=self.LSTLangues.yview)
        self.LBL_Langue = Label(self.panel1, bg=couleur_fond, fg=couleur_texte, text=_("Veuillez sélectionner une langue"))
        self.ENT_Description = Entry(self.panel1, bg=couleur_fond_saisie, fg=couleur_texte_saisie)
        self.BTN_Valider = Button(
            self.panel1, bg=couleur_fond_saisie, fg=couleur_texte_saisie, text=_("Modifier"), command=self.do_ModifierLangue
        )

        """
        Mise en place des callbacks
        """
        self.LSTLangues.bind("<<ListboxSelect>>", self.do_ListeSelect)
        self.do_feed_list()

        """ Implantation des composants.
        """
        self.panel1.pack(fill=BOTH, side=BOTTOM, expand=True)
        self.SCROLL_LST.pack(side=RIGHT, fill=Y)
        self.panel0.pack(fill=BOTH, expand=True)
        self.LSTLangues.pack(fill=BOTH, expand=True)
        self.LBL_Langue.pack(fill=X, expand=True)
        self.ENT_Description.pack(fill=X, expand=True)
        self.BTN_Valider.pack(fill=X, expand=True)

    def do_feed_list(self):
        VAR_row = 0

        for ligne in self.langue:
            self.LSTLangues.insert(VAR_row, ligne[0])
            VAR_row += 1

    def liste_langue(self):
        """ Retourne la liste des langues présentes dans la base de données.
        self.langue[0][0] = FRE; self.langue[0][1] = Français
        self.langue[1][0] = ENG; self.langue[1][1] = Anglais
        ...
        """
        self.langue = []

        for l in Langues.select():
            if self.debug:
                print(f"{l.langue} : {l.description}")
            self.langue.append([l.langue, l.description])

    def do_ListeSelect(self, event):
        # Losqu'une langue est sélectionnée dans la liste
        Code_Langue = self.LSTLangues.selection_get()

        for ligne in self.langue:
            if ligne[0] == Code_Langue:
                Description_Langue = ligne[1]
            pass

        self.LBL_Langue.config(text=_("Le code\n{}\nest attribué à la langue\n{}").format(Code_Langue, Description_Langue))
        self.ENT_Description.delete(0, END)
        self.ENT_Description.insert(0, Description_Langue)

    def do_ModifierLangue(self):
        """
        Modification de la description de langue
        """
        Code_Langue = self.LSTLangues.selection_get()
        Description_Langue = self.ENT_Description.get()
        q = Langues.update({Langues.description: Description_Langue}).where(Langues.langue == Code_Langue)
        q.execute()
        self.LBL_Langue.config(text=_("Le code\n{}\nest attribué à la langue\n{}").format(Code_Langue, Description_Langue))
        self.liste_langue()

    def run(self):
        self.interface()


if __name__ == "__main__":
    w = Tk()
    w.after(30000, w.destroy)
    w.wm_state("icon")
    App = Configuration_Langues(debug=True)
    App.run()
    w.mainloop()
