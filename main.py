from tkinter import*
from PIL import Image, ImageTk
import pygame
from pygame import mixer
import os

col0 = "#f0f3f5"
col1 = "#feffff"
col2 = "#3fb5a3"
col3 = "#2e2d2c"
col4 = "#40323d"
col5 = "#4a88e8"

#-------------------------------


janela = Tk()
janela.title("MP3_do_tygas")
janela.geometry("352x255")
janela.configure(width=False, height=False)

#frames---------------------

frame_esquerda = Frame(janela,width=150, height=150,bg=col3)
frame_esquerda.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

frame_direita = Frame(janela,width=250, height=150,bg=col3)
frame_direita.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela,width=404, height=100,bg=col3)
frame_baixo.grid(row=1, column=0, columnspan=3, pady=1, padx=0, sticky=NSEW)

#configurando o frame esquerda

img_1 = Image.open("musica-alt.png")
img_1 = img_1.resize((130,130))
img_1 = ImageTk.PhotoImage(img_1)

l_logo =Label(frame_esquerda, height=130, image=img_1, compound=LEFT, padx=0, anchor='nw', font=('ivy 16 bold'), bg=col3, fg=col3)
l_logo.place(x=7, y=15)

#funcoes ------------------------

def play_musicas():
   rodando = listbox.get(ACTIVE)
   l_rodando['text'] = rodando
   mixer.music.load(rodando)
   mixer.music.play()

def pausar_musica():
   mixer.music.pause()

def continuar_musica():
   mixer.music.unpause()

def parar_musica():
   mixer.music.stop()

def proxima_musica():
   tocando = l_rodando['text']
   index = musicas.index(tocando)
   novo_index = index + 1
   tocando = musicas[novo_index]
   mixer.music.load(tocando)
   mixer.music.play()
   listbox.delete(0,END)
   mostrar()
   listbox.select_set(novo_index)
   listbox.config(selectmode=SINGLE)
   l_rodando['text']=tocando

def anterior_musica():
   tocando = l_rodando['text']
   index = musicas.index(tocando)
   novo_index = index - 1
   tocando = musicas[novo_index]
   mixer.music.load(tocando)
   mixer.music.play()
   listbox.delete(0,END)
   mostrar()
   listbox.select_set(novo_index)
   listbox.config(selectmode=SINGLE)
   l_rodando['text']=tocando

#frame direita---------------------------


listbox = Listbox(frame_direita, width=22, height=10, selectmode=SINGLE, font=('ariel 9 bold'), bg=col3, fg=col1 )
listbox.grid(row=0, column=0)

s = Scrollbar(frame_direita)
s.grid(row=0, column=1, sticky=NSEW)

listbox.configure(yscrollcommand=s.set)
s.configure(command=listbox.yview)

#frame baixo----------

l_rodando =Label(frame_baixo, text = "escolha musica na lista", width=44, justify=LEFT, anchor='nw', font=('ivy 10'), bg=col1, fg=col4)
l_rodando.place(x=0, y=1)


img_2 = Image.open("angulo-duplo-esquerdo.png")
img_2 = img_2.resize((30,30))
img_2 = ImageTk.PhotoImage(img_2)
b_anterior =Button(frame_baixo, command=anterior_musica,width=40, height=40,image=img_2, font=('ivy 10 bold'), relief=RAISED, overrelief=RAISED, bg=col3, fg=col4)
b_anterior.place(x=38, y=35)

img_3 = Image.open("jogar.png")
img_3 = img_3.resize((30,30))
img_3 = ImageTk.PhotoImage(img_3)
b_play =Button(frame_baixo, command=play_musicas, width=40, height=40,image=img_3, font=('ivy 10 bold'), relief=RAISED, overrelief=RAISED, bg=col3, fg=col4)
b_play.place(x=84, y=35)

img_4 = Image.open("angulo-duplo-pequeno-direito.png")
img_4 = img_4.resize((30,30))
img_4 = ImageTk.PhotoImage(img_4)
b_proxima =Button(frame_baixo, command=proxima_musica, width=40, height=40,image=img_4, font=('ivy 10 bold'), relief=RAISED, overrelief=RAISED, bg=col3, fg=col4)
b_proxima.place(x=130, y=35)

img_5 = Image.open("pausa.png")
img_5 = img_5.resize((30,30))
img_5 = ImageTk.PhotoImage(img_5)
b_pausa =Button(frame_baixo, command=pausar_musica, width=40, height=40,image=img_5, font=('ivy 10 bold'), relief=RAISED, overrelief=RAISED, bg=col3, fg=col4)
b_pausa.place(x=176, y=35)

img_6 = Image.open("angulo-direito.png")
img_6 = img_6.resize((30,30))
img_6 = ImageTk.PhotoImage(img_6)
b_continua =Button(frame_baixo, command=continuar_musica, width=40, height=40,image=img_6, font=('ivy 10 bold'), relief=RAISED, overrelief=RAISED, bg=col3, fg=col4)
b_continua.place(x=222, y=35)

img_7 = Image.open("pare.png")
img_7 = img_7.resize((30,30))
img_7 = ImageTk.PhotoImage(img_7)
b_pare =Button(frame_baixo, command=parar_musica, width=40, height=40,image=img_7, font=('ivy 10 bold'), relief=RAISED, overrelief=RAISED, bg=col3, fg=col4)
b_pare.place(x=268, y=35)


os.chdir(r'C:\Users\User\PycharmProjects\ MP3player\musicas')
musicas = os.listdir()

def mostrar():
   for i in musicas:
      listbox.insert(END, i)
mostrar()

mixer.init()  #iniciando mixer

janela.mainloop()




