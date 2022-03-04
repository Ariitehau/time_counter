from module import *
from tkinter import *
toto = True
duration = 0


def start():
    import time
    from datetime import timedelta
    global duration, running_time
    started_time = time.time()
    while toto is True:
        diff = int(time.time() - started_time)
        total = diff + recup()[0]
        duration = timedelta(seconds=total)
        running_time = timedelta(seconds=diff)
        count.set(str(duration))
        runtime.set(str(running_time))
        fenetre.update()


def pause():
    global toto
    toto = False
    ecrire(duration, "w")
    ecrire(running_time, "a")



def resume():
    import time
    from datetime import timedelta
    global toto, duration, running_time
    toto = True
    started_time = time.time()
    while toto is True:
        diff = int(time.time() - started_time) + recup()[1]
        total = diff + recup()[0]
        duration = timedelta(seconds=total)
        running_time = timedelta(seconds=diff)
        count.set(str(duration))
        runtime.set(str(running_time))
        fenetre.update()


def stop():
    global toto, fenetre
    toto = False
    if duration == 0:
        fenetre.quit()
    else:
        ecrire(duration, "w")
        running_time = timedelta(seconds=0)
        ecrire(running_time, "a")
        fenetre.quit()


fenetre = Tk()
fenetre.geometry("287x110")

count = StringVar()
runtime = StringVar()
Label(text="Total", justify='center', width=35).place(x=0, y=0)
Entry(fenetre, text=count, justify='center', width=35).place(x=0, y=20)
Label(text="This session", justify='center', width=35).place(x=0, y=40)
Entry(fenetre, text=runtime, justify='center', width=35).place(x=0, y=60)
count.set(str(timedelta(seconds=recup()[0])))
runtime.set(str(timedelta(seconds=recup()[1])))
Button(fenetre, text='START', command=start).place(x=0, y=80)
Button(fenetre, text='PAUSE', command=pause).place(x=70, y=80)
Button(fenetre, text='RESUME', command=resume).place(x=141, y=80)
Button(fenetre, text='STOP', command=stop).place(x=224, y=80)
fenetre.mainloop()
