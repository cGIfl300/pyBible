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
import pygame
from configuration import *
from class_pyBible import pyBible_Global
import gettext

fr = gettext.translation('base', localedir='locales', languages=[langue_appli], fallback=False)
fr.install()
_ = fr.gettext
ngettext = fr.ngettext

pygame.init()

class AppRechercher(Toplevel):
    ''' Interface graphique ...
    '''
    def __init__(self, debug = False, langue = 'FRE', traduction = 'French Louis Segond', book = 1, chapitre = 1):
        Toplevel.__init__(self)
        self.debug = debug
        self.langue = langue
        self.traduction = traduction
        self.book = book
        self.chapitre = chapitre
        self.moteur = pyBible_Global(langue = self.langue, traduction = self.traduction)
    
    def interface(self):
        ''' Interface de la fenêtre
        '''
        self.title(_('Rechercher'))
        
        self.panel_menu = Canvas(self, bg = couleur_fond)
        self.panel_contenu = Canvas(self, bg = couleur_fond)
        
        self.SCROLL_001 = Scrollbar(self.panel_contenu,
                                    bg = couleur_fond,
                                    orient = VERTICAL)
        self.contenu = Text(self.panel_contenu,
                            bg = couleur_fond,
                            fg = couleur_texte,
                            wrap = WORD,
                            yscrollcommand = self.SCROLL_001.set)
        self.SCROLL_001.config(command = self.contenu.yview)
        self.contenu.config(state = DISABLED)
        self.entry_recherche = Entry(self.panel_menu,
                                bg = couleur_fond_saisie,
                                fg = couleur_texte_saisie,
                                relief = 'flat')
        
        ''' Implantation des composants
        '''
        
        self.panel_menu.pack(fill = BOTH,
                             expand = True)
        self.entry_recherche.pack(fill = BOTH,
                              expand = True)
        self.panel_contenu.pack(fill = BOTH,
                                expand = True)
        self.SCROLL_001.pack(side = RIGHT,
                             fill = Y)
        self.contenu.pack(fill = BOTH,
                          expand = True)
        
        ''' Binding
        '''
        self.entry_recherche.bind('<Return>', self.do_Recherche)
        self.entry_recherche.bind('<KP_Enter>', self.do_Recherche)
    
    def do_Recherche(self, event):
        ''' Recherche d'un mot ou d'une phrase dans la traduction active
        '''
        phrase = self.entry_recherche.get()
        résultats = self.moteur.word_found(phrase)
        self.entry_recherche.config(state = DISABLED)
        if self.debug:
            print(f'Il y a {len(résultats)} résultats.')
            print(résultats)
        self.contenu.config(state = NORMAL)
        self.contenu.delete('0.0', 'end')
        temporaire = _('{} résultats.\n\n').format(len(résultats))
        ancien_nom_livre = ''
        for l in résultats:
            verset = self.moteur.verset_found(l[0], l[1], l[2])
            nom_livre = self.moteur.chapitre_found(l[0], l[1])
            nom_livre = self.moteur.bookname
            if ancien_nom_livre != nom_livre:
                if ancien_nom_livre == '':
                    temporaire = temporaire + f'{nom_livre.upper()}\n\n'
                else:
                    temporaire = temporaire + f'\n{nom_livre.upper()}\n\n'
                ancien_nom_livre = nom_livre
            temporaire = temporaire + f'{l[1]}:{l[2]} - {verset}\n' 
        self.contenu.insert('0.0', temporaire)
        self.contenu.config(state = DISABLED)
        self.entry_recherche.config(state = NORMAL)
    
    def run(self):
        self.interface()

if __name__ == '__main__':
    w = Tk()
    w.after(60000, w.destroy)
    w.wm_state('icon')
    App = AppRechercher(debug = True, langue = 'FRE', traduction = 'French Louis Segond')
    App.run()
    w.mainloop()
