from tkinter import *
from googletrans import Translator

def trans():
    text = t.get('1.0', END)
    a = translator.translate(text, dest='en' )
    t2.delete('1.0', END)
    t2.insert('1.0', a.text)
#в цьому модулі я створив вікно перекладачу 
root = Tk()
root.geometry('600x350')
root.title('Перекладач')
root.resizable(width=True, height=True)
root['bg'] = 'black'
translator = Translator()

#Тут я створив модулі вводу тексту + кнопку для перекладу але в майбутніх весіях її не буде 

label = Label(root, fg='white', bg='black',font='Arial 15 bold', text='Введіть текст')
label.place(relx=0.4, y=60, anchor='e' )
t = Text(root, width=23, height=5, font='Arial 12 bold')
t.place(relx=0.5, y=150, anchor='e')

btn = Button(root, width=45, text='Отримати переклад', command=trans)
btn.place(relx=0.5, y=230, anchor=CENTER)

label2 = Label(root, fg='white', bg='black',font='Arial 15 bold', text='Переклад')
label2.place(relx=0.6, y=60, anchor='w')
t2 = Text(root, width=23, height=5, font='Arial 12 bold')
t2.place(relx=0.6, y=150, anchor='w')


root.mainloop()