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

from secret_garden import *
from configuration import *
from peewee import *

def connexion_db():
    ''' Connexion à la base de données
    '''
    if db_type == 'sqlite':
        if debug:
            print ('Connexion à la base de donnée SQLite {}'.format(db_database))
        db_link = SqliteDatabase(db_database, pragmas={
            'journal_mode': 'wal',
            'cache_size': -1024 * 256})

    if db_type == 'mysql':
        if debug:
            print ('Connexion à la base de donnée MySQL {}'.format(db_database))
        db_link = MySQLDatabase(db_database,
                                user = db_username,
                                password = db_password,
                                host = db_server,
                                port = db_port)
    return db_link

db_link = connexion_db()
    
class Langues(Model):
    langue = CharField()
    description = CharField()
    
    class Meta:
        database = db_link
        
class Bibles(Model):
    langue = ForeignKeyField(Langues)
    titre = CharField()
    description = TextField()

    class Meta:
        database = db_link
        
class Livres(Model):
    ID_Bible = ForeignKeyField(Bibles)
    N_Livres = IntegerField()
    Nom_Livre = CharField()
    Shortcut = CharField()
    
    class Meta:
        database = db_link
        
class Versets(Model):
    ID_Livre = ForeignKeyField(Livres)
    ID_Bible = ForeignKeyField(Bibles)
    N_Chapitre = IntegerField()
    N_Verset = IntegerField()
    Texte = TextField()
    
    class Meta:
        database = db_link
