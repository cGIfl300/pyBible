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

import codecs
import gettext
import time
from tkinter import *

import pygame
from peewee import *

from app_applytemplate import AppApplyTemplate
from creer_bouton import creer_bouton
from db_model import *

fr = gettext.translation(
    "base",
    localedir=repertoire_script + "locales",
    languages=[langue_appli],
    fallback=False,
)
fr.install()
_ = fr.gettext
ngettext = fr.ngettext

pygame.init()


class AppEditBibles(Toplevel):
    """Application d'édition des tites des livres contenus dans les Bibles."""

    def __init__(self, debug=False):
        Toplevel.__init__(self)
        self.debug = debug
        self.Traduction = ""
        self.Code_Langue = ""
        self.Numéro_Livre = ""
        self.Template = ""

    def interface(self):
        """Interface de la fenêtre"""
        self.title(_("Editeur Bibles"))

        self.panel0 = Canvas(self, bg=couleur_fond)
        self.panel1 = Canvas(self, bg=couleur_fond)
        self.panel_langue = Canvas(self.panel0, bg=couleur_fond)
        self.panel_traduction = Canvas(self.panel0, bg=couleur_fond)
        self.panel_livres = Canvas(self.panel0, bg=couleur_fond)
        self.panel_saisie = Canvas(self.panel1, bg=couleur_fond)
        self.SCROLL_001 = Scrollbar(self.panel_langue, orient=VERTICAL)
        self.SCROLL_002 = Scrollbar(self.panel_traduction, orient=VERTICAL)
        self.SCROLL_003 = Scrollbar(self.panel_livres, orient=VERTICAL)

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

        self.SCROLL_001.config(command=self.LSTLangues.yview)
        self.SCROLL_002.config(command=self.LSTTraductions.yview)
        self.SCROLL_003.config(command=self.LSTLivres.yview)
        self.panel_langue.config(yscrollcommand=self.SCROLL_001.set)

        self.description = Label(
            self.panel_saisie,
            bg=couleur_fond,
            fg=couleur_texte,
            text=_("Aucun livre sélectionné"),
        )

        self.lbl_shortcut = Label(
            self.panel_saisie, fg=couleur_texte, bg=couleur_fond, text=_("Courte: ")
        )

        self.entry_shortcut = Entry(
            self.panel_saisie,
            bg=couleur_fond_saisie,
            fg=couleur_texte_saisie,
            relief="flat",
        )

        self.lbl_longue = Label(
            self.panel_saisie, fg=couleur_texte, bg=couleur_fond, text=_("Complet: ")
        )

        self.entry_longue = Entry(
            self.panel_saisie,
            bg=couleur_fond_saisie,
            fg=couleur_texte_saisie,
            relief="flat",
        )

        self.menu_exporter = creer_bouton(
            self.panel1, image_locale="images/menu_exporter"
        )
        self.menu_importer = creer_bouton(
            self.panel1, image_locale="images/menu_importer"
        )
        self.panel_saisie.pack(fill=BOTH, expand=True, side=LEFT)
        self.menu_enregistrer = creer_bouton(
            self.panel1, image_locale="images/menu_enregistrer"
        )

        """ Positionnement des widgets
        """
        self.panel0.pack(fill=BOTH, expand=True)
        self.panel1.pack(fill=BOTH, expand=True)
        self.panel_langue.pack(fill=BOTH, expand=True, side=LEFT)
        self.panel_traduction.pack(fill=BOTH, expand=True, side=LEFT)
        self.panel_livres.pack(fill=BOTH, expand=True, side=LEFT)
        self.LSTLangues.pack(fill=BOTH, expand=True, side=LEFT)
        self.LSTTraductions.pack(fill=BOTH, expand=True, side=LEFT)
        self.LSTLivres.pack(fill=BOTH, expand=True, side=LEFT)
        self.SCROLL_001.pack(side=RIGHT, fill=Y)
        self.SCROLL_002.pack(side=RIGHT, fill=Y)
        self.SCROLL_003.pack(side=RIGHT, fill=Y)

        self.description.pack(fill=BOTH, expand=True)
        self.lbl_shortcut.pack(fill=BOTH, expand=True)
        self.entry_shortcut.pack(fill=BOTH, expand=True)
        self.lbl_longue.pack(fill=BOTH, expand=True)
        self.entry_longue.pack(fill=BOTH, expand=True)

        self.do_feed_lists()

        """ Binding
        """
        self.LSTLangues.bind("<Button-1>", self.do_SelectLangues)
        self.LSTTraductions.bind("<Button-1>", self.do_SelectTraductions)
        self.LSTLivres.bind("<Button-1>", self.do_SelectLivres)
        self.menu_enregistrer.btn.bind("<Button-1>", self.do_validate)
        self.menu_exporter.btn.bind("<Button-1>", self.do_export)
        self.menu_importer.btn.bind("<Button-1>", self.do_import)

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
        self.LSTLivres.delete("0", "end")
        try:
            self.Traduction = self.LSTTraductions.selection_get()
        except:
            pass
        VAR_row = 0
        for l in Livres.select().where(
            Livres.ID_Bible == Bibles.select().where(Bibles.titre == self.Traduction)
        ):
            self.LSTLivres.insert(VAR_row, l.N_Livres)
            VAR_row += 1

    def do_export(self, event):
        """Exporte un modèle de nomage de livres"""
        if self.Traduction == "":
            return 0
        self.entry_shortcut.delete("0", "end")
        self.entry_longue.delete("0", "end")

        liste_livres = []

        for l in Livres.select().where(
            Livres.ID_Bible == Bibles.select().where(Bibles.titre == self.Traduction)
        ):
            liste_livres.append([l.Nom_Livre, l.Shortcut])

        if self.debug:
            print(f"{liste_livres}")

        Nom_Template = self.Code_Langue + "-" + str(time.time()) + ".tpl"
        if self.debug:
            print(f"{Nom_Template}")

        fichier = codecs.open(repertoire_script + "data/" + Nom_Template, "w", "utf-8")
        for l in liste_livres:
            if l[0].strip() == "":
                l[0] = "-"
            if l[1].strip() == "":
                l[1] = "-"
            fichier.write(l[0].strip() + "$" + l[1].strip() + "\n")
        fichier.close()

        self.description.config(
            text=_("Exportation réussie de:\n{}\n{}").format(
                Nom_Template, self.Traduction
            )
        )
        s = pygame.mixer.Sound(repertoire_script + "sounds/mgb-7.ogg")
        s.play()

    def do_import(self, event):
        """Importe un modèle de nomage de livres et l'applique à la traduction courante"""
        app = AppApplyTemplate()
        app.run()
        s = pygame.mixer.Sound(repertoire_script + "sounds/mgb-7.ogg")
        s.play()

    def do_SelectLivres(self, event):
        try:
            self.Numero_Livre = self.LSTLivres.selection_get()
        except:
            return 0
        self.description.config(
            text=_(
                """Langue: {}
Titre: {}
Livre N°: {}"""
            ).format(
                self.do_langue(self.Code_Langue), self.Traduction, self.Numero_Livre
            )
        )
        self.entry_shortcut.delete("0", "end")
        self.entry_longue.delete("0", "end")
        for l in Livres.select().where(
            Livres.ID_Bible == Bibles.select().where(Bibles.titre == self.Traduction)
        ):
            if str(l.N_Livres) == str(self.Numéro_Livre):
                self.entry_longue.insert("0", l.Nom_Livre)
                self.entry_shortcut.insert("0", l.Shortcut)

    def do_validate(self, event):
        s = pygame.mixer.Sound(repertoire_script + "sounds/blaster08.ogg")
        s.play()
        try:
            q = Livres.update(
                {
                    Livres.Nom_Livre: self.entry_longue.get(),
                    Livres.Shortcut: self.entry_shortcut.get(),
                }
            ).where(
                Livres.ID_Bible
                == Bibles.select().where(
                    Bibles.titre == self.Traduction,
                    Livres.N_Livres == self.Numéro_Livre,
                )
            )
            q.execute()
        except:
            if self.debug:
                print("Erreur: do_validate")
            pass

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
        self.LSTLivres.delete("0", "end")
        VAR_row = 0
        for l in self.langues:
            if len(l[1]) > 0:
                # Si il existe une description de la langue alors on l'utilise
                self.LSTLangues.insert(VAR_row, l[1])
            else:
                # Sinon, on utilise le code langue
                self.LSTLangues.insert(VAR_row, l[0])
            VAR_row += 1

    def do_code_langue(self, code):
        """Retourne le code langue en fonction du code langue ou de la description langue"""
        for l in self.langues:
            if l[0] == code:
                return code
            if l[1] == code:
                return l[0]

    def do_langue(self, code):
        """Retourne la langue en fonction du code langue"""
        for l in self.langues:
            if l[1] == code:
                return code
            if l[0] == code:
                return l[1]

    def run(self):
        self.interface()


if __name__ == "__main__":
    w = Tk()
    w.after(30000, w.destroy)
    w.wm_state("icon")
    App = AppEditBibles(debug=True)
    App.run()
    w.mainloop()
