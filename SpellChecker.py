from cProfile import label
from cgitb import text
import tkinter
from tkinter import *
from turtle import heading
from setuptools import Command

def cap_tu_canh_nhau_cua_1_tu(van_ban_nhap_vao):
    return [van_ban_nhap_vao[i] + van_ban_nhap_vao[i+1] for i in range (len(van_ban_nhap_vao)-1)]

def do_giong_nhau(tu1,tu2):
    tu1, tu2 = tu1.lower(), tu2.lower()
    dac_diem_chung = []
    bigram1, bigram2 = cap_tu_canh_nhau_cua_1_tu(tu1), cap_tu_canh_nhau_cua_1_tu(tu2)
    for i in range (len(bigram1)):
        #cặp kí tự chung
        try:
            ki_tu_chung = bigram2.index(bigram1[i])
            dac_diem_chung.append(bigram1[i])
        except:
            continue
    return len(dac_diem_chung)/max(len(bigram1), len(bigram2))

def AutoCorrect(tu_nhap):
    max_sim_score = 0.0
    most_sim_word = tu_nhap

    for word in docThuVien():
        cur_sim = do_giong_nhau(tu_nhap, word)
        if cur_sim > max_sim_score:
            max_sim_score = cur_sim
            most_sim_word = word
    if max_sim_score > 0.5:
        return most_sim_word
    else: 
        return tu_nhap

            

    


def docThuVien():
    tu_trong_thu_vien = []
    doc_file = open("mydictionary.txt",'r')
    for dong in doc_file:
        tu = dong.strip().lower()
        tu_trong_thu_vien.append(tu)
    doc_file.close()
    return tu_trong_thu_vien

def docFileVanBan(tenfilevanban):
    cac_tu_de_check = []
    doc_file_van_ban = open(tenfilevanban,'r')
    for dong in doc_file_van_ban:
        cac_chu_trong_1_dong = dong.strip().split()
        for tu in cac_chu_trong_1_dong:
            tu = tu.strip(".,!\":;?").lower()
            cac_tu_de_check.append(tu)
    doc_file_van_ban.close()
    return cac_tu_de_check

def kiemTraChinhTa():
    global ketqua
    ketqua.destroy()
    tu = van_ban_nhap_vao.get().strip().lower()
    if (tu not in docThuVien()) == True:
        a = "Sai Chinh Ta, duoc sua thanh:{}".format(AutoCorrect(tu))
    else:
        a = "Dung Chinh Ta, khong can sua"
    ketqua = Label(giao_dien_cua_so,font=("poppins",20),bg="#dae6f6",fg="#364971")
    ketqua.place(x=200,y=300)
    ketqua.config(text=a)

giao_dien_cua_so = Tk()
giao_dien_cua_so.title("Kiểm Tra Lỗi Chính Tả")
giao_dien_cua_so.geometry("700x400")
giao_dien_cua_so.config(background="#dae6f6")

ketqua = Label(giao_dien_cua_so)

phan_dau = Label(giao_dien_cua_so,text="Kiểm Tra Lỗi Chính Tả",font=("Trebuchet MS",30,"bold"),bg="#dae6f6",fg="#364971")
phan_dau.pack(pady=(50))

van_ban_nhap_vao = Entry(giao_dien_cua_so,justify="center",width=30,font=("poppins",25),bg="white",border=2)
van_ban_nhap_vao.pack(pady=10)
van_ban_nhap_vao.focus()

nut_nhan = Button(giao_dien_cua_so,text="Kiểm Tra",font=("arial",20,"bold"),fg="white",bg="red",command=kiemTraChinhTa)
nut_nhan.pack()

giao_dien_cua_so.mainloop()


