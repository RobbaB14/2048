from tkinter import *
from random import *

class Polje:
    #polje ima svojo vrednost
    def __init__(self, val=0):
        self.vrednost = val
        

class Plosca:
    #plosca je sestavljena iz 16 polj (4 x 4 tabela)
    def __init__ (self):
        self.povrsina =[[Polje() for i in range(4)] for i in range(4)]
        
        #Ko zacnemo igro se dvakrat klice funkcija ustvari
        self.ustvari()
        self.ustvari()
            
    def odpri (self):
        # ko odpiramo shranjeno datoteko
        ime = filedialog.askopenfilename()
        if ime == "":
            return
        with open(ime)as datoteka:
            j = 0
            for vrstica in datoteka:
                nums = vrstica.split(',')
                for i in range(4):
                    self.povrsina[j][i].vrednost = int(nums[i])
                j += 1
            
    #nakljucno izbere polje in vanj postavi 2(75%) ali 4(25%)  
    def ustvari(self):
        prazna = self.prazna_polja()
        for i in range(4):
            for j in range(4):
                if self.povrsina[i][j].vrednost == 0:
                    a = randint(0, 99)
                    verjetnost = 100/prazna #klice spodnjo funkcijo
                    if verjetnost > a:
                        b = randint(0, 99)
                        if b < 25:
                            self.povrsina[i][j].vrednost = 4
                            return
                        else:
                            self.povrsina[i][j].vrednost = 2
                            return
                    else:
                        prazna -= 1

    #presteje prazna polja
    def prazna_polja(self):
        n = 0
        for i in range(4):
            for j in range(4):
                if self.povrsina[i][j].vrednost == 0:
                    n += 1
        return n

    #shrani pozicijo in vrednost polj
    def shrani(self):
        ime = filedialog.asksaveasfilename()
        if ime == "":  
            return
        with open(ime, "wt", encoding="utf8") as save_file:
            vsebina =  ""
            for i in range(4):
                vrstica = ""
                for j in range(4):
                    if j != 3:
                        vrstica += str(self.povrsina[i][j].vrednost) + ","
                    else:
                        vrstica += str(self.povrsina[i][j].vrednost)
                if i != 3:
                    vsebina += vrstica + "\n"
                else:
                    vsebina += vrstica
            print(vsebina)
            save_file.write(vsebina)

    #premiki:
    def premik_levo(self):
        uspesnost = False #uspesnost je potrebno definirati zato, da program ne bo, ko bo poteza nemogoca vseeno ustvaril novo polje.
        ze_sesteti = [] #seznam v katerega bomo dodajali (i,j) ze sestetih polj. To je potrebno, da funkcija v eni potezi ne sesteje istih polj dvakrat
        for i in range(4):
            for j in range(1, 4):#gledamo 2., 3. in 4. stolpec in jih primerjamo z levim sosedom
                for k in range (1,j+1):
                    if self.povrsina[i][j-k].vrednost == 0 and self.povrsina[i][j-k+1].vrednost != 0:#ce ima na levi niclo, se vrednost premakne (ce ni 0)
                        self.povrsina[i][j-k].vrednost = self.povrsina[i][j-k+1].vrednost
                        self.povrsina[i][j-k+1].vrednost = 0
                        uspesnost = True
                    #ce je vrednost na levi enaka in se ni bila sesteta polji sestejemo (ce nista enaki 0)
                    elif self.povrsina[i][j-k].vrednost == self.povrsina[i][j-k+1].vrednost and (i, j-k) not in ze_sesteti and self.povrsina[i][j-k].vrednost != 0:
                        self.povrsina[i][j-k].vrednost = self.povrsina[i][j-k].vrednost + self.povrsina[i][j-k+1].vrednost
                        ze_sesteti.append((i, j-k))
                        self.povrsina[i][j-k+1].vrednost = 0
                        uspesnost = True
                        break
                    else:
                        break
        return uspesnost
                    
    def premik_desno(self):
        uspesnost = False
        ze_sesteti = []
        for i in range(4):
            for j in range(1, 4):
                for k in range (1,j+1):
                    if self.povrsina[i][3-j+k].vrednost == 0 and self.povrsina[i][3-j+k-1].vrednost != 0:
                        self.povrsina[i][3-j+k].vrednost = self.povrsina[i][3-j+k-1].vrednost
                        self.povrsina[i][3-j+k-1].vrednost = 0
                        uspesnost = True 
                    elif self.povrsina[i][3-j+k].vrednost == self.povrsina[i][3-j+k-1].vrednost and (i, 3-j+k) not in ze_sesteti and self.povrsina[i][3-j+k].vrednost != 0:
                        self.povrsina[i][3-j+k].vrednost = self.povrsina[i][3-j+k].vrednost + self.povrsina[i][3-j+k-1].vrednost
                        ze_sesteti.append((i, 3-j+k))
                        self.povrsina[i][3-j+k-1].vrednost = 0
                        uspesnost = True
                        break
                    else:
                        break
        return uspesnost

    def premik_dol(self):
        uspesnost = False
        ze_sesteti = []
        for i in range(1,4):
            for j in range(4):
                for k in range (1,i+1):
                    if self.povrsina[3-i+k][j].vrednost == 0 and self.povrsina[3-i+k-1][j].vrednost != 0:
                        self.povrsina[3-i+k][j].vrednost = self.povrsina[3-i+k-1][j].vrednost
                        self.povrsina[3-i+k-1][j].vrednost = 0
                        uspesnost = True 
                    elif self.povrsina[3-i+k][j].vrednost == self.povrsina[3-i+k-1][j].vrednost and (3-i+k, j) not in ze_sesteti and self.povrsina[3-i+k][j].vrednost != 0:
                        self.povrsina[3-i+k][j].vrednost = self.povrsina[3-i+k][j].vrednost + self.povrsina[3-i+k-1][j].vrednost
                        ze_sesteti.append((3-i+k, j))
                        self.povrsina[3-i+k-1][j].vrednost = 0
                        uspesnost = True
                        break
                    else:
                        break
        return uspesnost

    def premik_gor(self):
        uspesnost = False
        ze_sesteti = []
        for i in range(1, 4):
            for j in range(4):
                for k in range (1,i+1):
                    if self.povrsina[i-k][j].vrednost == 0 and self.povrsina[i-k+1][j].vrednost != 0:
                        self.povrsina[i-k][j].vrednost = self.povrsina[i-k+1][j].vrednost
                        self.povrsina[i-k+1][j].vrednost = 0
                        uspesnost = True 
                    elif self.povrsina[i-k][j].vrednost == self.povrsina[i-k+1][j].vrednost and (i-k, j) not in ze_sesteti and self.povrsina[i-k][j].vrednost != 0:
                        self.povrsina[i-k][j].vrednost = self.povrsina[i-k][j].vrednost + self.povrsina[i-k+1][j].vrednost
                        ze_sesteti.append((i-k, j))
                        self.povrsina[i-k+1][j].vrednost = 0
                        uspesnost = True
                        break
                    else:
                        break
        return uspesnost

    #po vsaki potezi bomo zagnali funkcijo, ki bo preverila ali je igre konec ( ali smo zmagali ali izgubili), ali lahko igramo naprej
    def konec_igre(self):
        if self.prazna_polja() == 0:
            for i in range(4):
                for j in range(1, 3):
                    if self.povrsina[i][j].vrednost == self.povrsina[i][j+1].vrednost or self.povrsina[i][j].vrednost == self.povrsina[i][j-1].vrednost:
                        return(2) # lahko nadaljujemo
            for i in range (1, 3):
                for j in range(4):
                    if self.povrsina[i][j].vrednost == self.povrsina[i+1][j].vrednost or self.povrsina[i][j].vrednost == self.povrsina[i-1][j].vrednost:
                        return(2) # lahko nadaljujemo
            
            return (0) # izgubili smo

        for i in range(4):
            for j in range (4):
                if self.povrsina[i][j].vrednost >= 2048:
                    return (1) #zmaga

    
    #ko bomo zagnali novo igro, moramo izbrisati vsa polja in ustvariti dve novi polji
    def nova_igra(self):
        for i in range(4):
            for j in range (4):
                self.povrsina[i][j].vrednost = 0
        self.ustvari()
        self.ustvari()
                
