# Intégration numérique

L'objectif de ce programme est de comparer 3 méthodes d'intégration numérique (rectangle, trapèze et simpson) pour pouvoir évaluer leur efficacité en terme de précision et de temps d'exécution sur le calcul d'une
l'intégrale d'un polynôme de degré inférieur ou égale à 3. 

Ce programme permet aussi d'évaluer les performances d'une même méthode implémentée en python de base, vectorisée ou avec une implémentation pré-programmée sur un paquet python scientifique comme 'Numpy' ou 'Scipy'. Et dans un second temps de comparer les différentes méthodes entre-elles.

Pour évaluer la précision des méthodes, le programme compare les solutions obtenues à l'aide des méthodes d'analyse numérique avec la solution exacte de l'intégration. La complexité est calculée à l'aide d'un timer en évaluant le temps d'execution de la fonction par rapport au nombre d'itération (proportionel au nombre de segment choisis). Les courbes sont ensuite tracées à l'aide du module 'Matplotlib'.

Le programme s'utilise en mode console, l'utilisateur peut choisir les coefficients du polynôme à intégrer, le programme renvoie ensuite les résultats des calculs et affiche différents graphiques, dans un premier temps, les courbes de convergences et de temps d'exécution entre les implémentations en python de base, vectorisées et pré-programmées pour chacune des méthodes. Ensuite, le programme renvoie deux graphiques pour comparer la perfomance des méthodes entre-elles en terme de temps d'exécution et de précision (valeur de l'erreur).

Pour que le programme s'exécute correctement, il est nécessaire avoir téléchargé les bibliothèques 'Numpy', 'Scipy', 'Matplotlib' ainsi que le module 'Time' nécessaire au calcul du temps d'execution. 
