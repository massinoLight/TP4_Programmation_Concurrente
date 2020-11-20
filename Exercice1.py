import random
import sys
from threading import Thread
import time

class Affichage(Thread):

    """Thread chargé de calculer
     et d'afficher les cubs et les carrées
       dans la console."""

    def __init__(self,calcule):
        Thread.__init__(self)
        self.calcule=calcule


    def __calcul_square__(self,liste):
       for item in liste:
           sys.stdout.write(str(item) +'^2='+str(item**2) + ' ')
           sys.stdout.flush()

    def __calcul_cube__(self,liste):
        for item in liste:
            sys.stdout.write(str(item)+'^3='+str(item ** 3) + ' ')
            sys.stdout.flush()


    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        l = [2, 3, 8, 9,12]
        if self.calcule==1:
           self.__calcul_square__(l)
        else:
            self.__calcul_cube__(l)



start_time = time.time()

# Création des threads
thread_1 = Affichage(1)
thread_2 = Affichage(666)

# Lancement des threads
thread_1.start()
thread_2.start()

"""Si on veut que les threads s attendent
thread_1.join()
thread_2.join()
"""

interval = time.time() - start_time
print()
print ('Temps d execution:', interval )