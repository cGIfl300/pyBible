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
from class_pyBible import pyBible_Global
from class_autobutton import creer_autobutton

pygame.init()

class pyBible(Tk):
    ''' Interface graphique ...
    '''
    def __init__(self, debug = False):
        Tk.__init__(self)
        self.debug = debug
        self.magic_system = pyBible_Global()
    
    def interface(self):
        ''' Interface de la fenêtre
        '''
        self.title('pyBible')
        self.panel_menu = Canvas(self, bg = couleur_fond)
        self.panel_contenu = Canvas(self, bg = couleur_fond)
        
        self.menu_marque_pages = creer_autobutton(self.panel_menu, texte = 'Marque\nPage')
        self.menu_rechercher_mot = creer_autobutton(self.panel_menu, texte = 'Rechercher')
        self.menu_configurer = creer_autobutton(self.panel_menu, texte = 'Configurer')
        
        self.SCROLL_001 = Scrollbar(self.panel_contenu,
                                    orient = VERTICAL)
        self.contenu = Text(self.panel_contenu,
                            bg = couleur_fond,
                            fg = couleur_texte,
                            yscrollcommand = self.SCROLL_001.set)
        
        self.SCROLL_001.config(command = self.contenu.yview)
        test = self.magic_system.word_found('ruth')
        test2 = ''
        for l in test:
            test2 = test2 + f'{l[0]} {l[1]} {l[2]} - {self.magic_system.verset_found(l[0], l[1], l[2])}\n'
        self.contenu.insert('0.0', test2)
        self.contenu.config(state = DISABLED)
        
        ''' Implantation des composants
        '''
        self.panel_menu.pack(fill = BOTH,
                             expand = True)
        self.panel_contenu.pack(fill = BOTH,
                                expand = True)
        self.SCROLL_001.pack(side = RIGHT,
                             fill = Y)
        self.contenu.pack(fill = BOTH,
                          expand = True)
    def do_a_try(self):
        ''' Testing code
        '''
        app_essai = pyBible_Global()
        print(app_essai.verset_found(1,1,1))
        print(app_essai.word_found('dieu'))
        resultats = app_essai.word_found('dieu')
        print(f'Occurences : {len(resultats)}')
        print(resultats)
    
    def run(self):
        self.interface()
        self.mainloop()

if __name__ == '__main__':
    App = pyBible(debug = True)
    App.run()