#
class Okno(Tk):
    def __init__(self):
        Tk.__init__(self)
        #ustvarimo naso plosco iz razreda Plosca
        self.nasa_plosca = Plosca()
        #ustvarimo igralno povrsino, ki je tabela velikosti (4x4)
        self.igralna_povrsina = Tabela(self, 4, 4)
        self.igralna_povrsina.grid(row = 2, column = 0, columnspan=3)
        self.igralna_povrsina.posodobi(self.nasa_plosca.povrsina)
        
        #gumbi na vrhi okna:
        gumb_shrani = Button (text = "SHRANI", command = self.nasa_plosca.shrani)  
        gumb_shrani.grid(row = 0, column = 0)
        gumb_igraj = Button (text = "NOVA IGRA", command = self.ustvari)
        gumb_igraj.grid(row = 0, column = 1)
        gumb_odpri = Button (text = "ODPRI", command = self.odpri)
        gumb_odpri.grid(row = 0, column = 2)

        #med gumbi in tabelo ustvarimo prazno vrstico, v katero se bo ob zmagi ali porazu izpisal napis.
        self.prazna_vrstica = Label(self, text = '', borderwidth = 20, width = 5, bg = 'gray94')
        self.prazna_vrstica.grid(row = 1, column = 0, columnspan = 3)
        
        #naredimo ukaze za delovanje tipk:
        self.bind('<Left>', self.leva_tipka)
        self.bind('<Right>', self.desna_tipka)
        self.bind('<Up>', self.tipka_gor)
        self.bind('<Down>', self.tipka_dol)

        #definicija, ki se klice ob pritisku na gumb odpri:
    def odpri(self):
        self.nasa_plosca.odpri()
        self.igralna_povrsina.posodobi(self.nasa_plosca.povrsina)#ce igralne povrsine ne posodobimo, se nam pojavi z zamikom ene poteze
        self.prazna_vrstica.configure(text = '', bg = 'gray94')
        
        #definicija, ki se klice ob pritisku na gumb NOVA IGRA
    def ustvari(self):
        self.nasa_plosca.nova_igra()
        self.igralna_povrsina.posodobi(self.nasa_plosca.povrsina)
        self.prazna_vrstica.configure(text = '', bg = 'gray94')
        
        #definicije za premik iz razreda Plosca damo v nove funkcije, ki se bodo klicale ob kliku na tipke
    def leva_tipka(self, event):
        if self.nasa_plosca.premik_levo():
            self.nasa_plosca.ustvari()
            self.igralna_povrsina.posodobi(self.nasa_plosca.povrsina)
            self.izpisi()

    def desna_tipka(self, event):
        if self.nasa_plosca.premik_desno():
            self.nasa_plosca.ustvari()
            self.igralna_povrsina.posodobi(self.nasa_plosca.povrsina)
            self.izpisi()

    def tipka_gor(self, event):
        if self.nasa_plosca.premik_gor():
            self.nasa_plosca.ustvari()
            self.igralna_povrsina.posodobi(self.nasa_plosca.povrsina)
            self.izpisi()

    def tipka_dol(self, event):
        if self.nasa_plosca.premik_dol():
            self.nasa_plosca.ustvari()
            self.igralna_povrsina.posodobi(self.nasa_plosca.povrsina)
            self.izpisi()

    #konec_igre iz Plosce zvezemo v novo funkcijo, ki se bo klicala ob vsakem kliku in izpisovala napise (ce bo potrebno)     
    def izpisi(self):
        konec = self.nasa_plosca.konec_igre()
        if konec == 1:
            self.prazna_vrstica.configure(text = 'ZMAGAL SI :)', bg = 'yellow')

        elif konec == 0:
            self.prazna_vrstica.configure(text = 'KONEC IGRE', bg = 'red')    
                      

