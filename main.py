import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.widgets import RangeSlider
from mpl_toolkits.mplot3d import Axes3D
import customtkinter as ctk
import numpy as np

global pearlsGlobal
pearlsGlobal = []

def distanceOfPoints(point1: dict, point2: dict):
    distPlane = np.sqrt(np.abs(point1['x'] - point2['x'])**2 + np.abs(point1['y'] - point2['y'])**2)
    distSpace = np.sqrt(distPlane**2 + np.abs(point1['z'] - point2['z']))
    return distSpace

def generate_random_points(min_coord, max_x_coord, max_y_coord, max_z_coord, min_value, max_value, num_points):
    points = []
    for _ in range(num_points):
        x = random.randint(min_coord, max_x_coord)
        y = random.randint(min_coord, max_y_coord)
        z = random.randint(min_coord, max_z_coord)
        value = random.randint(min_value, max_value)
        point = {'x': x, 'y': y, 'z': z, 'price': value}
        points.append(point)
    return points

def browse_file():
    file_path = tk.filedialog.askopenfilename()

    pearls = []
    with open(file_path) as f:
        data = f.read()
        lines = data.split('\n')[1:]
        pearls = []
        for line in lines:
            if line.strip():
                values = line.split(';')
                distFromOrigo = distanceOfPoints({'x': 0, 'y': 0, 'z': 0}, {'x': int(values[0]), 'y': int(values[1]), 'z': int(values[2])})
                pearl = {'x': int(values[0]), 'y': int(values[1]), 'z': int(values[2]), 'price': int(values[3]), 'distFromOrigo': distFromOrigo}
                pearls.append(pearl)

        global pearlsGlobal
        pearlsGlobal = pearls

    prices = [pearl['price'] for pearl in pearls]
    sizes = np.array([pearl['price'] * 10 for pearl in pearls])

    x_coords = [pearl['x'] for pearl in pearls]
    y_coords = [pearl['y'] for pearl in pearls]
    z_coords = [pearl['z'] for pearl in pearls]

    ax.scatter(x_coords, y_coords, z_coords, s=sizes)
    warning_text.pack_forget()
    show_algorithm()

def generate_points():
    max_x_coord = int(max_x_coord_slider.get())
    max_y_coord = int(max_y_coord_slider.get())
    max_z_coord = int(max_z_coord_slider.get())
    min_value = int(min_value_slider.get())
    max_value = int(max_value_slider.get())
    num_points = int(pearls_number_slider.get())
    
    if messagebox.askquestion("Confirmation", 
                            f"Do these prompts look good?\nMaximum x: {max_x_coord}\nMaximum y: {max_y_coord}\nMaximum z: {max_z_coord}\nMinimum Value: {min_value}\nMaximum Value: {max_value}\nNumber of Points: {num_points}", 
                            icon ='info') == 'yes':
        pearls = generate_random_points(0, max_x_coord, max_y_coord, max_z_coord, min_value, max_value, num_points)
        global pearlsGlobal
        pearlsGlobal = pearls
        sizes = np.array([pearl['price'] * 10 for pearl in pearls])

        x_coords = [pearl['x'] for pearl in pearls]
        y_coords = [pearl['y'] for pearl in pearls]
        z_coords = [pearl['z'] for pearl in pearls]
        ax.scatter(x_coords, y_coords, z_coords, s=sizes)
        warning_text.pack_forget()
        show_algorithm()
    else:
        return

def empty_graph(ax):
    ax.clear()
    root.update()
    root.update_idletasks()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Pearlhunt')

def remove_lines(ax):
    for line in ax.lines:
        line.remove()

def start_algorithm():
    if ax.has_data():
        algorithm = algorith_selector.get()
        treshold = moho_treshold.get()
        smart = smart_checkbox.get()
        if smart_checkbox.get() == 1:
            smart_moho()
        else:
            start_moho(algorithm, treshold, smart)
    else:
        messagebox.showerror("Error", "No data is imported yet, please select one and add some data to the graph!")

