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
        self.title('Rechercher')
        self.geometry('400x200')
        
        ''' Implantation des composants
        '''
        
        ''' Binding
        '''
    
    def do_Recherche(self, phrase):
        ''' Recherche d'un mot ou d'une phrase dans la traduction active
        '''
        résultats = self.moteur.word_found(phrase)
        if self.debug:
            print(f'Il y a {len(résultats)} résultats.')
            print(résultats)
    
    def run(self):
        self.interface()

if __name__ == '__main__':
    w = Tk()
    w.after(30000, w.destroy)
    w.wm_state('icon')
    App = AppRechercher(debug = True, langue = 'FRE', traduction = 'French Louis Segond')
    App.run()
    w.mainloop()
