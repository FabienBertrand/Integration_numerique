import timeit

import numpy as np
import matplotlib.pyplot as plt
from fonctions import *

#Partie méthode des rectangles
polynome=[float(input("X0")),float(input("X1")),float(input("X2")),float(input("X3"))]
interval=[float(input("borne intégration inférieur")),float(input("borne intégration supérieur"))]
nb_segment=int(input("nombre de segment pour l intégration avec méthode des rectangle"))
print(f"l'intégration analytrique nous donne {integrer_analytique(polynome,interval)}")
print(f"l'intégration avec la méthode des rectangles nous donne {integrer_methode_rectangle(polynome,nb_segment,interval)}")
print(f"l'erreur d'intégration est donc {calculer_erreur_integartion(polynome,nb_segment,interval, integrer_methode_rectangle)*100} % ")
print(f"Le temps d'exécussion est{timeit.timeit(lambda :integrer_methode_trapeze_numpy(polynome, nb_segment, interval), number=1000)/1000} secondes")