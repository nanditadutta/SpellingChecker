from tkinter import * #install tkinter --> pip install tk
from textblob import TextBlob #install this library using pip install textblob
def check_spelling():
    print (type(spell_check.get()))
    print(spell_check.get())
    
    a = TextBlob(spell_check.get())
    print(type(a))
    print(a.correct())
    spell = Label(window,text = "The correct spelling is :" , font =("Andale Mono",25,"italic"),bg = "brown")
    spell.pack()
    correct_text = Label(window, text = str(a.correct()),font =("Andale Mono",35,"italic"),bg = "blue")
    correct_text.pack()

window =Tk()
window.title("My Spelling Checker")
window.geometry("800x600")
window.config(background ="purple")
text_heading = Label(window,text="Spelling Checker(Check your spellings!!)", font = ("Andale Mono",30,"italic"),bg = "black", fg ="Blue")
text_heading.pack()


text_check=Label(window, text="Enter the spelling", font=("Andale Mono",20,"italic"),bg = "black", fg ="orange")
text_check.pack()
spell_check = Entry(window, font = ("Andale Mono", 35,"bold"),width =500, bg ="white")
spell_check.pack()
Check_button = Button(window, text ="Check!!" , font = ("Andale Mono",30, "bold"),fg = "red" ,bg = "black", command=check_spelling)
Check_button.pack() 

window.mainloop()

                                
                                # code is contributed by Nandita Dutta....#
