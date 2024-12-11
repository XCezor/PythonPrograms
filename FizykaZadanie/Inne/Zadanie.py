import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt


# Funkcja obliczająca prąd i rysująca sinusoidę
def oblicz_i_rysuj():
    try:
        # Pobranie danych wejściowych
        U_text = entry_u.get()
        R_text = entry_r.get()
        f_text = entry_f.get()

        # Weryfikacja poprawności danych wejściowych
        if not U_text or not R_text or not f_text:
            raise ValueError("Wszystkie pola muszą być wypełnione.")

        U = float(U_text)
        R = float(R_text)
        f = float(f_text)

        if R == 0:
            raise ZeroDivisionError("Rezystancja nie może być równa zeru.")

        if f <= 0:
            raise ValueError("Częstotliwość musi być dodatnia.")

        # Obliczanie prądu
        I = U / R  # Prawo Ohma

        # Tworzenie danych do sinusoidy
        t = np.linspace(0, 1, 500)  # 1 sekunda, 500 punktów
        sinus = U * np.sin(2 * np.pi * f * t)

        # Rysowanie sinusoidy w nowym oknie
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(t, sinus, label="Napięcie (V)")
        ax.set_title("Sinusoida napięcia")
        ax.set_xlabel("Czas (s)")
        ax.set_ylabel("Napięcie (V)")
        ax.legend()
        plt.show()  # Otwiera nowy wykres w osobnym oknie

        # Wyświetlenie wyniku w oknie dialogowym
        messagebox.showinfo("Wynik", f"Prąd wynosi: {I:.2f} A")
    except ValueError as ve:
        messagebox.showerror("Błąd danych", f"Błąd: {ve}")
    except ZeroDivisionError as zde:
        messagebox.showerror("Błąd obliczeń", f"Błąd: {zde}")
    except Exception as e:
        messagebox.showerror("Nieoczekiwany błąd", f"Wystąpił nieoczekiwany błąd: {e}")


# Tworzenie głównego okna
root = tk.Tk()
root.title("Kalkulator prądu i rysownik sinusoidy")

# Styl globalny
style = ttk.Style()
style.configure("TLabel", font=("Arial", 23))
style.configure("TButton", font=("Arial", 23))
style.configure("TEntry", font=("Arial", 23))

# Etykiety i pola wejściowe
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Napięcie [V]:").grid(row=0, column=0, sticky=tk.W, pady=5)
entry_u = ttk.Entry(frame, width=15)
entry_u.grid(row=0, column=1, pady=5)

ttk.Label(frame, text="Rezystancja [Ω]:").grid(row=1, column=0, sticky=tk.W, pady=5)
entry_r = ttk.Entry(frame, width=15)
entry_r.grid(row=1, column=1, pady=5)

ttk.Label(frame, text="Częstotliwość [Hz]:").grid(row=2, column=0, sticky=tk.W, pady=5)
entry_f = ttk.Entry(frame, width=15)
entry_f.grid(row=2, column=1, pady=5)
entry_f.insert(0, "50")  # Domyślna częstotliwość

# Przycisk do obliczeń
ttk.Button(frame, text="Policz i narysuj", command=oblicz_i_rysuj).grid(row=3, column=0, columnspan=2, pady=10)

# Uruchomienie głównej pętli
root.mainloop()