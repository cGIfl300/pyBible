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
from class_autobutton import creer_autobutton
from image_set import image_set

class AppBookmark(Toplevel):
    ''' Interface graphique ...
    '''
    def __init__(self, master, debug = False, langue = 'FRE', traduction = 'French Louis Segond', book = 1, chapitre = 1):
        Toplevel.__init__(self)
        self.debug = debug
        self.langue = langue
        self.traduction = traduction
        self.book = book
        self.chapitre = chapitre
        self.master = master
    
    def interface(self):
        ''' Interface de la fenêtre
        '''
        self.title('Marque Pages')
        
        self.panel_menu = Canvas(self, bg = couleur_fond)
        self.panel_contenu = Canvas(self, bg = couleur_fond)
        
        self.menu_delete = creer_autobutton(self.panel_menu, texte = 'Supprimer')
        self.menu_go = creer_autobutton(self.panel_menu, texte = 'Aller')
        self.menu_add = creer_autobutton(self.panel_menu, texte = 'Ajouter')
        
        self.SCROLL_001 = Scrollbar(self.panel_contenu,
                                    bg = couleur_fond,
                                    orient = VERTICAL)
        self.LSTBookmarks = Listbox(self.panel_contenu,
                                    selectmode = SINGLE,
                                    bg = couleur_fond_saisie,
                                    fg = couleur_texte_saisie,
                                    yscrollcommand = self.SCROLL_001.set)
        ''' Implantation des composants
        '''
        self.SCROLL_001.config(command = self.LSTBookmarks.yview)
        
        ''' Binding
        '''
        self.panel_menu.pack(fill = BOTH,
                         expand = True)
        self.panel_contenu.pack(fill = BOTH,
                         expand = True)
        self.decoration = image_set(self.panel_contenu, image_locale = 'images/vertical_spacer')
        self.LSTBookmarks.pack(fill = BOTH,
                         expand = True,
                         side = LEFT)
        self.SCROLL_001.pack(side = RIGHT,
                             fill = Y)
    
    def feed_list(self):
        ''' Actialiser la liste des marque page
        '''
        pass
    
    def bookmark(self, livre, chapitre):
        ''' Bookmarks a chapiter
        emplacement:
        data/bookmarks.dat
        format:
        1,1
        '''
    # Si déjà présent dans la liste, ne pas l'ajouter
    pass
    
    def run(self):
        self.interface()

if __name__ == '__main__':
    w = Tk()
    w.after(30000, w.destroy)
    w.wm_state('icon')
    App = AppBookmark()
    App.run()
    w.mainloop()
