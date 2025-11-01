import tkinter as tk
from tkinter import ttk
import string
class Caesar:
    def __init__(self, phrase, number):
        self.p = phrase
        self.n = int(number)
        self.l = [chr(n) for n in range(945, 970) if n != 962]  # λίστα που περιέχει τα μικρά, άτονα γράμματα της αλφαβήτου
                                                                # η λίστα δημιουργείται με βάση τους αριθμούς των χαρακτήρων
                                                                # σε unicode. Από την λίστα εξαιρείται το 'ς' που βρίσκεται
                                                                # στο λεξικό self.dict_lower
        self.lu = [i.upper() for i in self.l]   # λίστα που περιέχει τα κεφαλαία, άτονα γράμματα της αλφαβήτου.
                                                # # Η λίστα δημιουργείται από την self.l με την χρήση της μεθόδου .upper()
                                                # που μετατρέπει τα μικρά γράμματα σε κεφαλαία.
        self.dict_lower = {'ά': 'α', 'έ': 'ε', 'ό': 'ο', 'ί': 'ι', 'ύ': 'υ', 'ώ': 'ω', 'ή': 'η', 'ς': 'σ'}
        self.dict_upper = {'Ά': 'Α', 'Έ': 'Ε', 'Ί': 'Ι', 'Ύ': 'Υ', 'Ώ': 'Ω', 'Ό': 'Ο', 'Ή': 'Η'}
        self.list_others = [i for i in string.punctuation]  # λίστα που περιέχει σύμβολα, η οποία δημιουργείται
                                                            # από την συμβολοσειρά που επιστρέφει η string.punctuation
        self.list_eng_l = [chr(l) for l in range(97, 123)]  #λίστα που περιλαμβάνει μικρά αγγλικά γράμματα
        self.list_eng_u = [chr(m) for m in range(65, 91)]   #λίστα που περιλαμβάνει κεφαλαία αγγλικά γράμματα
        self.s = []
    def make_list(self):    #μέθοδος που μετατρέπει συμβολοσειρά σε λίστα
        for i in self.p:
            self.s.append(i)
        return self.s

    def cipher(self):    #μέθοδος που πραγματοποιεί την κρυπτογράφηση
        self.clist = []  # λίστα με τα κρυπτογραφημένα γράμματα
        self.cindex = []    # λίστα που περιέχει τα indexes των κρυπτογραφημένων γραμμάτων
        for k in self.s:    # εντός αυτής της επανάληψης βρίσκονται οι θέσεις (indexes) των γραμμάτων με βάση τις αρχικές λίστες και
                            # λεξικά που ορίζονται στην __init__
            if k == ' ':
                index = ' '
            elif k in self.dict_lower.keys():
                k = self.dict_lower[k]
                index = self.l.index(k)
            elif k in self.dict_upper.keys():
                k = self.dict_upper[k]
                index = self.lu.index(k)
            elif k in self.l: 
                index = self.l.index(k)
            elif k in self.lu:
                index = self.lu.index(k)
            elif k in self.list_others:
                index = self.list_others.index(k)
            elif k in self.list_eng_l:
                index = self.list_eng_l.index(k)
            elif k in self.list_eng_u:
                index = self.list_eng_u.index(k)
            else:
                print('Η φράση που δίνεται προς κρυπτογράφηση μπορεί να περιέχει μικρά, κεφαλαία γράμματα, κενά ή/και σύμβολα.')
                break
            self.cindex.append(index)

        for k in self.s:    # εντός αυτής της επανάληψης πραγματοποιείται η εύρεση των κρυπτογραφημένων γραμμάτων
            if k == ' ':
                self.clist.append(k)
            else:
                letter_index = self.cindex[self.s.index(k)]     # βρίσκει την θέση του γράμματος στην συμβολοσειρά self.s και την 
                                                                # χρησιμοποιεί για να βρει το στοιχείο της self.cindex που αντιστοιχεί
                                                                # σ'αυτή τη θέση 
                if k in self.list_eng_u:
                    if (letter_index + self.n) >= 23:
                        new_letter_index = letter_index + self.n - 24
                    else:
                        new_letter_index = letter_index + self.n
                    new_letter = self.list_eng_u[new_letter_index]
                    self.clist.append(new_letter)
                elif k in self.list_eng_l:
                    if (letter_index + self.n) >= 23:
                        new_letter_index = letter_index + self.n - 24
                    else:
                        new_letter_index = letter_index + self.n
                    new_letter = self.list_eng_l[new_letter_index]
                    self.clist.append(new_letter)
                elif k in self.list_others:
                    new_letter = self.list_others[letter_index] 
                    self.clist.append(new_letter)
                elif k.isupper():
                    if (letter_index + self.n) >= 23:
                        new_letter_index = letter_index + self.n - 24
                    else:
                        new_letter_index = letter_index + self.n
                    new_letter = self.lu[new_letter_index] 
                    self.clist.append(new_letter) 
                elif k.islower():
                    if (letter_index + self.n) >= 23:
                        new_letter_index = letter_index + self.n - 24
                    else:
                        new_letter_index = letter_index + self.n
                    new_letter = self.l[new_letter_index]
                    self.clist.append(new_letter)
                else: break
        self.cstring = ''.join(self.clist)    # κρυπτογραφημένη συμβολοσειρά
        return self.cstring

    def decipher(self):    #μέθοδος που πραγματοποιεί την αποκρυπτογράφηση
        self.dlist = []  # λίστα με τα αποκρυπτογραφημένα γράμματα
        self.dindex = []    # λίστα που περιέχει τα indexes των αποκρυπτογραφημένων γραμμάτων
        for k in self.s:    # εντός αυτής της επανάληψης πραγματοποιείται η εύρεση των θέσεων (indexes) των γραμμάτων
                            # με βάση τις αρχικές λίστες και λεξικά που ορίζονται στην __init__
            if k == ' ':
                self.index = ' '
            elif k in self.dict_lower.keys():
                k = self.dict_lower[k]
                index = self.l.index(k)
            elif k in self.dict_upper.keys():
                k = self.dict_upper[k]
                index = self.lu.index(k)
            elif k in self.l: 
                index = self.l.index(k)
            elif k in self.lu:
                index = self.lu.index(k)
            elif k in self.list_others:
                index = self.list_others.index(k)
            elif k in self.list_eng_l:
                index = self.list_eng_l.index(k)
            elif k in self.list_eng_u:
                index = self.list_eng_u.index(k)
            else: 
                print('Η φράση που δίνεται προς αποκρυπτογράφηση μπορεί να περιέχει μικρά, κεφαλαία γράμματα, κενά ή/και σύμβολα.')
                break
            self.dindex.append(index)

        for k in self.s:    # εντός αυτής της επανάληψης πραγματοποιείται η εύρεση των αποκρυπτογραφημένων γραμμάτων
            if k == ' ':
                self.dlist.append(k)
            else:
                letter_index = self.dindex[self.s.index(k)]     # βρίσκει την θέση του γράμματος στην συμβολοσειρά self.s και την χρησιμοποιεί για 
                                                                # να βρει το στοιχείο της self.dindex που αντιστοιχεί σ'αυτή τη θέση 
                if k in self.list_eng_l:
                    new_letter_index = letter_index - self.n
                    new_letter = self.list_eng_l[new_letter_index]
                    self.dlist.append(new_letter)
                elif k in self.list_eng_u:
                    new_letter_index = letter_index - self.n
                    new_letter = self.list_eng_u[new_letter_index]
                    self.dlist.append(new_letter)
                elif k in self.list_others:
                    new_letter_index = letter_index - self.n
                    new_letter = self.list_others[new_letter_index]
                    self.dlist.append(new_letter)
                elif k.islower():
                    new_letter_index = letter_index - self.n
                    new_letter = self.l[new_letter_index]
                    self.dlist.append(new_letter)
                elif k.isupper():
                    new_letter_index = letter_index - self.n
                    new_letter = self.lu[new_letter_index] 
                    self.dlist.append(new_letter)
                else: break
        self.dstring = ''.join(self.dlist)    # αποκρυπτογραφημένη συμβολοσειρά
        return self.dstring

