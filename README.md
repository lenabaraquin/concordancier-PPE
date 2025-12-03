# Concordancier pour PPE1

## Présentation 

Le but de ce script est de générer les concordances dans un texte contenu dans un seul fichier.

Ce script gère trois langues : l'anglais, le persan et le français.
NLTK est utilisé pour les traitements de l'anglais et du français.
Shekar est utilisé pour les traitements du persan.

## Installation

Ce script a été testé avec la version 3.11.6 de python.

Pour installer les dépendances :

```
pip install -r requirements.txt
```

## Avec `uv`

Il est possible de créer un environnement dédié avec `uv` et d'y installer les dépendances:

```
uv venv --python 3.11.6 concordancier
uv pip install -r requirements.txt
```

## Usage

Ce script a besoin de quatre arguments :
 - le code ISO-639-1 de la langue (en, fa ou fr)
 - le chemin vers le fichier contenant le texte à analyser
 - la taille de la fenêtre contextuelle (nombre de mots avant et après la mot cible)
 - le mot cible

Ils doivent être passés dans sous cette forme :

```
python concordancier.py code_langue chemin/vers/fichier/texte taille_fenetre mot_cible
```

## Exemple 

Pour un texte français avec pour mot cible "Terre" et pour une fenêtre de taille 5 :

```
python concordancier.py fr exemple.txt 5 Terre
```

La sortie attendue a la forme suivante :

```
La	Terre	est la troisième planète par
L'axe de rotation de la	Terre	possède une inclinaison d'environ 23°
la datation radiométrique , la	Terre	s'est formée il y a
que la distance de la	Terre	au Soleil ( environ 150
ont un jour vécu sur	Terre	sont maintenant éteintes . En
milliards d'êtres humains vivent sur	Terre	et dépendent de sa biosphère
pour leur survie . La	Terre	est la planète la plus
La structure interne de la	Terre	est géologiquement active , le
détaillés : Histoire de la	Terre	et Histoire évolutive du vivant
vivant . L'âge de la	Terre	est aujourd'hui estimé à 4,54
```

## TESTS 

Pour les tests du scripts, j'ai utilisé l'article wikipedia Terre (il est traduit dans beaucoup de langues).
Vous pouvez retrouver les fichiers texte de test dans le dossier `./test/` sous la forme `code_langue.txt` et les sorties du script sous la forme `code_langue_concordances.tsv`.
