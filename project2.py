import tkinter as tk
from tkinter import font
import requests
HEIGHT = 400
WIDTH = 400

def test_function(entry):
		print('This is the entry:', entry)


def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem retrieving that information'

	return final_str

def get_weather(city):
	weather_key = 'e6b5d06386bb3f507e302cf5f58880b7'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)



root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='rock.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='lightblue', bd=2.5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button (frame, text="Find Weather", font=(' Arial',15), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='lightblue', bd=2.5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.65, anchor='n')

label = tk.Label(lower_frame, font=('Sitka Text', 20))
label.place(relwidth=1, relheight=1)

root.mainloop()
