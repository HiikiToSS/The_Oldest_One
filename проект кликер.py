from tkinter import *
from tkinter import messagebox


f1 = open('scoreX.txt', 'r')
scoreX = int(f1.read())
f1.close()
f2 = open('score.txt', 'r')
score = int(f2.read())
f2.close()

def reWrite():
    f = open("score.txt", "w")
    d = str(score)
    f.write(d)
    f.close()
    m = open('scoreX.txt', 'w')
    s = str(scoreX)
    m.write(s)
    m.close()

def reCommand():
    f = open("score.txt", "w")
    d = str(0)
    f.write(d)
    f.close()
    m = open('scoreX.txt', 'w')
    s = str(1)
    m.write(s)
    m.close()

def multChange(d, price):
    global score
    global scoreX
    if score >= price:
        score -= price
        scoreX = 1
        scoreX *= d
        reWrite()
    else:
        messagebox.showinfo(message = 'Не достаточно очков')


def shopWindow(prev1):
    global scoreX
    prev1.destroy()
    w2=Tk()
    w2.geometry('600x600')
    goGame1 = Button(w2, text='Play', font = "Arial 19", command = lambda: gameWindow(w2))
    goGame1.pack()
    xPrice = [50,150,350,600]
    xList = ['x2 стоит 50','x3 стоит 150','x4 стоит 350','x5 стоит 600']
    for i in range(len(xPrice)):
        x = Button(w2, text = xList[i], font = "Arial 17", command = lambda i=i: multChange(i + 2, xPrice[i]))
        x.pack()
    reButton1 = Button(w2, text = 'Сброс', command = reCommand)
    reButton1.pack()
    w2.mainloop()

def gameWindow(prev2):
    global score
    global scoreX
    def scorePlus():
        global score
        global scoreX
        score += scoreX
        scoreLbl["text"] = score
        reWrite()

    prev2.destroy()
    w3 = Tk()
    w3.geometry('600x600')

    gamelbl = Label(w3, text = 'Clicker game', font = "Arial 20")
    gamelbl.pack()
    goGame3 = Button(w3, text = 'Shop', command = lambda: shopWindow(w3), font = "Arial 19")
    goGame3.pack()
    scoreLbl = Label(w3, text = str(score), font = "Arial 20")
    scoreLbl.pack()
    click = Button(w3, text = 'click me!', font = "Arial 25", command = scorePlus)
    click.pack()
    reButton2 = Button(w3, text = 'Сброс', command = reCommand)
    reButton2.pack()
    w3.mainloop()

def homeWindow():
    w1=Tk()
    w1.geometry('600x600')
    homeWind = Label(w1, text = 'Home Page', font = "Arial 20")
    homeWind.pack()
    butShop = Button(w1, text = 'Shop', font = "Arial 19", command = lambda : shopWindow(w1))
    butShop.pack()
    goGame2 = Button(w1, text='Play', font = "Arial 19", command = lambda: gameWindow(w1))
    goGame2.pack()
    w1.mainloop()

homeWindow()