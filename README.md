# pyBible
**PROJET EN COURS DE REALISATION**  

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

- Utilisation de modèles de nomage des lives (Editeur de Bibles) - en cours -  
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

Vous trouverez une base de donnée déjà construite en téléchargement sur mon site personnel https://www.blueroses.fr/dl/pybible.db .  