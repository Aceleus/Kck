import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag
import pandas as pd

t=np.linspace(0,3797.200*37.97)

prob=200

dane= pd.read_csv(r"C:\Users\Szefcu\desktop\KCKFQ.csv", delimiter=',', engine='python')

sygnal=dane["kol2"]

zmiennaA=dane['kol6']

filtr1= ag.pasmowozaporowy(sygnal, prob, 49, 51)

filtr2=ag.pasmowoprzepustowy(filtr1, prob, 1, 50)



for i in range(len(filtr2)):
    if filtr2[i]>0.2:
        print(zmiennaA[i])
