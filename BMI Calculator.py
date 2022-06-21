import tkinter

root = tkinter.Tk()
root.title("BMI Calculator")

def hitungBMI():
    berat = float(inputBerat.get())
    tinggi = float(inputTinggi.get())
    bmi = round(berat/(tinggi ** 2), 2)
    hasil["text"] = f"BMI: {bmi}"


labelBerat = tkinter.Label(root, text="Berat(Kg): ")
labelBerat.grid(column=0, row=0)

inputBerat = tkinter.Entry(root)
inputBerat.grid(column=1, row=0)

labelTinggi = tkinter.Label(root, text="Tinggi(m): ")
labelTinggi.grid(column=0, row=1)

inputTinggi = tkinter.Entry(root)
inputTinggi.grid(column=1, row=1)

button_calculate = tkinter.Button(root, text="Hitung", command=hitungBMI)
button_calculate.grid(column=0, row=2)

hasil = tkinter.Label(root, text="BMI: ")
hasil.grid(column=1, row=2)

root.mainloop()