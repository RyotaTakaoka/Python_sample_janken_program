import random
import tkinter as tk
import tkinter.messagebox as tkmsg


hantei = False
watashi_name = 0
watashi_ans = 0
watashi_aiko = 0
watashi_win = 0
watashi_lose = 0
emp_ans = 0
emp_aiko = 0
tuzuki = 0


print("僕はジャンケン帝王！\nじゃんけんをしよう!")
print("帝王>>君の名前は？")

watashi_name = input("you>>")

print("帝王>>よろしくね{}！".format(watashi_name))
print("帝王>>さっそく、ジャンケンを始めよう")
print("帝王>>グーを出すときは0を、チョキを出すときは1を、パーを出すときは2を入力してね")
print("帝王>>最初はグー、じゃんけん・・・ポイ")


while hantei == False:
    watashi_ans = int(input("you>>"))
    emp_ans = int(random.choice("012"))

    if watashi_ans == 0 or watashi_ans == 1 or watashi_ans == 2:
        if watashi_ans != emp_ans:
            hantei = True
            if watashi_ans == 0 and emp_ans == 1:
                print("君がグーで、僕がチョキだから君の勝ち")
                watashi_win += 1
            elif watashi_ans == 0 and emp_ans ==2:
                print("君がグーで、僕がパーだから君の負け")
                watashi_lose += 1
            elif watashi_ans == 1 and emp_ans == 0:
                print("君がチョキで、僕がグーだから君の負け")
                watashi_lose += 1
            elif watashi_ans == 1 and emp_ans ==2:
                print("君がチョキで、僕がパーだから君の勝ち")
                watashi_win += 1
            elif watashi_ans == 2 and emp_ans == 0:
                print("君がパーで、僕がグーだから君の勝ち")
                watashi_win += 1
            elif watashi_ans == 2 and emp_ans == 1:
                print("君がパーで、僕がチョキだから君の負け")
                watashi_lose += 1
        else:
            if watashi_ans == 0 and emp_ans == 0:
                watashi_aiko = "グー"
                emp_aiko = "グー"
            elif watashi_ans == 1 and emp_ans == 1:
                watashi_aiko = "チョキ"
                emp_aiko = "チョキ"
            elif watashi_ans == 2 and emp_ans == 2:
                watashi_aiko = "パー"
                emp_aiko = "パー"
            print("帝王>>君が{}で、僕が{}だから、あいこ！".format(watashi_aiko, emp_aiko))
            print("帝王>>あいこで・・・しょ")
            continue
    else:
        print("指定された番号を入力してね")
        continue

    print("帝王>>もう一度じゃんけんをする？")
    print("帝王>>する場合は0を、やめる場合は1を入力してね")

    while tuzuki != 0 or tuzuki != 1:
        tuzuki = int(input("you>>"))
        if tuzuki == 0:
            hantei = False
            print("帝王>>もう一度じゃんけんをしよう！\n帝王>>最初はグー、じゃんけん・・・ポイ")
            break
        elif tuzuki == 1:
            print("帝王>>対戦成績は君の{}勝{}敗".format(watashi_win, watashi_lose))
            print("帝王>>楽しかった！\n帝王>>また遊ぼうね、{}！".format(watashi_name))
            break
        else:
            print("指定された番号を入力してね")
