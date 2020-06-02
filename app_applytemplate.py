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
import time
import codecs

pygame.init()

class AppApplyTemplate(Toplevel):
    ''' Applique un modèle de nomage de livres à une Bible
    '''
    def __init__(self, debug = False):
        Toplevel.__init__(self)
        self.debug = debug
    
    def interface(self):
        ''' Interface de la fenêtre
        '''
        self.title('Appliquer Modèle')
        self.geometry('400x200')
    
    def run(self):
        self.interface()

if __name__ == '__main__':
    w = Tk()
    w.after(30000, w.destroy)
    w.wm_state('icon')
    App = AppApplyTemplate(debug = True)
    App.run()
    w.mainloop()
