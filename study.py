#import csv
#import platform
from datetime import datetime
import json
import os


import tkinter as tk
import customtkinter as ctk
DATA_FILE = "log.json"


# class Application:
#     def __init__(self, root):
#         self.root = root
#         root.title("Timer")
    
#         root.geometry("450x200")
#         root.resizable(False, False)

#         self.total_seconds = 0
#         self.timer_running = False
#         self.timer_after_id = None

#         self.TimerCounter = ctk.CTkLabel(
#             root, 
#             text="00:00:00", 
#             font=ctk.CTkFont(family="Helvetica", size=56, weight="bold"), 
#             width=390, 
#             height=70
#         )
#         self.TimerCounter.place(x=30, y=30)

#         self.start = ctk.CTkButton(
#             root, 
#             text="Start", 
#             command=self.start_timer, 
#             width=100, 
#             height=35,
#             font=ctk.CTkFont(size=14, weight="bold")
#         )
#         self.start.place(x=110, y=120)

#         self.pause = ctk.CTkButton(
#             root, 
#             text="Pause", 
#             command=self.stop_timer, 
#             width=100, 
#             height=35,
#             font=ctk.CTkFont(size=14, weight="bold"),
#             fg_color="#A0A0A0",     
#             hover_color="#808080"
#         )
#         self.pause.place(x=240, y=120)

#     def start_timer(self):
#         if not self.timer_running:
#             self.timer_running = True
#             self.update_timer()

#     def stop_timer(self):
#         if self.timer_running:
#             self.timer_running = False
#             if self.timer_after_id:
#                 self.root.after_cancel(self.timer_after_id)
#                 self.timer_after_id = None

        

#     def update_timer(self):
#         if self.timer_running:
#             hours = self.total_seconds // 3600
#             minutes = (self.total_seconds % 3600) // 60
#             seconds = self.total_seconds % 60

#             time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
#             self.TimerCounter.configure(text=time_string)

#             self.total_seconds += 1
#             self.timer_after_id = self.root.after(1000, self.update_timer)

# if __name__ == "__main__":
#     ctk.set_appearance_mode("light")  
#     ctk.set_default_color_theme("blue")
    
#     root = ctk.CTk()
#     app = Application(root)
#     root.mainloop()



class Application:
    def __init__(self, root):
        self.root = root
        root.title("Timer")
        
        root.geometry("450x200")
        root.resizable(False, False)

        self.total_seconds = 0
        self.timer_running = False
        self.timer_after_id = None

        self.TimerCounter = ctk.CTkLabel(
            root, 
            text="00:00:00", 
            font=ctk.CTkFont(family="Helvetica", size=56, weight="bold"), 
            width=390, 
            height=70
        )
        self.TimerCounter.place(x=30, y=30)

        self.start = ctk.CTkButton(
            root, 
            text="Start", 
            command=self.start_timer, 
            width=100, 
            height=35,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.start.place(x=110, y=100)

        self.pause = ctk.CTkButton(
            root, 
            text="Pause", 
            command=self.stop_timer, 
            width=100, 
            height=35,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#A0A0A0",     
            hover_color="#808080"
        )
        self.pause.place(x=240, y=100)

        self.exit = ctk.CTkButton(
            root, 
            text="Exit", 
            command=self.exit_app, 
            width=100, 
            height=35,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#A0A0A0",     
            hover_color="#808080"
        )
        self.exit.place(x=167, y=155)

        root.protocol("WM_DELETE_WINDOW", self.exit_app)


    def log_session_json(self, minutes):
            if minutes <= 0:
                return

            if not os.path.exists(DATA_FILE) or os.stat(DATA_FILE).st_size == 0:
                data = []
            else:
                try:
                    with open(DATA_FILE, "r") as file:
                        data = json.load(file)
                except json.JSONDecodeError:
                    data = []

            today = datetime.now().strftime("%Y-%m-%d")
            exact_time = datetime.now().strftime("%H:%M:%S")
            session = {"date": today,"time":exact_time, "duration_minutes": round(minutes, 2)}

            data.append(session)

            with open(DATA_FILE, "w") as file:
                json.dump(data, file, indent=4)

            self.total_seconds = 0
    
    def start_timer(self):

        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def stop_timer(self):
        
        if self.timer_running:
            self.timer_running = False
            if self.timer_after_id:
                self.root.after_cancel(self.timer_after_id)
                self.timer_after_id = None


    def exit_app(self):
            # Stop background loop if active
            if self.timer_after_id:
                self.root.after_cancel(self.timer_after_id)

            # Log any active session duration before closing
            if self.total_seconds > 0:
                self.log_session_json(self.total_seconds / 60)

            self.root.destroy()

    def update_timer(self):
        if self.timer_running:
            hours = self.total_seconds // 3600
            minutes = (self.total_seconds % 3600) // 60
            seconds = self.total_seconds % 60

            time_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.TimerCounter.configure(text=time_string)

            self.total_seconds += 1
            self.timer_after_id = self.root.after(1000, self.update_timer)

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  
    ctk.set_default_color_theme("blue")
    
    root = ctk.CTk()
    app = Application(root)
    root.mainloop()


# if __name__ =="__main__":
#     file_path = r"C:\Users\flamm\Downloads\Study.csv"


# if platform.system() == "Windows":
#     current_date = datetime.now().strftime("%#d/%#m")
# else:
#     current_date = datetime.now().strftime("%-d/%-m")

# print(current_date)
# print(type(current_date))




# file = open(file_path)
# reader = csv.reader(file)
# header = next(reader)
# #assigning the header above so it won't get assigned everytime we access the csv file.

# studying_dic = {}




# def totalStudiedHours(reader):
#     acc = 0
#     print("      "*3)
#     for row in reader:
#         acc += (int(row[-1]))
#     return acc

# def mapping(fil):
#     global studying_dic
#     for row in fil:
#         if row[0] in studying_dic:
#             continue
#         else:
#             studying_dic|= {row[0]:{"Today's hours":0, "Total Hours":"0"}}
# #make sure to run mapping() before updating
# def HoursUpdate(fil):
#     global studying_dic
#     for row in fil:
#         if datetime.now().strftime("%#d/%#m") == row[1]:
#             int(row[0]["Total hour"]) += int(row[0]["Today's hours"])


# def addingDates(fil):
#     dates =[]
#     for row in fil:
#         dates.append(row[1])
#     return dates

# def chartsData(lst,dic):
#     print("hi")



# data shape is dictionary = {"Subject" : 
# {"Today's hours": value, "Total hours": value2}
# }
#mapping(reader)
#print(studying_dic)

#file.close
