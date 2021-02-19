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

import time

from acquiert_bible import *
from app_edit_bibles import AppEditBibles
from app_secret_garden import app_secret_garden
from configuration_langues import Configuration_Langues
from db_creation import *
from image_set import image_set

fr = gettext.translation(
    "base",
    localedir=repertoire_script + "locales",
    languages=[langue_appli],
    fallback=False,
)
fr.install()
_ = fr.gettext
ngettext = fr.ngettext


def do_initialiser(event):
    App = db_creation()
    App.run()


def do_ImportXML(event):
    start_time = time.time()
    traductions = 0
    for root, dirs, files in os.walk(repertoire_script + "data/xml/"):
        for name in files:
            if name.endswith((".xml")):
                traductions = traductions + 1
                app = Acquiert_Bible(fichier_xml=os.path.join(root, name), debug=debug)
                app.run()
    print(_("Vous avez {} traductions.".format(traductions)))
    print(_("Temps d'execution: %s secondes" % (round(time.time() - start_time))))


def do_quitter(event):
    w.destroy()


def do_secret_garden(event):
    app = app_secret_garden()
    app.run()


def do_EditerLangues(event):
    app = Configuration_Langues()
    app.run()


def do_EditerBibles(event):
    app = AppEditBibles()
    app.run()


if __name__ == "__main__":
    w = Tk()
    w.title(_("pyBible - Configuration"))

    w.panel_001 = Label(w, bg=couleur_fond, fg=couleur_texte)
    w.panel_002 = Label(w, bg=couleur_fond, fg=couleur_texte)
    w.panel_003 = Label(w, bg=couleur_fond, fg=couleur_texte)

    w.menu11 = creer_bouton(
        w.panel_001, image_locale="images/menu_secret_garden", cote=TOP
    )
    w.menu12 = creer_bouton(
        w.panel_001, image_locale="images/menu_initialiser_base_locale", cote=TOP
    )
    w.menu13 = creer_bouton(
        w.panel_001, image_locale="images/menu_importer_bible_xml", cote=TOP
    )
    w.menu14 = creer_bouton(w.panel_001, image_locale="images/menu_elangues", cote=TOP)
    w.menu15 = creer_bouton(w.panel_001, image_locale="images/menu_ebibles", cote=TOP)

    w.menu2 = image_set(w.panel_002, image_locale="images/vertical_spacer")

    w.menu35 = creer_bouton(w.panel_003, image_locale="images/menu_quitter", cote=TOP)

    w.panel_001.pack(fill=BOTH, expand=True, side=LEFT)
    w.panel_002.pack(fill=BOTH, expand=True, side=LEFT)
    w.panel_003.pack(fill=BOTH, expand=True, side=LEFT)

    w.menu11.btn.bind("<Button-1>", do_secret_garden)
    w.menu12.btn.bind("<Button-1>", do_initialiser)
    w.menu13.btn.bind("<Button-1>", do_ImportXML)
    w.menu14.btn.bind("<Button-1>", do_EditerLangues)
    w.menu15.btn.bind("<Button-1>", do_EditerBibles)

    w.menu35.btn.bind("<Button-1>", do_quitter)

    w.mainloop()
