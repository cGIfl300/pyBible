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

import os

chemin_script = os.path.abspath(__file__)
repertoire_script = chemin_script[:next(i for i in reversed(range(len(chemin_script))) if chemin_script[i] == os.path.sep)+1]
couleur_fond = 'white'
couleur_texte = 'blue'
couleur_fond_saisie = 'white'
couleur_texte_saisie = 'blue'
couleur_activebackground = couleur_texte_saisie
couleur_activeforeground = couleur_fond_saisie
debug = True
langue_appli = 'fr'

def generer_secret_garden(db_type = 'sqlite',
                          db_username = '',
                          db_password = '',
                          db_database = 'change_me.db',
                          db_server = '',
                          db_port = 3306):
    ''' Génération du fichier de configuration de la base de données.
    '''
    if debug:
        print('Génération du fichier de configuration de la base de données.')
    pass
    fichier = open(repertoire_script + 'secret_garden.py', 'w')
    fichier.write('''# -*- coding:utf-8 -*-
#
# Copyright © 2020 cGIfl300
#
# This file contains secret data and should not be shared.

db_type = '{}'
db_username = '{}'
db_password = '{}'
db_database = '{}'
db_server = '{}'
db_port = {}'''.format(db_type,
                       db_username,
                       db_password,
                       db_database,
                       db_server,
                       db_port))
    fichier.close()
