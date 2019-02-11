import markdown2
import os
import click

@click.command()
@click.option("--dir","--input_directory", default = '', help = "Dossier ou sont les fichiers à convertir")
@click.option("--i", default = '', help = "Fichier markdown à préciser")
@click.option("--o","--output_directory", default = 'result', help = "Dossier ou le HTML va se créer")
@click.option("--title", default = 'Site Statique', help = "Titre de la page ou le HTML va se créer")

def converter(dir,i,o,title):
    if dir == '' and i == '':
        print('Hum ? As-tu compris le principe du programme ?')
        print('Tu devrais taper --help au lancement du programme pour voir la liste des commandes.')

    if dir != '' :
        files = [f for f in os.listdir(dir) if os.path.isfile(f)]
        for str in files:
                if '.md' in str:
                    title_name,extension_null = str.split('.md')
                    # print(title_name)
                    input_fichier = open(str, mode='r', encoding="utf-8")
                    output_fichier = o + "\ " + title_name + ".html"
                    output_fichier2 = input_fichier.read()
                    html = markdown2.markdown(output_fichier2)
                    if os.path.exists(o):
                        output_fichier2 = open(output_fichier, "w+", encoding="utf-8")
                        output_fichier2.write('<!DOCTYPE html>\n<html>\n<head>\n<title>' + title +'</title>\n</head>\n<body>\n' + html + '</body>\n</html>')
                        output_fichier2.close
                        print('Le convert a bien fonctionné.')
                    else:
                        os.makedirs(o)
                        output_fichier2 = open(output_fichier, "w+", encoding="utf-8")
                        output_fichier2.write('<!DOCTYPE html>\n<html>\n<head>\n<title>' + title +'</title>\n</head>\n<body>\n' + html + '</body>\n</html>')
                        output_fichier2.close
                        print("Le convert a bien fonctionné même si le dossier n'existait pas.")
                    
    if i != '':
        input_fichier = open(i, mode='r', encoding="utf-8")
        fichier = input_fichier.read()
        html = markdown2.markdown(fichier)
        input_title = i
        title_name,extension_null = input_title.split('.md')

        output_fichier = o + "\ " + title_name + ".html"

        if os.path.exists(o):
            output_fichier2 = open(output_fichier, "w+", encoding="utf-8")
            output_fichier2.write('<!DOCTYPE html>\n<html>\n<head>\n<title>' + title +'</title>\n</head>\n<body>\n' + html + '</body>\n</html>')
            output_fichier2.close
            print('Le convert a bien fonctionné.')
        else:
            os.makedirs(o)
            output_fichier2 = open(output_fichier, "w+", encoding="utf-8")
            output_fichier2.write('<!DOCTYPE html>\n<html>\n<head>\n<title>' + title +'</title>\n</head>\n<body>\n' + html + '</body>\n</html>')
            output_fichier2.close
            print("Le convert a bien fonctionné même si le dossier n'existait pas.")
 

if __name__ == '__main__':
    converter()