def start_moho(algorithm, moho_min, smart):
    if ax.has_data():    
        if algorithm == "MOHO":
            remove_lines(ax)
            
            submarine_speed = algorithm_speed.get()
            distance_available = algorithm_time.get() * submarine_speed
            valueables = []
            path = []

            for i in pearlsGlobal:
                if i['price'] >= moho_min:
                    valueables.append(i)
            origo = {'x': 0, 'y': 0, 'z': 0, 'price': 0}
            path.append(origo)
            actualPeal = origo

            while len(valueables) > 0:
                valueables = sorted(valueables, key=lambda x: distanceOfPoints(actualPeal, x))
                if distance_available < (distanceOfPoints(actualPeal, valueables[0]) + distanceOfPoints(valueables[0], origo)):
                    path.append(origo)
                    break
                
                actualPeal = valueables.pop(0)
                distance_available -= distanceOfPoints(actualPeal, path[-1])
                path.append(actualPeal)
            
            if smart:
                pass
            else:
                x_coords = [pearl['x'] for pearl in path]
                y_coords = [pearl['y'] for pearl in path]
                z_coords = [pearl['z'] for pearl in path]
                ax.plot(x_coords, y_coords, z_coords, color='red')

                ax.plot([path[-1]['x'], 0], [path[-1]['y'], 0], [path[-1]['z'], 0], color='red')
            
            collected_pearls = len(path)-2 if len(path) > 3 else 0
            total_value = sum(pearl['price'] for pearl in path)
            percentage_collected = (collected_pearls / len(pearlsGlobal)) * 100
            if smart:
                pass
            else:
                messagebox.showinfo("Collected Pearls", f"Number of Pearls: {collected_pearls}\nTotal Value: {total_value}")
            
            show_statistics(collected_pearls, total_value, percentage_collected)
            
            return collected_pearls, total_value, moho_min
    else:
        messagebox.showerror("Error", "No data is imported yet, please select one and add some data to the graph!")

def smart_moho():
    gathered_data = []
    for i in range(9):
        loop_data = start_moho("MOHO", i, True)
        gathered_data.append(loop_data)

    gathered_data = np.array(gathered_data)
    gathered_data = gathered_data[gathered_data[:, 1].argsort()]

    used_treshold = gathered_data[-1][2]
    moho_treshold.set(used_treshold)
    treshold_text.configure(text=f"Value Treshold: {round(used_treshold, 0)}")
    start_moho("MOHO", used_treshold, False)

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Pearlhunt")
root.geometry("800x800")

graph_frame = ctk.CTkFrame(root)
graph_frame.pack(side="right", fill="both", expand=True)

fig = plt.Figure(figsize=(5, 4), dpi=100)

ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Pearlhunt')
ax.view_init(elev=-90, azim=0)
ax.set_box_aspect([3, 4, 1])

canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.draw()
canvas.get_tk_widget().pack(fill="both", expand=True)

inputs_frame = ctk.CTkScrollableFrame(root)
inputs_frame.pack(side="left", fill="both", expand=True, pady=10)

sidebar_frame = ctk.CTkFrame(inputs_frame, width=200)
sidebar_frame.pack(side="top", fill="x", pady=10)

statistics_frame = ctk.CTkFrame(inputs_frame, width=200)
collected_pearls_text = ctk.CTkLabel(statistics_frame, text="", text_color="black")
collected_pearls_value = ctk.CTkLabel(statistics_frame, text="", text_color="black")
collected_pearls_percentage = ctk.CTkLabel(statistics_frame, text="", text_color="black")

algorithm_frame = ctk.CTkFrame(inputs_frame)

def on_dropdown_change(*args):
    new_value = options_dropdown.get()
    toggle_visibility(new_value)

