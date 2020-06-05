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
import time

class pyBible_Global():
    def __init__(self, debug = False, langue = 'FRE', traduction = 'French Louis Segond'):
        self.debug = debug
        self.langue = langue
        self.traduction = traduction
        self.bookname = ''
    
    def run(self):
        pass
    
    def chapitre_found(self, book, chapitre):
        ''' Retourne tous les versets d'un chapitre
        '''
        resultats = []
        l = Livres.get(Livres.ID_Bible == Bibles.get(Bibles.titre == self.traduction, Bibles.langue == self.langue), Livres.N_Livres == book)
        for v in Versets.select().where(Versets.ID_Bible == Bibles.get(Bibles.titre == self.traduction, Bibles.langue == self.langue), Versets.ID_Livre == l, Versets.N_Chapitre == chapitre):
            resultats.append([l.N_Livres, v.N_Chapitre, v.N_Verset, v.Texte])
            self.bookname = l.Nom_Livre
        return resultats
    
    def word_found(self, word):
        ''' Recherche un mot dans la Bible active
        '''
        word = word.upper()
        resultats = []
        for l in Livres.select().where(Livres.ID_Bible == Bibles.get(Bibles.titre == self.traduction, Bibles.langue == self.langue)):
            for v in Versets.select().where(Versets.ID_Bible == Bibles.get(Bibles.titre == self.traduction, Bibles.langue == self.langue), Versets.ID_Livre == l):
                verset = str(v.Texte)
                verset = verset.upper()
                if verset.find(word) > 0:
                    resultats.append([l.N_Livres, v.N_Chapitre, v.N_Verset])
                pass
        return resultats
    
    def verset_found(self, book, chapitre, verset):
        ''' Recherche d'un verset
        '''
        try:
            record = Versets.get(Versets.ID_Bible == Bibles.get(Bibles.langue == self.langue, Bibles.titre == self.traduction), Versets.ID_Livre == Livres.get(Livres.ID_Bible == Bibles.get(Bibles.langue == self.langue, Bibles.titre == self.traduction), Livres.N_Livres == book), Versets.N_Chapitre == chapitre, Versets.N_Verset == verset)
        except:
            return 0
        resultat = record.Texte
        return resultat
if __name__ == '__main__':
    app = pyBible_Global(debug = True)
    app.run()
