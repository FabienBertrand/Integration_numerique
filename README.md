L'objectif de ce programme est d'implémenter 3 méthodes d'intégration numérique (rectangle, trapèze et simpson) pour pouvoir évaluer leur efficacité en terme de précision et de temps d'exécution sur le calcul de
l'intégrale d'un polynome de degrès inférieur ou égale à 3. Ce programme permet aussi d'évaluer les performances d'une même méthode implémenté en en python de base avec une implémentation pré-programmé sur un 
paquet python scientifique comme Numpy ou Scipy. 
Pour évaluer la précision des méthodes, le programme compare les solutions obtenues avec les méthodes d'analyse numérique avec la solution exacte de l'intégration. La complexité est calculé puis tracé en évaluant le 
temps d'execution de la fonction par rapport au nombre d'itération (proportionel au nombre de segment choisis). Les courbes sont ensuite tracées à l'aide du module 'Matplotlib'.
Le programme s'utilise en mode console, l'utilisateur peut choisir différentes options pour comparer les performances des méthodes-entre elles et afficher des graphiques de comparaison.
Pour que le programme s'exécute correctement, il est nécessaire avoir téléchargé les bibliothèques 'Numpy', 'Scipy' et 'Matplotlib'. 
