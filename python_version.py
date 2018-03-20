# Faire un import sys
# mettre sys.version_info dans une variable
# afficher le resultat dans une chaine de caractère
# !!! utiliser str() et les acces tableau d'indices dans une liste
import sys

sysv = str(list(sys.version_info))
#detailsys = list(sysvers)
print("La version du système est : " + sysv)

v = sys.version_info
####### version 01 chaine et tableau
vt = str(v[0]) + '.' + str(v[1]) + '.' + str(v[2]) + '.' + str(v[3])
print("La version de python est : " + vt)

####### version 02 chaine et boucle for()
vers = [str(x) for x in v]
version = '.'.join(str(x) for x in v)
print("La version de python est : " + version )
######