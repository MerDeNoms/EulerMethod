import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib . pyplot as plt


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        self.equation_label = tk.Label(text="y''+    y'+    y=    x", font='Arial, 16')
        self.equation_label.place(x=40, y=20)
        self.time_label = tk.Label(text="T =        h = ", font='Arial, 16')
        self.time_label.place(x=40, y=60)
        self.first_var = ttk.Entry(width=1, font='Arial, 14')
        self.first_var.place(x=80, y=22)
        self.second_var = ttk.Entry(width=1, font='Arial, 14')
        self.second_var.place(x=131, y=22)
        self.third_var = ttk.Entry(width=1, font='Arial, 14')
        self.third_var.place(x=178, y=22)
        self.time_var = ttk.Entry(width=2, font='Arial, 14')
        self.time_var.place(x=80, y=60)
        self.time_interval_var = ttk.Entry(width=4, font='Arial, 14')
        self.time_interval_var.place(x=155, y=60)
        self.button = tk.Button(root, bg="white", text=u"SOLVE !", command=self.open_graph)
        self.button.place(x=215, y=63)

    def open_graph(self):
        a, b, c = int(self.first_var.get()), int(self.second_var.get()), int(self.third_var.get())
        dt = float(self.time_interval_var.get())
        time = int(self.time_var.get())
        y0 = 0
        v0 = 0
        t = np.linspace(0, time, int(time / dt) + 1)
        y = np.zeros(len(t))
        v = np.zeros(len(t))
        y[0] = y0
        v[0] = v0
        print(len(t))
        for i in range(1, len(t)):
            v[i] = v[i - 1] + (c - b * y[i - 1] - a * v[i - 1]) * dt
            y[i] = y[i - 1] + v[i - 1] * dt
        plt.figure()
        plt.plot(t, y, color='blue')
        plt.xlabel('t, c')
        plt.ylabel('y(t)')
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("EulerMethod")
    root.geometry("270x100+300+200")
    root.resizable(False, False)
    root.mainloop()
