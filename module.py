import time
from datetime import timedelta
from pandas import to_timedelta
toto = True
def ecrire(data, option):
    d = open("/home/arii/coding/PycharmProjects/trials/time_project/time.txt", option)
    data = str(data)
    d.write(data+"\n")
    d.close()

def recup():
    d = open("/home/arii/coding/PycharmProjects/trials/time_project/time.txt", "r")
    j = 0
    dico = dict()
    for i in d:
        dico[j] = to_timedelta(i).total_seconds()
        j += 1
    return dico

