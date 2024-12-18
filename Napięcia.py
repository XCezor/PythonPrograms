# Importing libraries
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import json
import os

file_path = "data/graphs.json"
file_path_final = "data/result_graph.json"

def load_data():
    '''
    Check if the file and folder exists. If exists, loads the data. If not, creates the file and an empty list.
    '''
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            try:
                data = json.load(file)
                if not isinstance(data, list):
                    data = []
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    return data

def load_data_final():
    '''
    Check if the file and folder exists. If exists, loads the data. If not, creates the file and an empty list.
    '''
    if os.path.exists(file_path_final):
        with open(file_path_final, "r") as file:
            try:
                data = json.load(file)
                if not isinstance(data, list):
                    data = []
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    return data

def save_data(data):
    """
    Saves data to .json file.
    """
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def save_data_final(data):
    """
    Saves data to .json file.
    """
    with open(file_path_final, "w") as file:
        json.dump(data, file, indent=4)

def add_graph(graph_data):
    '''
    Loads data from the .json file, creates new user with provided data and saves them to the file.
    '''
    # Load existing data
    data = load_data()

    # Add new data
    data.append(graph_data)

    # Save new user to the file
    save_data(data)

def add_graph_final(graph_data):
    '''
    Loads data from the .json file, creates new user with provided data and saves them to the file.
    '''
    # Load existing data
    data = load_data_final()

    # Add new data
    data.append(graph_data)

    # Save new user to the file
    save_data_final(data)

def print_graph():
    data_final = load_data_final()
    graph = tk.Toplevel(window)
    graph.title("Graph of Voltage")
    graph.geometry("800x600")

    a, b = plt.subplots()
    colors = ("r", "b", "y", "g")
    num_color = 0

    max_time = 0
    for data in data_final:
        time = 1 / data["frequency"]
        max_time = max(max_time, 2 * time)

    timeline = np.linspace(0, max_time, 1000)

    for data in data_final:
        voltage = data["maxvoltage"] * np.sin(2 * np.pi * data["frequency"] * timeline)
        b.plot(timeline, voltage, color=colors[num_color])
        if num_color < 3:
            num_color += 1
        else:
            num_color = 0

    b.set_title("Graph")
    b.set_xlabel("Time [s]")
    b.set_ylabel("Voltage [V]")
    b.legend()

    canvas = FigureCanvasTkAgg(a, master=graph)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def count_voltage(induction, turns, area, frequency):
    global max_voltage
    graph_data = {"induction": induction, "turns": turns, "area": area, "frequency": frequency}
    add_graph(graph_data)

    new_graph_data = load_data()

    for data in new_graph_data:
        omega = 2 * np.pi * data["frequency"]
        max_voltage = data["turns"] * data["induction"] * data["area"] * omega * np.cos(0)
        voltage = max_voltage / np.sqrt(2)
        result_count = {"maxvoltage": max_voltage, "frequency": data["frequency"]}
        add_graph_final(result_count)
        result.config(text=f"Max Voltage: {max_voltage:.2f}V\nEffective Voltage: {voltage:.2f}V")
    print_graph()

def check_data():
    try:
        induction = float(entry_tesla.get())
        turns = int(entry_turns.get())
        area = float(entry_area.get())
        frequency = float(entry_frequency.get())

        raise ValueError("All data needs to be a positive number.") if induction <= 0 or turns <= 0 or area <= 0 or frequency <= 0 else count_voltage(induction, turns, area, frequency)

    except ValueError:
        messagebox.showerror("Error", "Please fill the correct data.")

window = tk.Tk()
window.title("Graph of a voltage")
window.geometry("300x350")

label = tk.Label(window, text="Input data:")
label.pack(pady=5)

#Tesla
label_tesla = tk.Label(window, text="Magnetic Induction (T):")
label_tesla.pack()
entry_tesla = tk.Entry(window)
entry_tesla.pack(pady=5)

#Turns
label_turns = tk.Label(window, text="Number of Turns:")
label_turns.pack()
entry_turns = tk.Entry(window)
entry_turns.pack(pady=5)

#Surface Area
label_area = tk.Label(window, text="Surface Area (m2):")
label_area.pack()
entry_area = tk.Entry(window)
entry_area.pack(pady=5)

#Frequency
label_frequency = tk.Label(window, text="Frequency (Hz):")
label_frequency.pack()
entry_frequency = tk.Entry(window)
entry_frequency.pack(pady=5)

calculate_button = tk.Button(window, text="Calculate Voltage", command=check_data)
calculate_button.pack(pady=10)

result = tk.Label(window, text="Results:")
result.pack(pady=5)

window.mainloop()