options_dropdown = ctk.CTkOptionMenu(sidebar_frame, command=on_dropdown_change, width=200)
options_dropdown.configure(values=["Choose own file", "Generate random points"])
options_dropdown.set("Choose own file")
options_dropdown.pack(pady=10)

def update_max_x_coord(*args):
    max_x_coord_text.configure(text=f"Max x Coordinate: {round(max_x_coord_slider.get(), 0)}")

def update_max_y_coord(*args):
    max_y_coord_text.configure(text=f"Max y Coordinate: {round(max_y_coord_slider.get(), 0)}")
    
def update_max_z_coord(*args):
    max_z_coord_text.configure(text=f"Max z Coordinate: {round(max_z_coord_slider.get(), 0)}")

def update_min_value(*args):
    min_value_text.configure(text=f"Min Value: {round(min_value_slider.get(), 0)}")
    
def update_max_value(*args):
    max_value_text.configure(text=f"Max Value: {round(max_value_slider.get(), 0)}")

def update_pearls_num(*args):
    pearls_number_text.configure(text=f"Number of pearls: {round(pearls_number_slider.get(), 0)}")

def update_time(*args):
    time_text.configure(text=f"Available Time: {round(algorithm_time.get(), 0)} s")

def update_speed(*args):
    speed_text.configure(text=f"Submarine Speed: {round(algorithm_speed.get(), 0)} m/s")

def update_treshold(*args):
    treshold_text.configure(text=f"Value Treshold: {round(moho_treshold.get(), 0)}")

def disable_treshold_slider(*args):
    if smart_checkbox.get() == 1:
        moho_treshold.configure(state="disabled")
    else:
        moho_treshold.configure(state="normal")

max_x_coord_text = ctk.CTkLabel(sidebar_frame, text="Max x Coordinate: 100.0")
max_x_coord_slider = ctk.CTkSlider(sidebar_frame, from_=0, to=500, command=lambda x: update_max_x_coord(x))
max_x_coord_slider.set(100)

max_y_coord_text = ctk.CTkLabel(sidebar_frame, text="Max y Coordinate: 100.0")
max_y_coord_slider = ctk.CTkSlider(sidebar_frame, from_=0, to=500, command=lambda x: update_max_y_coord(x))
max_y_coord_slider.set(100)

max_z_coord_text = ctk.CTkLabel(sidebar_frame, text="Max z Coordinate: 50.0")
max_z_coord_slider = ctk.CTkSlider(sidebar_frame, from_=0, to=500, command=lambda x: update_max_z_coord(x))
max_z_coord_slider.set(50)

min_value_text = ctk.CTkLabel(sidebar_frame, text="Min Value: 1.0")
min_value_slider = ctk.CTkSlider(sidebar_frame, from_=0, to=100, command=lambda x: update_min_value(x))
min_value_slider.set(1)

max_value_text = ctk.CTkLabel(sidebar_frame, text="Max Value: 10.0")
max_value_slider = ctk.CTkSlider(sidebar_frame, from_=0, to=100, command=lambda x: update_max_value(x))
max_value_slider.set(10)

pearls_number_text = ctk.CTkLabel(sidebar_frame, text="Number of Pearls: 100.0")
pearls_number_slider = ctk.CTkSlider(sidebar_frame, from_=0, to=250, command=lambda x: update_pearls_num(x))
pearls_number_slider.set(100)

submit_button = ctk.CTkButton(sidebar_frame, text="Submit", width=200, command=lambda: browse_file() if options_dropdown.get() == "Choose own file" else generate_points())
submit_button.pack(pady=20)

empty_button = ctk.CTkButton(sidebar_frame, text="Empty Graph", width=200, command=lambda: empty_graph(ax))
empty_button.pack(pady=5)

warning_text = ctk.CTkLabel(sidebar_frame, text="No data is imported yet,\n please select one and add some data to the graph!", text_color="red")
warning_text.pack(pady=10)

