
from colorama import init
from colorama import Fore, Back, Style
from tkinter import *
from PIL import ImageTk,Image

root = Tk()

init()

print( Back.CYAN )
print("Выберите любое число от 1 до 7")
a=str(input())

if ((a=="1") or (a=="2") or (a=="3") or (a=="4") or (a=="5") or (a=="6") or (a=="7")):
 if(a=="1"):
  canvas=Canvas(root,width=1800,height=1500)
  image=ImageTk.PhotoImage(Image.open("C:\\Users\\Asus\\OneDrive\\Изображения\\Снимки экрана\\programmist_st1.jpg"))
  canvas.create_image(0,0,anchor=NW,image=image)
  canvas.pack()
  v=input()
 elif(a=="2"):
  canvas=Canvas(root,width=1800,height=1500)
  image=ImageTk.PhotoImage(Image.open("C:\\Users\\Asus\\OneDrive\\Изображения\\Снимки экрана\\стэтхэм.jpg"))
  canvas.create_image(0,0,anchor=NW,image=image)
  canvas.pack()
  v=input()
 elif(a=="3"):
  canvas=Canvas(root,width=1800,height=1500)
  image=ImageTk.PhotoImage(Image.open("C:\\Users\\Asus\\OneDrive\\Изображения\\Снимки экрана\\Нуб.jpg"))
  canvas.create_image(0,0,anchor=NW,image=image)
  canvas.pack()
  v=input()
 elif(a=="4"):
  canvas=Canvas(root,width=1800,height=1500)
  image=ImageTk.PhotoImage(Image.open("C:\\Users\\Asus\\OneDrive\\Изображения\\Снимки экрана\\качок.jpg"))
  canvas.create_image(0,0,anchor=NW,image=image)
  canvas.pack()
  v=input()
 elif(a=="5"):
  canvas=Canvas(root,width=1800,height=1500)
  image=ImageTk.PhotoImage(Image.open("C:\\Users\\Asus\\OneDrive\\Изображения\\Снимки экрана\\богач.jpg"))
  canvas.create_image(0,0,anchor=NW,image=image)
  canvas.pack()
  v=input()
 elif(a=="6"):
  canvas=Canvas(root,width=1800,height=1500)
  image=ImageTk.PhotoImage(Image.open("C:\\Users\\Asus\\OneDrive\\Изображения\\Снимки экрана\\красавчик.jpg"))
  canvas.create_image(0,0,anchor=NW,image=image)
  canvas.pack()
  v=input()
 elif(a=="7"):
  canvas=Canvas(root,width=1800,height=1500)
  image=ImageTk.PhotoImage(Image.open("C:\\Users\\Asus\\OneDrive\\Изображения\\Снимки экрана\\Месси.jpg"))
  canvas.create_image(0,0,anchor=NW,image=image)
  canvas.pack()
  v=input()
else:
	print("Выбирай число только от 1 до 7 :)")





