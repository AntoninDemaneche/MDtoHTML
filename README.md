# MDtoHTML

## Comment ca marche ?

C'est très simple, il suffit d'installer le programme et ses addons.

Pour installer les addons, il faut ouvrir un terminal de commande et écrire :


```
pip install markdown2

pip install click
```

Pour lancer le convertisseur il suffit de créer un (ou plusieurs fichiers) au format **.MD** et de lancer le programme dans un terminal.

```
python converter.py
```

Il suffit d'y ajouter des arguments, accessibles via --help à la suite de la commande si dessus.

Voici la liste des arguments ici :

--dir ( Permet à l'utilisateur de convertir tous les fichiers MD d'un dossier avec une seule commande )


--i ( Si l'utilisateur veut préciser un fichier à convertir en particulier )


--o ( La commande permettant de choisir la destination du fichier HTML sortant )


--title ( Commande permettant de changer le titre de ses page HTML converties )

