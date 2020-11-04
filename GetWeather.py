import tkinter as tk
import requests
from tkinter import font

HEIGHT = 500
WIDTH = 600

'''
Intro to what Tkinter can do, random stuff with random widgets. Next is full project

Making the tab/box
root = tk.Tk()

A canvas on top of the root tab, makes the initial size HEIGHT and WIDTH
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

A frame on the root to place things into - on top of root, but does not have to be entire size
frame = tk.Frame(root, bg = '#80c1ff')
frame.place(relx=.1, rely=.1, relheight=.5, relwidth=.8)

button = tk.Button(frame, text="Test Button", bg = 'red')
# One way to do it - button.pack(side='left', fill='both', expand=True)
# Second way to do it - not reccomended - button.grid(row=0, column=0)
button.place(relx=0, rely=0, relwidth=.25, relheight=.15)

label = tk.Label(frame, text="This is a label", bg='yellow')
# One way to do it - label.pack(side='right', fill='both')
# Second way to do it - not reccomended - label.grid(row=1, column=1)
label.place(relx=.3, rely=0, relwidth=.45, relheight=.1)

entry = tk.Entry(frame, bg='green', fg='white')
# One way to do it - entry.pack(side='left', fill='both')
# Second way to do it - not reccomended - entry.grid(row=2, column=2)
entry.place(relx=.8, rely=0, relwidth=.2, relheight=.1)

root.mainloop()
'''

def test_function(entry):
	print("This is the entry:", entry)

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']
		final_str = 'City: %s\nConditions: %s\nTemperature (°F): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem retrieving that information'
	return final_str

def get_weather(city):
	key = '3c34ca6a4700548681080ca64d95b7d6'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()
	format_response(weather)

	label['text'] = format_response(weather)
	

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='field.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=.5, rely=.1, relwidth=.75, relheight=.1, anchor='n')

entry = tk.Entry(frame, font=('Cambria', 14), justify='c')
entry.place(relwidth=.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('Cambria', 14), command=lambda: get_weather(entry.get()))
button.place(relx=.7, relheight=1, relwidth=.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=.5, rely=.25, relwidth=.75, relheight=.6, anchor='n')

label = tk.Label(lower_frame, font=('Cambria', 14), anchor='nw', justify='l', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()