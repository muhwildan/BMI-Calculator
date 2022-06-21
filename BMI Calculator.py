import tkinter

def hitungBMI():
    try :
        berat = float(inputBerat.get())
        tinggi = float(inputTinggi.get())/100
        bmi = round(berat/(tinggi ** 2), 2)
        kategori = ""
        if bmi < 18 :
            kategori = "Kurang Gizi 1"
        elif bmi <= 20 :
            kategori = "Kurang Gizi 2"
        elif bmi <= 25 :
            kategori = "Normal"
        elif bmi <= 27 :
            kategori = "Overweight"
        elif bmi <= 30 :
            kategori = "Obesitas Tingkat 1"
        elif bmi <= 35 :
            kategori = "Obesitas Tingkat 2"
        else :
            kategori = "Obesitas Tingkat 3"
        hasil["text"] = f"BMI: {bmi} ({kategori})"
    except ValueError :
        hasil["text"] = f"Input yang dimasukkan salah!"

root = tkinter.Tk()
root.title("BMI Calculator")

labelBerat = tkinter.Label(root, text="Berat(Kg): ")
labelBerat.grid(column=0, row=0)

inputBerat = tkinter.Entry(root)
inputBerat.grid(column=1, row=0)

labelTinggi = tkinter.Label(root, text="Tinggi(cm): ")
labelTinggi.grid(column=0, row=1)

inputTinggi = tkinter.Entry(root)
inputTinggi.grid(column=1, row=1)

button_calculate = tkinter.Button(root, text="Hitung", command=hitungBMI)
button_calculate.grid(column=0, row=2)

hasil = tkinter.Label(root, text="BMI: ")
hasil.grid(column=1, row=2)

root.mainloop()