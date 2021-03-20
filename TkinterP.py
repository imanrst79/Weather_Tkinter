from tkinter import *
from tkinter import font

import requests

root = Tk()


# ===============================functions====================================================
def format_response(weather):
    try:
        name = weather["name"]
        desc = weather["weather"][0]["description"]
        temp = f"Temperature is: {weather['main']['temp']}°C"
        final_str = f"City: {name}\nCondition: {desc}\n{temp}"
    except:
        final_str = "Please Enter Correct City"
    return final_str


def get_weather(city):
    weather_key = "da0afed072066f240d8557d13758d304"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"appid": weather_key, 'q': city, 'units': "metric"}
    response = requests.get(url, params=params)
    weather = response.json()
    label["text"] = format_response(weather)


# ==============================User Interface===============================================

canvas = Canvas(root, height=500, width=600)
canvas.pack()

background_image = PhotoImage(file="image.png")
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = Frame(root, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = Entry(frame, font=("Courier", 15))
entry.place(relwidth=0.65, relheight=1)

button = Button(frame, text="Get Weather", font=("Courier", 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = Label(lower_frame, font=("Courier", 18), anchor='nw', justify='left',bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()
