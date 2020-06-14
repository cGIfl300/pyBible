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
from creer_bouton import *
import os

class app_config_mysql(Toplevel):
    ''' Application configuration sqlite
    '''
    def __init__(self, debug = False):
        Toplevel.__init__(self)
        self.debug = debug
    
    def interface(self):
        ''' Interface de la fenêtre
        '''
        self.title(_('Configuration MySQL'))
        
        self.panel_001 = Label(self, bg = couleur_fond)
        
        self.lbl_db_server = Label(self.panel_001,
                                   fg = couleur_texte,
                                   bg = couleur_fond,
                                   text = _('Serveur: '))
        
        self.entry_db_server = Entry(self.panel_001,
                                bg = couleur_fond_saisie,
                                fg = couleur_texte_saisie,
                                relief = 'flat')
        
        self.lbl_db_username = Label(self.panel_001,
                                   fg = couleur_texte,
                                   bg = couleur_fond,
                                   text = _('Nom d\'utilisateur: '))
        
        self.entry_db_username = Entry(self.panel_001,
                                bg = couleur_fond_saisie,
                                fg = couleur_texte_saisie,
                                relief = 'flat')
        
        self.lbl_db_password = Label(self.panel_001,
                                   fg = couleur_texte,
                                   bg = couleur_fond,
                                   text = _('Mot de passe: '))
        
        self.entry_db_password = Entry(self.panel_001,
                                bg = couleur_fond_saisie,
                                fg = couleur_texte_saisie,
                                relief = 'flat')
        
        self.lbl_db_database = Label(self.panel_001,
                                   fg = couleur_texte,
                                   bg = couleur_fond,
                                   text = _('Base de données: '))
        
        self.entry_db_database = Entry(self.panel_001,
                                bg = couleur_fond_saisie,
                                fg = couleur_texte_saisie,
                                relief = 'flat')
        
        self.lbl_db_port = Label(self.panel_001,
                                   fg = couleur_texte,
                                   bg = couleur_fond,
                                   text = 'Port: ')
        
        self.entry_db_port = Entry(self.panel_001,
                                bg = couleur_fond_saisie,
                                fg = couleur_texte_saisie,
                                relief = 'flat')
        self.entry_db_port.insert(0, '3306')
        
        self.btn_enregistrer = Button(self.panel_001,
                                  bg = couleur_fond_saisie,
                                  fg = couleur_texte_saisie,
                                  text = _('Enregistrer'),
                                  command = self.do_genere,
                                  activebackground = couleur_activebackground,
                                  activeforeground = couleur_activeforeground)
        
        ''' Implantation des composants
        '''
        
        self.panel_001.pack(fill = BOTH,
                            expand = True)
        
        Grid.rowconfigure(self.panel_001, 0, weight=1)
        Grid.rowconfigure(self.panel_001, 1, weight=1)
        Grid.rowconfigure(self.panel_001, 2, weight=1)
        Grid.rowconfigure(self.panel_001, 3, weight=1)
        Grid.rowconfigure(self.panel_001, 4, weight=1)
        Grid.rowconfigure(self.panel_001, 5, weight=1)
        Grid.columnconfigure(self.panel_001, 0, weight=1)
        Grid.columnconfigure(self.panel_001, 1, weight=1)
        
        self.lbl_db_server.grid(column = 0,
                                row = 0,
                                sticky = W+E)
        self.entry_db_server.grid(column = 1,
                               row = 0,
                               sticky = W+E)
        self.lbl_db_username.grid(column = 0,
                                row = 1,
                                sticky = W+E)
        self.entry_db_username.grid(column = 1,
                               row = 1,
                               sticky = W+E)
        self.lbl_db_password.grid(column = 0,
                                row = 2,
                                sticky = W+E)
        self.entry_db_password.grid(column = 1,
                               row = 2,
                               sticky = W+E)
        self.lbl_db_database.grid(column = 0,
                                row = 3,
                                sticky = W+E)
        self.entry_db_database.grid(column = 1,
                               row = 3,
                               sticky = W+E)
        self.lbl_db_port.grid(column = 0,
                                row = 4,
                                sticky = W+E)
        self.entry_db_port.grid(column = 1,
                               row = 4,
                               sticky = W+E)
        
        self.btn_enregistrer.grid(column = 0,
                              row = 5,
                              sticky=W+E+N+S,
                              columnspan = 2)
    
    def run(self):
        self.interface()
    
    def do_genere(self):
        try:
            port = int(self.entry_db_port.get())
        except:
            port = 3306

        generer_secret_garden(db_type = 'mysql',
                              db_server = self.entry_db_server.get(),
                              db_username = self.entry_db_username.get(),
                              db_password = self.entry_db_password.get(),
                              db_database = self.entry_db_database.get(),
                              db_port = port)
        self.destroy()

if __name__ == '__main__':
    w = Tk()
    w.after(30000, w.destroy)
    w.wm_state('icon')
    App = app_config_mysql(debug = True)
    App.run()
    w.mainloop()
