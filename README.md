# MDtoHTML
Ce projet est sous license publique Mozilla 2.0.

## Comment ca marche ?

C'est très simple, il suffit d'installer le programme et ses addons.

Pour installer les addons, il faut ouvrir un terminal de commande et écrire :

Veillez à modifier FOLDER_PATH par le chemin d'accès du dossier ou vous avez installé le MDtoHTML.

```
cd FOLDER_PATH
pip install -r requirements.txt
```

Pour lancer le convertisseur il suffit de créer un (ou plusieurs fichiers) au format **.MD** dans un dossier quelconque et de lancer le programme dans un terminal.

```
python converter.py
```

Il suffit d'y ajouter des arguments, accessibles via --help à la suite de la commande ci dessus.

* Voici la liste des arguments ici :

  * --dir **OU** --input_directory ( Permet à l'utilisateur de convertir tous les fichiers MD d'un dossier avec une seule commande )


  * --i ( Si l'utilisateur veut préciser un fichier à convertir en particulier )


  * --o **OU** --output_directory ( La commande permettant de choisir la destination du fichier HTML sortant )


  * --title ( Commande permettant de changer le titre de ses page HTML converties )

## Librairie communautaire

Vous pouvez retrouver le package en tapant cette commande afin de l'utiliser dans d'autres projets :

```
pip install mdtohtml-cst
```