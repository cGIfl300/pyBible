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

"""
Application qui permet de garder la page active
"""

from peewee import *
from db_model import *
from configuration import *
from class_autobutton import creer_autobutton
from image_set import image_set
import codecs
import os
import gettext

fr = gettext.translation("base", localedir=repertoire_script + "locales", languages=[langue_appli], fallback=False)
fr.install()
_ = fr.gettext
ngettext = fr.ngettext


class AppIamReading:
    """ Interface graphique ...
    update = mise à jour du bookmark
    """

    def __init__(self, debug=False, book=1, chapitre=2):
        self.debug = debug
        self.livre = book
        self.chapitre = chapitre
        self.bookmarks = []

    def update(self):
        """
        self.livre = livre
        self.chapitre = chapitre
        """
        self.bookmarks_refresh()

        fichier = codecs.open(repertoire_script + "data/bookmarks.dat", "w", "utf-8")

        fichier.write(f"o,{self.livre},{self.chapitre}\n")

        for l in self.bookmarks:
            if l[0] == "s":
                if self.debug:
                    print(f"Livre: {livre} is {l[1]} | Chapitre: {chapitre} is {l[2]}")
                fichier.write(f"s,{l[1]},{l[2]}\n")

        fichier.close()

    def bookmarks_refresh(self):
        """ Rafraîchir la liste des bookmarks
        """
        self.bookmarks = []
        fichier = codecs.open(repertoire_script + "data/bookmarks.dat", "r", "utf-8")
        contenu = fichier.readlines()
        fichier.close()
        for l in contenu:
            l = l.replace("\n", "")
            l = l.split(",")
            if l[0] == "s":
                self.bookmarks.append(l)

    def run(self):
        """ Cette application n'a pas d'interface
        """
        self.update()


if __name__ == "__main__":
    App = AppIamReading(book=8, chapitre=2)
    App.run()
