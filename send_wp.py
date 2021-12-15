import os
from dotenv import load_dotenv

import pywhatkit
import datetime

load_dotenv()
phone_num = os.getenv("Diyar_Phone_Num")

now = datetime.datetime.now()

int_hour = int(now.hour)
int_minute = int(now.minute)

def set_hour_min(hour,minute):
    
    minute+=3
    
    if minute >= 60:
        hour+=1
        n_minute = minute - 60

        if hour == 24:
            hour = 00
    
        return hour,n_minute

    return hour,minute

s_hour,s_min = set_hour_min(int_hour,int_minute)

class msg:
    
    def __init__(self):
        pass

    def msg_hi(self):

        pywhatkit.sendwhatmsg(phone_num, 'Hi!',s_hour,s_min,8,True,5)

