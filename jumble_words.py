from tkinter import *
from tkinter import messagebox
import random 

answers = ["apple","mango","banana",'achieve','kolkata','evening','servant','receiver','london','ferrari','hollow','horror','master','morning','bottle','pen','router','copy','narrow','wide','dive','love','block','right','simple','deaf','single','knight','hope']
words = ["papel", "ganmo", "naanba", "caheiev", "kkaalot", "eevngin", "vsntare", "eecrierv", "onlond", "rrraief", "lowhol", "rrrooh", "tremas", "nromnig", "tolteb", "enp","outrer", "pyoc", "arwonr", "diew", "ived", "vole", "colbk", "ghtri", "misple", "eafd", "nisleg", "ghtnik", "peoh"]
random_number = random.randrange(0, len(words), 1)
attempt = 0 
score = ""
count = 0

def reset():
    global answers, words, random_number
    random_number = random.randrange(0, len(words), 1)
    jumbled_word.config(text = words[random_number])
    input.delete(0, END)

def default():
    global answers, words, random_number
    jumbled_word.config(text = words[random_number])

def check_answer():
    global score, count, attempt, random_number, words, answers
    attempt = int(attempt)+1
    user_answer = ans.get()
    if user_answer == answers[random_number]:
        count = int(count)+1
        messagebox.showinfo("Correct", "Correct Answer!")
    else:
        messagebox.showwarning("Wrong", "You got it wrong.")
    reset()
    score = "Score: "+str(count)+"/"+str(attempt)
    score_label.config(text = score)

window = Tk()
window.geometry("260x320")
window.configure(background = "black")

ans = StringVar()

title = Label(window, text = "Jumbled word game", bg = "black", fg = "white", font = ("times", 30))
jumbled_word = Label(window, text = "", bg = "black", fg = "white", font = ("times", 20))
input = Entry(window, width = 20, textvariable = ans)
check_button = Button(window, text = "Check", font = ("times", 20), command = check_answer)
reset_button = Button(window, text = "Reset", font = ("times", 20), command = reset)
score_label = Label(window, text = "", bg = "black", fg = "white", font = ("times", 20))

title.pack()
jumbled_word.pack(pady = 20)
input.pack()
check_button.pack(pady = 20)
reset_button.pack()
score_label.pack(pady = 20)

default()
window.mainloop()