# ustvarimo razred Tabele ( ki jo klicemo v razredu okno)
class Tabela(Frame):
    def __init__(self, parent, rows = 10, columns = 2):
        Frame.__init__(self, parent, background = "black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                label = Label(self, text = 0, borderwidth = 20, width = 2, font = ("Helvetica", 16) )
                label.grid(row = row, column = column, sticky = "nsew", padx = 2, pady = 2)#padx, pady = debelina crnih robov
                current_row.append(label)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

    #igra je mnogo bolj pregledna, ce ima vsaka vrednst poja svojo barvo, zato barvo polja nastavimo glede na vrednost polja
    def set(self, row, column, value):
        widget = self._widgets[row][column]
        if value == '':
            a = 'White'
        elif value == '2':
            a = 'khaki1'
        elif value == '4':
            a =  'yellow'
        elif value == '8':
            a = 'gold'
        elif value == '16':
            a = 'dark orange'
        elif value == '32':
            a = 'orange red'
        elif value == '64':
            a = 'VioletRed3'
        elif value == '128':
            a = 'VioletRed2'
        elif value == '256':
            a = 'magenta3'
        elif value == '512':
            a = 'purple1'
        elif value == '1024':
            a = 'SlateBlue2'
        elif value == '2048':
            a = 'turquoise3'
        else:
            a = 'SeaGreen3'
        widget.configure(text = value, bg = a)
           
        
   # funkcija s katero se posodablja tabela     
    def posodobi(self, stanje):
        for i in range (4):
            for j in range (4):
                vrednost = stanje[i][j].vrednost
                if vrednost == 0:
                    vrednost = ""
                else:
                    vrednost = str(vrednost)
                self.set(i, j, vrednost)

nase_okno = Okno()
nase_okno.mainloop()
