# pyBible
**PROJET EN COURS DE REALISATION**  

![](images/backend-global-view.png) 

Outil de lecture et d'études bibliques OpenSource.  

## (DEV) Importer Bible XML
 
Setup_GUI.py fonctionne avec tkinter, c'est donc une application fenetrée.  
C'est l'interface de configuration principale du projet.  
Elle permet l'importation des Bibles contenues dans ./data au format xml.  
Les Bibles doivent contenir 66 livres (voir le code source pour plus de détails).  

> Les Bibles originales au format xml viennent de Zefania https://sourceforge.net/projects/zefania-sharp/  
> Certaines ont été excluses car elles ne permettaient pas une importation convenable dans notre base de donnée actuelle.  

### secret_garden.py

C'est le fichier de configuration de la base de donnée utilisée par pyBible, vous pouvez le modifier depuis Setup_GUI.py  

### Setup_GUI

Ce script est à utiliser pour générer la base de données et initialiser les données de configuration. Il est à exécuter AVANT toute compilation.  
Sauf si vous utilisez directement les scripts, il ne peut pas être utilisé après compilation. C'est un outil destiné aux dévelopeurs permetant de générer et / ou configurer la base de données.  

### (DEV) Todo Setup_GUI

- Interface de lecture desktop  

## (DEV) Todo pyBible

### Lecture d'une Bible

- Pouvoir lire une Bible.  
- Sélection d'une Bible par défaut.  
- Limiter les recherches à une langue spécifique.  

#### Marque pages

- Ouverture d'une Bible à la dernière page choisie par l'utilisateur (lecture continue).  
- Gestion d'un carnet de marque page (avec nomage de chaque marque page).  

#### Commentaires

Possibilité d'ajouter des commentaires:  
- Bible
- Livre
- Chapitre
- Verset (par défaut)

## Utilisateurs

Sous Windows, débrouillez-vous, vous avez l'habitude.  
Sous Linux, allez dans le répertoire destiné aux code sources. Vous devez être sous un environement graphique.  

####Réalisez une copie locale de ce dépôt:  
git clone https://github.com/cgifl300/pybible.git  
####Ensuite allez dans pybible:  
cd pybible  
####Reconstituez l'environement python avec toutes ses librairies:  
make init  
####Lancez l'interface de configuration:  
make setup  
L'interface de configuration et de génération de la base de donnée derait s'ouvrir:  
![](images/doc-img001.png)   
Vous pouvez faire le trie des Bibles qui vous intéresse en supprimant celles qui ne vous intéresse pas dans data/xml .

Vous trouverez une base de donnée déjà construite en téléchargement sur mon site personnel https://www.blueroses.fr/dl/pybible.db . C'est la méthode d'installation recommandée.  
Dans ce cas il vous suffira d'indiquer le chemin de la base de donnée sqlite en cliquant sur 'secret_garden.py'.  
