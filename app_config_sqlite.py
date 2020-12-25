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

import os

from creer_bouton import *


class app_config_sqlite(Toplevel):
    """ Application configuration sqlite
    """

    def __init__(self, debug=False):
        Toplevel.__init__(self)
        self.debug = debug

    def interface(self):
        """ Interface de la fenêtre
        """
        self.title(_("Configuration sqlite"))

        self.panel_001 = Label(self, bg=couleur_fond)

        self.lbl_db_database = Label(self.panel_001, fg=couleur_texte, bg=couleur_fond, text=_("Base de données: "))

        self.entry_db_database = Entry(self.panel_001, bg=couleur_fond_saisie, fg=couleur_texte_saisie, relief="flat")
        self.entry_db_database.insert(0, repertoire_script + "data{}pybible.db".format(os.path.sep))

        self.btn_enregistrer = Button(
            self.panel_001,
            bg=couleur_fond_saisie,
            fg=couleur_texte_saisie,
            text=_("Enregistrer"),
            command=self.do_genere,
            activebackground=couleur_activebackground,
            activeforeground=couleur_activeforeground,
        )

        """ Implantation des composants
        """

        self.panel_001.pack(fill=BOTH, expand=True)

        Grid.rowconfigure(self.panel_001, 0, weight=1)
        Grid.rowconfigure(self.panel_001, 1, weight=1)
        Grid.columnconfigure(self.panel_001, 0, weight=1)
        Grid.columnconfigure(self.panel_001, 1, weight=1)

        self.lbl_db_database.grid(column=0, row=0, sticky=W + E)
        self.entry_db_database.grid(column=1, row=0, sticky=W + E)
        self.btn_enregistrer.grid(column=0, row=1, sticky=W + E + N + S, columnspan=2)

    def run(self):
        self.interface()

    def do_genere(self):
        generer_secret_garden(db_type="sqlite", db_database=self.entry_db_database.get())
        self.destroy()


if __name__ == "__main__":
    w = Tk()
    w.after(30000, w.destroy)
    w.wm_state("icon")
    App = app_config_sqlite(debug=True)
    App.run()
    w.mainloop()
