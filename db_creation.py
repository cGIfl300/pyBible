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

import gettext

from peewee import *

from creer_bouton import *
from db_model import *

fr = gettext.translation("base", localedir=repertoire_script + "locales", languages=[langue_appli], fallback=False)
fr.install()
_ = fr.gettext
ngettext = fr.ngettext


class db_creation:
    """ Interface graphique ...
    Création du fichier de configuration de la base de données
    """

    def __init__(self, debug=False):
        self.debug = debug

    def interface(self):
        """ Interface de la fenêtre de configuration
        """
        self.tl = Toplevel()
        self.tl.title(_("Configuration DB"))
        self.tl.panel_001 = Label(self.tl, bg=couleur_fond)

        self.tl.lbl001 = Label(self.tl.panel_001, text=_("Type de base: {}".format(db_type)), bg=couleur_fond,
                               fg=couleur_texte)

        self.tl.menu1 = creer_bouton(self.tl.panel_001, image_locale="images/menu_confirmer", cote=BOTTOM)
        self.tl.menu1.btn.bind("<Button-1>", self.do_initialisation)

        """ Implantation des composants
        """

        self.tl.panel_001.pack(fill=BOTH, expand=True)
        self.tl.lbl001.pack()

    def run(self):
        self.interface()

    def do_initialisation(self, event):
        """ Algorithme de création de la base de données
        """
        if self.debug:
            print("do_initialisation")
        # Connection aux différentes bases
        db_link = connexion_db()

        # Création des tables initiales
        db_link.create_tables([Langues, Bibles, Livres, Versets])

        self.tl.destroy()


if __name__ == "__main__":
    w = Tk()
    w.after(30000, w.destroy)
    w.wm_state("icon")
    App = db_creation(debug=True)
    App.run()
    w.mainloop()
