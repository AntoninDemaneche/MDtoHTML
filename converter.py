import markdown2
import os
import click

@click.command()
@click.option("--i", default = 'index.md', help = "Fichier markdown à préciser")
@click.option("--o", default = 'result', help = "Dossier ou le HTML va se créer")


def converter(i,o):
    input_fichier = open(i, mode='r', encoding="utf-8")
    fichier = input_fichier.read()
    html = markdown2.markdown(fichier)

    input_title = i
    title_name,extension_null = input_title.split('.md')
    print(title_name)

    output = o
    output_fichier = o + "\ " + title_name + ".html"

    if os.path.exists(output):
        output_fichier2 = open(output_fichier, "w+", encoding="utf-8")
        output_fichier2.write('<!DOCTYPE html>\n<html>\n<head>\n<title></title>\n</head>\n<body>\n' + html + '</body>\n</html>')
        output_fichier2.close
        print('Le convert a bien fonctionné')
    else:
        os.makedirs(output)
        output_fichier2 = open(output_fichier, "w+", encoding="utf-8")
        output_fichier2.write('<!DOCTYPE html>\n<html>\n<head>\n<title></title>\n</head>\n<body>\n' + html + '</body>\n</html>')
        output_fichier2.close
        print("Le convert a bien fonctionné même si le dossier n'existait pas")

if __name__ == '__main__':
    converter()