class Ui:#Κλάση για την δημιουργία γραφικών
    def __init__(self,root):
        self.root=root
        self.root.geometry('1000x600')

        self.Frame_one=tk.Frame(root,bg='#1C2530') # Χωρίζεται η εφαρμογή σε 2 Frames , ενα δεξιά και ένα αριστερά.
        self.Frame_one.pack(fill='both',expand=True,side='left')

        self.Frame_two=tk.Frame(root,bg='#1C2530')
        self.Frame_two.pack(fill='both',expand=True,side='right')

        self.Label_one=tk.Label(self.Frame_one,text='Cipher',bg='#1C2530',fg='#F7B661',font='Aerial 30')#Labels με τις επικεγαλίδες
        self.Label_one.pack(side='top',fill='x')

        self.Label_two=tk.Label(self.Frame_two,text='Decipher',bg='#1C2530',fg='#F7B661',
                                font='Aerial 30')
        self.Label_two.pack(side='top',fill='x')

        self.Entry_one=tk.Entry(self.Frame_one,width=50,font='Verdana 10')#4 Entry Boxes όπου τα 2 παίρνουν τα Text και τα άλλα 2 την μετατόπιση
        self.Entry_one.insert(0,'Insert Text')
        self.Entry_one.bind('<FocusIn>',self.EntryoneIn)
        self.Entry_one.bind('<FocusOut>',self.EntryoneOut)
        self.Entry_one.pack(padx=10,pady=10)

        self.Entry_two=tk.Entry(self.Frame_two,width=50,font='Verdana 10')
        self.Entry_two.insert(0,'Insert Text')
        self.Entry_two.bind('<FocusIn>',self.EntrytwoIn)
        self.Entry_two.bind('<FocusOut>',self.EntrytwoOut)
        self.Entry_two.pack(padx=10,pady=10)

        self.entry_one=tk.Entry(self.Frame_one)
        self.entry_one.insert(0,'Insert Movement')
        self.entry_one.bind('<FocusIn>',self.entryoneIn)
        self.entry_one.bind('<FocusOut>',self.entryoneOut)
        self.entry_one.pack(padx=10,pady=10)

        self.entry_two=tk.Entry(self.Frame_two)
        self.entry_two.insert(0,'Insert Movement')
        self.entry_two.bind('<FocusIn>',self.entrytwoIn)
        self.entry_two.bind('<FocusOut>',self.entrytwoOut)
        self.entry_two.pack(padx=10,pady=10)

        self.FrameButtonsLeft=tk.Frame(self.Frame_one,bg='#1C2530')                           #2 frames για να μπουν τα buttons διπλα 
        self.FrameButtonsLeft.pack()

        self.Button_one=tk.Button(self.FrameButtonsLeft,text='Press to cipher',command=self.getcipher)#4 Buttons , 2 για να γίνει η κρυπτογράφιση-αποκρυπρογράφιση...
        self.Button_one.pack(side='left',padx=5)

        self.ButonPasteOne=tk.Button(self.FrameButtonsLeft,text='Paste from clipboard',command=self.clipboardcipher)#...και δύο για να κάνει επικόλληση απο το clipboard στα entry
        self.ButonPasteOne.pack(padx=5)

        self.FrameButtonsRight=tk.Frame(self.Frame_two,bg='#1C2530')
        self.FrameButtonsRight.pack()

        self.Button_two=tk.Button(self.FrameButtonsRight,text='Press to decipher',command=self.getdecipher)
        self.Button_two.pack(padx=5,side='left')

        self.ButtonPasteTwo=tk.Button(self.FrameButtonsRight,text='Paste from clipboard',command=self.clipboarddecipher)
        self.ButtonPasteTwo.pack(padx=5)

        self.Text_one=tk.Text(self.Frame_one,width=60,height=20,bg='black',fg='#90EE90') #Texts που αναγράφεται το κέιμενο πριν και μετα την μετατόπιση
        self.Text_one.pack(pady=20)

        self.Text_two=tk.Text(self.Frame_two,width=60,height=20,bg='black',fg='#90EE90')
        self.Text_two.pack(pady=20)    

        self.Error_One=tk.Label(self.Frame_one,bg='#1C2530',fg='Red',height=4,width=10,font='Verdana 20') #Labels για να κάνει pop την λέξη error όταν κάποιο entry είναι κενό
        self.Error_One.pack()
        self.Error_Two=tk.Label(self.Frame_two,bg='#1C2530',fg='Red',height=4,width=10,font='Verdana 20')
        self.Error_Two.pack()

    def getcipher(self):   #μέθοδος που κάνει την κωδικοποίηση μέσω των γραφικών
        try:
            Entry=str(self.Entry_one.get())
            entry=int(self.entry_one.get())
            c=Caesar(Entry,entry)
            c.make_list()
            f=open('Cipher.txt','a',encoding='utf-8') #Κάθε κωδικποίηση γράφεται σε ένα αρχείο, σαν ιστορικό
            f.write(f'{Entry}==>{c.cipher()}\n')
            f.close()
            self.Text_one.insert(tk.END,f'{Entry}==>{c.cipher()}\n')
            self.Error_One.config(text='')
        except:
            self.ErrorUi_One()
        

    def getdecipher(self):#Μέθοδος που κάνει την αποκωδικοποίηση μέσω των γραφικών
        try:
            Entry=str(self.Entry_two.get())
            entry=int(self.entry_two.get())
            c=Caesar(Entry,entry)
            c.make_list()
            f=open('Decipher.txt','a',encoding='utf-8')#Ομοίως σε άλλο αρχείο γράφει αυτά που αποκωδικοποιήθηκαν
            f.write(f'{Entry}==>{c.decipher()}\n')
            f.close()
            self.Text_two.insert(tk.END,f'{Entry}==>{c.decipher()}\n')
            self.Error_Two.config(text='')
        except:
            self.ErrorUi_Two()


    def EntryoneIn(self,e):                                                 #Οι πρώτοι 8 μέθοδοι δημιουργούν τα Texts πάνω στα Entries και πατηθεί κλίκ μέσα στο καθένα από αυτα...
        if self.Entry_one.get()=='Insert Text':   #1
            self.Entry_one.delete(0,"end")                                  #... αφαιρείται το Text και αν είνα κενό το Entry και πατηθεί click αλλού κάνει reset στην αρχική κατάσταση

    def EntryoneOut(self,e):
        if self.Entry_one.get()=='':
            self.Entry_one.insert(0,'Insert Text') #2

    def EntrytwoIn(self,e):
        if self.Entry_two.get()=='Insert Text':#3
            self.Entry_two.delete(0,"end")

    def EntrytwoOut(self,e):
        if self.Entry_two.get()=='':
            self.Entry_two.insert(0,'Insert Text')#4

    def entryoneIn(self,e):
        if self.entry_one.get()=='Insert Movement':#5
            self.entry_one.delete(0,"end")

    def entryoneOut(self,e):
        if self.entry_one.get()=='':
            self.entry_one.insert(0,'Insert Movement')#6

    def entrytwoIn(self,e):
        if self.entry_two.get()=='Insert Movement':
            self.entry_two.delete(0,"end")#7

    def entrytwoOut(self,e):
        if self.entry_two.get()=='':
            self.entry_two.insert(0,'Insert Movement')#8

    def clipboardcipher(self):
        self.Entry_one.delete(0,"end")
        self.Entry_one.insert(0,self.root.clipboard_get()) #παίρνουν το Text του clipboard 

    def clipboarddecipher(self):
        self.Entry_two.delete(0,"end")
        self.Entry_two.insert(0,self.root.clipboard_get())

    def ErrorUi_One(self):
        self.Error_One.config(text='Error')  #Άν παρουσιαστεί error , αναγράφεται η λεξη error κάτω απο το κάθε text

    def ErrorUi_Two(self):
        self.Error_Two.config(text='Error')
def main():                          #Το main program όπου δημιοργείται το παράθυρο , και κλειδώνει το μέγεθος του.
    root=tk.Tk()
    root.resizable(height = False, width = False) 
    Ui(root)
    root.mainloop()
main()


