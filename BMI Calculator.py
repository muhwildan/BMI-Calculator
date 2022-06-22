import tkinter

#Fungsi untuk menghitung Body Mass Index (BMI)
def hitungBMI() :
    try :
        berat = float(inputBerat.get())
        tinggi = float(inputTinggi.get())
        if berat <= 0 or tinggi <= 0 :
            raise ValueError
        bmi = round(berat/((tinggi/100) ** 2), 2)
        kategori = ""
        if bmi < 18 :
            kategori = "Kurang Gizi Tingkat 1"
        elif bmi <= 20 :
            kategori = "Kurang Gizi Tingkat 2"
        elif bmi <= 25 :
            kategori = "Ideal"
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
        hasil["text"] = "Input yang dimasukkan salah!"

#GUI
root = tkinter.Tk()
root.geometry("250x75")
root.title("BMI Calculator")

labelBerat = tkinter.Label(root, text="Berat(Kg): ")
labelBerat.grid(column=0, row=0)

inputBerat = tkinter.Entry(root)
inputBerat.grid(column=1, row=0)

labelTinggi = tkinter.Label(root, text="Tinggi(cm): ")
labelTinggi.grid(column=0, row=1)

inputTinggi = tkinter.Entry(root)
inputTinggi.grid(column=1, row=1)

tombolHitung = tkinter.Button(root, text="Hitung", command=hitungBMI)
tombolHitung.grid(column=0, row=2)

hasil = tkinter.Label(root, text="BMI: ")
hasil.grid(column=1, row=2)

root.mainloop()