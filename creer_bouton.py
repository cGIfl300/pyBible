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
from tkinter import *
from PIL import Image, ImageTk

class creer_bouton():
    ''' Ajouter un bouton personnalisé avec une image
    qui change en fonction du survol de celui-ci.
    
    exemple d'utilisation:
    
    menu1 = creer_bouton(w, image_locale = 'images/mon_image')
    menu1.btn.bind("<Button-1>", do_mafonction)
    
    images/mon_image.png sera utilisé par défaut
    images/mon_image_over.png sera utilisé quand le curseur sera au dessus du bouton
    '''
    def __init__(self, master, image_locale, cote = LEFT):
        self.master = master
        self.original = Image.open(repertoire_script + image_locale + '.png')
        self.image_locale = ImageTk.PhotoImage(self.original)
        self.original_over = Image.open(repertoire_script + image_locale + '_over.png')
        self.image_over = ImageTk.PhotoImage(self.original_over)
        
        self.btn = Label(master, image = self.image_locale,
                            bg = couleur_fond)
        
        self.btn.pack(expand = True, fill = BOTH, side = cote)
        
        self.btn.bind("<Enter>", self.do_btn_over)
        self.btn.bind("<Leave>", self.do_btn_leave)
    
    def do_btn_over(self, event):
        self.btn.config(image = self.image_over)
        
    def do_btn_leave(self, event):
        self.btn.config(image = self.image_locale)