algorith_selector = ctk.CTkOptionMenu(algorithm_frame, width=200)
algorith_selector.configure(values=["MOHO"])
algorith_selector.set("MOHO")

smart_checkbox = ctk.CTkCheckBox(algorithm_frame, text="Smart MOHO", command=lambda: disable_treshold_slider())

time_text = ctk.CTkLabel(algorithm_frame, text="Time: 5 s", text_color="black")
algorithm_time = ctk.CTkSlider(algorithm_frame, from_=1, to=300, command=lambda x: update_time(x))
speed_text = ctk.CTkLabel(algorithm_frame, text="Submarine Speed: 15 m/s", text_color="black")
algorithm_speed = ctk.CTkSlider(algorithm_frame, from_=1, to=100, command=lambda x: update_speed(x))
algorithm_time.set(5)
algorithm_speed.set(25)

treshold_text = ctk.CTkLabel(algorithm_frame, text="Value Treshold: 9", text_color="black")
moho_treshold = ctk.CTkSlider(algorithm_frame, from_=1, to=50, command=lambda x: update_treshold(x))
moho_treshold.set(9)

algorithm_start_button = ctk.CTkButton(algorithm_frame, text="Start Algorithm", width=200, command=lambda: start_algorithm())

note_label = ctk.CTkLabel(inputs_frame, text="Note: Due to limitations,\n the graph only updates when touched slightly,\n so to see any changes,\n you have to move the graph a bit!", text_color="black")
note_label.pack(pady=10)

def show_statistics(collected_pearls, total_value, percentage):
    note_label.pack_forget()
    statistics_frame.pack(side="top", fill="x", pady=10)
    collected_pearls_text.pack(pady=5)
    collected_pearls_value.pack(pady=5)
    collected_pearls_percentage.pack(pady=5)
    collected_pearls_text.configure(text=f"Collected Pearls: {collected_pearls}")
    collected_pearls_value.configure(text=f"Total Value: {total_value}")
    collected_pearls_percentage.configure(text=f"Percentage Collected: {round(percentage, 0)}%")
    note_label.pack(pady=10)

def show_algorithm():
    note_label.pack_forget()
    algorithm_frame.pack(side="top", fill="x", pady=10)
    algorith_selector.pack(pady=10)
    smart_checkbox.pack(pady=10)
    time_text.pack(pady=5)
    algorithm_time.pack(pady=10)
    speed_text.pack(pady=5)
    algorithm_speed.pack(pady=10)
    treshold_text.pack(pady=5)
    moho_treshold.pack(pady=10)
    algorithm_start_button.pack(pady=10)
    note_label.pack(pady=10)

def toggle_visibility(value):
    if value == "Generate random points":
        submit_button.forget()
        empty_button.forget()
        if ax.has_data():
            pass
        else:
            warning_text.forget()
        
        max_x_coord_text.pack()
        max_x_coord_slider.pack()
        max_y_coord_text.pack()
        max_y_coord_slider.pack()
        max_z_coord_text.pack()
        max_z_coord_slider.pack()
        
        min_value_text.pack()
        min_value_slider.pack()
        max_value_text.pack()
        max_value_slider.pack()
        pearls_number_text.pack()
        pearls_number_slider.pack()
        
        submit_button.pack(pady=20)
        empty_button.pack(pady=5)
        if ax.has_data():
            pass
        else:
            warning_text.pack(pady=10)
    else:
        max_x_coord_text.pack_forget()
        max_x_coord_slider.pack_forget()
        max_y_coord_text.pack_forget()
        max_y_coord_slider.pack_forget()
        max_z_coord_text.pack_forget()
        max_z_coord_slider.pack_forget()
        
        min_value_text.pack_forget()
        min_value_slider.pack_forget()
        max_value_text.pack_forget()
        max_value_slider.pack_forget()
        pearls_number_text.pack_forget()
        pearls_number_slider.pack_forget()

root.mainloop()