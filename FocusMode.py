import threading
import time
import datetime
from tkinter import *

def validate_input(input_time):
    try:
        datetime.datetime.strptime(input_time, '%H:%M')
        return True
    except ValueError:
        return False

def block_websites(host_file, website_list):
    redirect = '127.0.0.1'
    with open(host_file, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(f'{redirect} {website}\n')
    print("Website Blocked")

def handle_input(stop_time, website_list):
    current_time = datetime.datetime.now().strftime('%H:%M')
    focus_time = datetime.datetime.strptime(stop_time, '%H:%M') - datetime.datetime.strptime(current_time, '%H:%M')
    focus_time_seconds = focus_time.total_seconds()

  
    host_path ='C:\Windows\System32\drivers\etc\hosts'
    block_websites(host_path, website_list)
    print("Focus mode turned on")
    
  
    time.sleep(focus_time_seconds)

   
    unblock_websites(host_path, website_list)
    print("Focus mode turned off")

    with open('C:\\Users\\RITESH YADAV\\Desktop\\AI Voice Assistant\\DataBase\\focus.txt', 'a') as log_file:
        log_file.write(f',{focus_time_seconds}')

    root = Tk()
    root.geometry('200x50')
    label = Label(root, text='Focus mode turned off')
    label.pack()
    root.mainloop()

def unblock_websites(host_file, website_list):
    with open(host_file, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()
    print("Website Unblocked")

def is_admin():
    stop_time = input('Enter the stop time (HH:MM): ')
    if not validate_input(stop_time):
        print('Invalid input. Please enter the stop time in HH:MM format.')
        return
    
    website_list = []
    while True:
        website = input('Enter a website to block (e.g., www.facebook.com): ')
        if website:
            website_list.append(website)
            response = input('Do you want to block another website? (y/n): ')
            if response.lower() == 'n':
                break
        else:
            print('Invalid input. Please enter a valid website address.')
    
    thread = threading.Thread(target=handle_input,args=(stop_time,website_list))
    thread.start()
