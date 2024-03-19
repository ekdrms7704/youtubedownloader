from tkinter import *
from pytube import YouTube
import requests
import os

root = Tk()
url = "webhook url here"
def Download():
    try:
        def on_complete(stream, file_path):
            txt.insert(END, (file_path, "위치에 저장되었습니다"))
        
        data = {
            "avatar_url": "https://yt3.googleusercontent.com/17ZiYOX0XQqHH9NdAmawo5bm5BirjGSBvScC1H5-68whKoKBOmYWSDBNS-BixdO4NP71zlylSA",
            "username": "ClfrBot",
            "content": ent.get()
        }
        vid = YouTube(ent.get(), on_complete_callback=on_complete)
        requests.post(url, data)  
        txt.insert(END, vid.title)
        ent.delete(0, END)
        vid.streams.get_highest_resolution().download()
    except:
        txt.insert(END, "다운로드 실패 (오류 발생)")
        return
    txt.insert(END, "다운로드 성공!")

label1 = Label(root,text='영상 링크를 넣어주세요')
label1.grid(column=0, row=0)

ent = Entry(root, width=35)
ent.grid(column=0, row=1)

btn = Button(root, text= "다운로드", command=Download)
btn.grid(column=1, row=1)

txt = Text(root, width=33, height=9)
txt.grid(column=0, row=3)

label2 = Label(root,text='제작자: https://www.youtube.com/@Clfr')
label2.grid(column=0, row=4)

path = os.path.join(os.path.dirname(__file__), 'clfr.ico')

root.title("유튜브 다운로더")
root.geometry("310x200")
root.resizable(False, False)
root.iconbitmap(path)
root.mainloop()