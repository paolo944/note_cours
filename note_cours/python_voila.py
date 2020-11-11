from tkinter import *
from tkinter import messagebox
from webbrowser import *
from tkinter.font import *
import smtplib

def mail(dac):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    sender_email = "mon.test.python4@gmail.com"
    rec_email = "paolomekhail4@gmail.com"
    password = "CoucouPython.13122002"
    sujet = "Note cours python"
    if dac:
        message = "Elle/Il a aime le cours ;)"
    else:
        message = "Ce fut un pouce gros rouge"

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sender_email, rec_email, sujet, message)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, rec_email, email_text)
    server.close()
    print("mail envoyé")

#fenetre principale
root = Tk()

root.title("Note cours d'info")
root.iconbitmap("XXX/pouce.ico")
root.geometry("500x400")
root.configure(bg="#32C5EB")

count = 0

def rouge():
    global count
    if count == 0:
        messagebox.showerror("Erreur 404", "Eeeeeeuh essaye le bouton d'à côté pour voir")
        count += 1
    elif count == 1:
        messagebox.showerror("Erreur 404", "Bon, .... \non a dit essaye celui d'à côté")
        count += 1
    elif count >= 2 and count < 4:
        messagebox.showerror("Erreur 404", "Bon tu force Touffik, \nc'était ton dernier cours avec nous, bisous('ou paye pour rester')")
        count += 1
    else:
        root.quit()

    mail(False)

def bleu():
    messagebox.showinfo("GG 404", "Pour te récompenser('et nous récompenser'), voila nos réseaux,\n\n                                 bisous")
    open("https://www.instagram.com/romain_fbn/")
    open("https://www.instagram.com/paolo___lop/")
    open("romain.png")
    open("poula.png")

    mail(True)

font = Font(family="roboto", size=28, underline=True, slant="italic")

titre = Label(root, text="Bonsoir,\nveuillez nous noter", font=font, bg="#32C5EB")
titre.pack
titre.place(anchor=CENTER, relx=0.5, rely=0.2)

pouce_bleu = PhotoImage(file=r"XXX/pouce.PNG")
pouce_rouge = PhotoImage(file=r"XXX/pouce_rouge.PNG")

pouce_bleu_bt = Button(root, image=pouce_bleu, command=bleu, border=0, height=40, width=40)

pouce_rouge_bt = Button(root, image=pouce_rouge, command=rouge, border=0, height=40, width=40)

pouce_bleu_bt.pack()
pouce_rouge_bt.pack()
pouce_bleu_bt.place(anchor=CENTER, relx=0.4, rely=0.5)
pouce_rouge_bt.place(anchor=CENTER, relx=0.6, rely=0.5)


root.mainloop()

