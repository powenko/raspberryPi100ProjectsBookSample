#!/usr/bin/env python
# author: Powen Ko
import time
import RPi.GPIO as GPIO
KeyCurrent=range(100)
i=0
key2=[446, 167,  29,  82,  29,  84,  26,  85,  37,  78,  27,  84,  25,  88,  32,  81,  38,  77, 163,  65, 161,  52, 158,  57, 168,
      54, 162,  57, 162,  50, 163,  56, 157,  65,  51,  53,  55,  48,  46,  58, 162,  56, 162,  49,  29,  87,  50,  49,  52,  62, 159,
      57, 165,  48, 165,  52,  19,  98,  54,  63, 160,  49, 166,  50, 171,  50,4001,  61, 221,  69];
key4=[445, 152,  22,  89,  26,  87,  34,  77,  42,  77,  32,  82,  33,  79,  38,  75,  29,  85, 155,  69, 166,  52, 165,  53, 162,
      61, 165,  52, 141,  86, 163,  52, 166,  60,  49,  50,  56,  58,  50,  55, 166,  49,  47,  57,  50,  59,  58,  51,  54,  57, 166,
      56, 162,  49, 165,  52,  43,  71, 167,  58, 164,  50, 163,  52, 166,  62]
key6=[447, 157,  29,  83,  31,  81,  34,  82,  27,  79,  43,  77,  24,  87,  29,  84,  34,  78, 149,  80, 148,  80, 140,  85, 144,
      78, 166,  57, 169,  55, 165,  61, 163,  50,  50,  56, 165,  48,  48,  60, 166,  51, 163,  51,  53,  52, 166,  48,  55,  53, 166,
      49,  52,  57, 164,  49,  54,  57,  50,  51, 158,  72,  48,  61, 165,  50,4003,  56, 223,  63]
key8=[443, 161,  29,  82,  34,  78,  30,  85,  32,  83,  36,  76,  22,  91,  24,  87,  37,  78, 167,  53, 164,  57, 165,  50, 164,
      61, 161,  63, 163,  51, 168,  52, 166,  51,  50,  63, 169,  50,  46,  50,  53,  55, 161,  49,  57,  58, 165,  53,  53,  52, 166,
      56,  52,  56, 164,  59, 168,  51,  49,  58, 166,  49,  44,  57, 167,  51]
    
keys=[key2,key4,key6,key8]
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO_ECHO = 24
print "IR Signal"

#函數 -用來判斷用戶按下那個按鈕
def Funcheck(a,b,i):
    if (a-b)>0.1:      #判斷是否傳送結束
       i=0


    for j1 in range(len(keys)):
        isThisKey=True
        for j2 in range(5,len(keys[j1])-4):
            value=keys[j1][j2]
            currentValue=KeyCurrent[j2]
            rangeValue=100     # 注意：請依照實際狀況調整此變數
            if ((currentValue-rangeValue)<value and (currentValue+rangeValue)>value)==False :
                isThisKey=False
                # print " error:j1=%d" % j1 + " j2=%d" %j2  + " currentValue=%d" %currentValue+ " value=%d "%value
                break
        if isThisKey==True:
           print "Get it key%d" % j1   ＃顯示用戶按下哪一個按鈕
           if j1==0:
              GPIO.output(21,True)
           elif j1==1:
              GPIO.output(21,False)
           elif j1==2:
              GPIO.output(22,True)
           elif j1==3:
              GPIO.output(22,False)
           i=0                         ＃清除紀錄
           for j3 in range(len(KeyCurrent)):
               KeyCurrent[j3]=0
                        
           return i
                        


# 主程式 設定GPIO
GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
start=0
stop=0
   while True:
      start = time.time()
      duringDown=start-stop;
                        
      while GPIO.input(GPIO_ECHO)==0:
         start = time.time()
                        
      while GPIO.input(GPIO_ECHO)==1:
         stop = time.time()
         i=Funcheck(stop,start,i)
                        
       duringUp = stop-start
       KeyCurrent[i]=(duringUp *100000)
       i=i+1
       KeyCurrent[i]=(duringDown*100000)
       i=i+1
       i=Funcheck(stop,start,i)

#結束離開程式並還原GPIO的設定
GPIO.cleanup()
                        
                        
                        
                        
                        
                        
                        

                        
                        

