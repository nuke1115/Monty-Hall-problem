import random
import tkinter as tk
root = tk.Tk()
root.geometry("340x260")
root.title("몬티홀 문제 증명기")
frame = tk.Frame(root)
frame.pack()
text_entry1 = tk.Entry(frame, width = 30, bg = 'light blue')
text_entry1.insert(0,"검증을 반복할 횟수 입력")
text_entry1.pack(pady = 15)
labelwarn = tk.Label(text='50만 회 이상은 분석에 시간이 오래 걸릴 수 있습니다',fg='red')
labelwarn.pack()
def get_text():
    Failed = 0
    Success = 0
#========값 받기 및 오류검사========
    try:
        repeatnum = int(text_entry1.get())
    except:
        labelexcept = tk.Label(text='오류가 발생하였습니다.\n입력은 무조건 숫자로만 해주세요.\n앱을 다시 실행하세요.',fg='red')
        labelexcept.pack()
    if repeatnum == 0:
        labelexceptzero = tk.Label(text='오류가 발생하였습니다.\n분석 횟수에 0은 입력할 수 없습니다\n앱을 다시 실행하세요.',fg='red')
        labelexceptzero.pack()
    if repeatnum < 0:
        labelexceptnegative = tk.Label(text='오류가 발생하였습니다.\n분석 횟수에 음수는 입력할 수 없습니다\n앱을 다시 실행하세요.',fg='red')
        labelexceptnegative.pack()        
#========증명 계산========
    if repeatnum > 0:
        for i in range(1,repeatnum+1):      
            door1 = False
            door2 = False
            door3 = False
            doored1 = False
            doored2 = False
            doored3 = False
            dnum = random.randrange(1,4)
            if dnum == 1:
                door1 = True
            if dnum == 2:
                door2 = True
            if dnum == 3:
                door3 = True
            dnum2 = random.randrange(1,4)
            if dnum2 == 1:
                doored1 = True
            if dnum2 == 2:
                doored2 = True
            if dnum2 == 3:
                doored3 = True
    #==========결과===========
            try:
                if doored1 == True:
                    if door1 == True:
                        Failed = Failed + 1
                    if door2 or door3:
                        Success = Success + 1
                if doored2 == True:
                    if door2 == True:
                        Failed = Failed + 1
                    if door1 or door3 == True:
                        Success = Success + 1
                if doored3 == True:
                    if door3 == True:
                        Failed = Failed + 1
                    if door1 or door2 == True:
                        Success = Success + 1
            except:
                labelexceptunknown = tk.Label(text='오류가 발생하였습니다.\n제작자에게 알려주세요.\n앱을 다시 실행하세요.',fg='red')
                labelexceptunknown.pack()
        a = "성공횟수:"
        b = "실패횟수:"
        c = "성공확률:"
        d = Success/repeatnum*100
        d = round(d,3)
        e = "%"
        f = "실패확률:"
        g = Failed/repeatnum*100
        g = round(g,3)
        h = "%"
        labelbar = tk.Label(text="==========분석결과==========")
        texted = a,Success,b, Failed
        textedper = c,d,e,f,g,h
        labelsum = tk.Label(text=texted)
        labelsumper = tk.Label(text=textedper)
        labelfuck = tk.Label(text='다시 하려면 앱을 다시켜주세요',fg='red')
        labelbar.pack()
        labelsumper.pack()
        labelsum.pack()
        labelfuck.pack()
button = tk.Button(frame, text = 'start', command = get_text)
button.pack(pady = 20)
root.mainloop()