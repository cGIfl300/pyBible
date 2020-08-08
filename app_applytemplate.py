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
import time
import codecs
import os
import gettext

fr = gettext.translation("base", localedir=repertoire_script + "locales", languages=[langue_appli], fallback=False)
fr.install()
_ = fr.gettext
ngettext = fr.ngettext

pygame.init()


class AppApplyTemplate(Toplevel):
    """ Applique un modèle de nomage de livres à une Bible
    """

    def __init__(self, debug=False):
        Toplevel.__init__(self)
        self.debug = debug

    def interface(self):
        """ Interface de la fenêtre
        """
        self.title(_("Appliquer Modèle"))

        self.panel0 = Canvas(self, bg=couleur_fond)
        self.panel1 = Canvas(self, bg=couleur_fond)

        self.panel_langue = Canvas(self.panel0, bg=couleur_fond)
        self.panel_traduction = Canvas(self.panel0, bg=couleur_fond)
        self.panel_livres = Canvas(self.panel0, bg=couleur_fond)

        self.panel_menu = Canvas(self.panel1, bg=couleur_fond)
        self.panel_templates = Canvas(self.panel1, bg=couleur_fond)

        self.SCROLL_001 = Scrollbar(self.panel_langue, orient=VERTICAL)
        self.SCROLL_002 = Scrollbar(self.panel_traduction, orient=VERTICAL)
        self.SCROLL_003 = Scrollbar(self.panel_livres, orient=VERTICAL)

        self.SCROLL_004 = Scrollbar(self.panel_templates, orient=VERTICAL)

        self.LSTLangues = Listbox(
            self.panel_langue,
            selectmode=SINGLE,
            bg=couleur_fond_saisie,
            fg=couleur_texte_saisie,
            yscrollcommand=self.SCROLL_001.set,
        )
        self.LSTTraductions = Listbox(
            self.panel_traduction,
            selectmode=SINGLE,
            bg=couleur_fond_saisie,
            fg=couleur_texte_saisie,
            yscrollcommand=self.SCROLL_002.set,
        )
        self.LSTLivres = Listbox(
            self.panel_livres,
            selectmode=SINGLE,
            bg=couleur_fond_saisie,
            fg=couleur_texte_saisie,
            yscrollcommand=self.SCROLL_003.set,
        )

        self.LSTTemplates = Listbox(
            self.panel_templates,
            selectmode=SINGLE,
            bg=couleur_fond_saisie,
            fg=couleur_texte_saisie,
            yscrollcommand=self.SCROLL_004.set,
        )

        self.SCROLL_001.config(command=self.LSTLangues.yview)
        self.SCROLL_002.config(command=self.LSTTraductions.yview)
        self.SCROLL_003.config(command=self.LSTLivres.yview)
        self.SCROLL_004.config(command=self.LSTTemplates.yview)

        """ Implantation des composants
        """

        self.menu_annuler = creer_bouton(self.panel_menu, image_locale="images/menu_annuler", cote=TOP)
        self.menu_valider = creer_bouton(self.panel_menu, image_locale="images/menu_enregistrer", cote=TOP)

        self.panel0.pack(fill=BOTH, expand=True)
        self.panel1.pack(fill=BOTH, expand=True)
        self.panel_langue.pack(fill=BOTH, expand=True, side=LEFT)
        self.panel_traduction.pack(fill=BOTH, expand=True, side=LEFT)
        self.panel_livres.pack(fill=BOTH, expand=True, side=LEFT)
        self.panel_templates.pack(fill=BOTH, expand=True, side=LEFT)
        self.panel_menu.pack(fill=BOTH, expand=True, side=RIGHT)
        self.LSTLangues.pack(fill=BOTH, expand=True, side=LEFT)
        self.LSTTraductions.pack(fill=BOTH, expand=True, side=LEFT)
        self.LSTLivres.pack(fill=BOTH, expand=True, side=LEFT)
        self.LSTTemplates.pack(fill=BOTH, expand=True, side=LEFT)
        self.SCROLL_001.pack(side=RIGHT, fill=Y)
        self.SCROLL_002.pack(side=RIGHT, fill=Y)
        self.SCROLL_003.pack(side=RIGHT, fill=Y)
        self.SCROLL_004.pack(side=RIGHT, fill=Y)

        self.do_feed_lists()

        self.LSTLangues.bind("<Button-1>", self.do_SelectLangues)
        self.LSTTraductions.bind("<Button-1>", self.do_SelectTraductions)
        self.LSTTemplates.bind("<Button-1>", self.do_SelectTemplate)
        self.menu_annuler.btn.bind("<Button-1>", self.do_quitter)
        self.menu_valider.btn.bind("<Button-1>", self.do_apply_template)

    def do_SelectTemplate(self, event):
        try:
            fichier = codecs.open(repertoire_script + "data/" + self.LSTTemplates.selection_get(), "r", "utf-8")
        except:
            return 0
        self.LSTLivres.delete("0", "end")
        self.template = []
        contenu = fichier.readlines()
        for l in contenu:
            l = l.strip("\n")
            self.template.append(l.split("$"))
        fichier.close()
        VAR_row = 0
        for l in self.template:
            self.LSTLivres.insert(VAR_row, self.template[VAR_row][0])
            VAR_row += 1

    def do_SelectLangues(self, event):
        self.LSTTraductions.delete("0", "end")
        self.LSTLivres.delete("0", "end")
        try:
            self.Code_Langue = self.LSTLangues.selection_get()
        except:
            return 0
        self.Code_Langue = self.do_code_langue(self.Code_Langue)
        VAR_row = 0
        for l in Bibles.select().where(Bibles.langue == self.Code_Langue):
            self.LSTTraductions.insert(VAR_row, l.titre)
            VAR_row += 1

    def do_SelectTraductions(self, event):
        try:
            self.Traduction = self.LSTTraductions.selection_get()
        except:
            pass
        self.LSTLivres.delete("0", "end")
        VAR_row = 0
        for l in Livres.select().where(Livres.ID_Bible == Bibles.select().where(Bibles.titre == self.Traduction)):
            if len(l.Nom_Livre) > 0:
                self.LSTLivres.insert(VAR_row, l.Nom_Livre.strip())
            else:
                self.LSTLivres.insert(VAR_row, l.N_Livres)
            VAR_row += 1

    def do_update_db(self):
        self.langues = []
        self.traductions = []
        self.livres = []

        for l in Langues.select():
            self.langues.append([l.langue, l.description])

    def do_feed_lists(self):
        self.do_update_db()
        self.LSTLangues.delete("0", "end")
        self.LSTTraductions.delete("0", "end")
        VAR_row = 0
        for l in self.langues:
            if len(l[1]) > 0:
                # Si il existe une description de la langue alors on l'utilise
                self.LSTLangues.insert(VAR_row, l[1])
            else:
                # Sinon, on utilise le code langue
                self.LSTLangues.insert(VAR_row, l[0])
            VAR_row += 1
        self.do_crawl_templates()

    def do_code_langue(self, code):
        """ Retourne le code langue en fonction du code langue ou de la description langue
        """
        for l in self.langues:
            if l[0] == code:
                return code
            if l[1] == code:
                return l[0]

    def do_langue(self, code):
        """ Retourne la langue en fonction du code langue
        """
        for l in self.langues:
            if l[1] == code:
                return code
            if l[0] == code:
                return l[1]

    def do_crawl_templates(self):
        templates = 0
        for root, dirs, files in os.walk(repertoire_script + "/data/"):
            for name in files:
                if name.endswith((".tpl")):
                    self.LSTTemplates.insert(templates, name)
                    templates += 1
        if self.debug:
            print(f"Vous avez {templates} templates.")

    def do_quitter(self, event):
        self.destroy()

    def do_apply_template(self, event):
        self.LSTLivres.delete("0", "end")
        VAR_row = 0
        try:
            test = len(self.Traduction)
            if self.debug:
                print(f"{self.Traduction}")
        except:
            return 0
        s = pygame.mixer.Sound(repertoire_script + "sounds/mgb-7.ogg")
        s.play()
        for l in self.template:
            self.LSTLivres.insert(VAR_row, self.template[VAR_row][0])
            q = Livres.update({Livres.Nom_Livre: self.template[VAR_row][0], Livres.Shortcut: self.template[VAR_row][1]}).where(
                Livres.ID_Bible == Bibles.select().where(Bibles.titre == self.Traduction, Livres.N_Livres == VAR_row + 1)
            )
            q.execute()
            VAR_row += 1

    def run(self):
        self.interface()


if __name__ == "__main__":
    w = Tk()
    w.after(30000, w.destroy)
    w.wm_state("icon")
    App = AppApplyTemplate(debug=True)
    App.run()
    w.mainloop()
