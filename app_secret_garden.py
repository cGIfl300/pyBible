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
from creer_bouton import *
from app_config_sqlite import *
from app_config_mysql import *

class app_secret_garden():
    ''' Interface graphique ...
    Création du fichier de configuration secret_garden.py
    '''
    def __init__(self, debug = False):
        self.debug = debug
    
    def interface(self):
        ''' Interface de la fenêtre de configuration
        '''
        self.tl = Toplevel()
        self.tl.title('secret_garden')
        self.tl.panel_001 = Label(self.tl, bg = couleur_fond)
        
        self.tl.lbl001 = Label(self.tl.panel_001,
                                   text = '''Création du fichier de configuration
local: secret_garden.py''',
                                   bg = couleur_fond,
                                   fg = couleur_texte)
            
        self.tl.menu1 = creer_bouton(self.tl.panel_001, image_locale = 'images/menu_mysql',
                                     cote = BOTTOM)
        self.tl.menu1.btn.bind("<Button-1>", self.do_create_mysql)
        self.tl.menu2 = creer_bouton(self.tl.panel_001, image_locale = 'images/menu_sqlite',
                                     cote = BOTTOM)
        self.tl.menu2.btn.bind("<Button-1>", self.do_create_sqlite)
            
        """ Implantation des composants
        """
        
        self.tl.panel_001.pack(fill = BOTH,
                            expand = True)
        self.tl.lbl001.pack(side = TOP)
        
    
    def run(self):
        self.interface()
        
    def do_create_sqlite(self, event):
        ''' Création du fichier de configuration secret_garden.py
        format sqlite
        '''
        if self.debug:
            print('do_create_sqlite')
        app = app_config_sqlite()
        app.run()
    
    def do_create_mysql(self, event):
        ''' Création du fichier de configuration secret_garden.py
        format mysql
        '''
        if self.debug:
            print('do_create_mysql')
        app = app_config_mysql()
        app.run()

if __name__ == '__main__':
    w = Tk()
    w.after(30000, w.destroy)
    w.wm_state('icon')
    App = app_secret_garden(debug = True)
    App.run()
    w.mainloop()
