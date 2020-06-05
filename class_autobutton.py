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
from configuration import *

class creer_autobutton():
    ''' Ajouter un bouton personnalisé qui change en fonction du survol de celui-ci.
    
    exemple d'utilisation:
    
    menu1 = creer_bouton(w, couleur_fond, couleur_texte)
    menu1.btn.bind("<Button-1>", do_mafonction)
    '''
    def __init__(self, master, couleur_fond = couleur_fond, couleur_texte = couleur_texte,
                 bordure = 1, texte = '', cote = LEFT):
        self.master = master
        self.couleur_fond = couleur_fond
        self.couleur_texte = couleur_texte
        self.bordure = bordure
        self.labelfond = Label(self.master,
                               bg = couleur_texte)
        self.btn = Label(self.labelfond,
                         bg = couleur_fond,
                         fg = couleur_texte,
                         text = texte,
                         anchor = CENTER)
        
        self.btn.pack(expand = True,
                      fill = BOTH,
                      padx = bordure,
                      pady = bordure)
        self.labelfond.pack(fill = BOTH,
                            expand = True,
                            side = cote)
        
        self.labelfond.bind("<Enter>", self.do_btn_over)
        self.labelfond.bind("<Leave>", self.do_btn_leave)
    
    def do_btn_over(self, event):
        self.labelfond.config(bg = self.couleur_fond)
        self.btn.config(fg = self.couleur_fond,
                        bg = self.couleur_texte,
                        padx = self.bordure,
                        pady = self.bordure)
        
    def do_btn_leave(self, event):
        self.labelfond.config(bg = self.couleur_texte)
        self.btn.config(fg = self.couleur_texte,
                        bg = self.couleur_fond,
                        padx = self.bordure,
                        pady = self.bordure)
