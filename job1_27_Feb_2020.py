def convert(data, fr):
    # 0 for fahrenheit
    # 1 for celsius

    if fr == 0:
        return (float(data) - 32) * 5 / 9
    else:
        return (float(data) * 9 / 5) + 32


choo = input("1). Fahrenheit --> Celcius\n2). Celcius --> Fahrenheit\nPilihan> ")
sign = ""
data = 0

if int(choo) == 1 or int(choo) == 2:
    data = float(input("angka> "))

    if int(choo) == 1:
        data = convert(data, 0)
        sign = "°C"
    elif int(choo) != 1:
        data = convert(data, 1)
        sign = "°F"

    print("Hasil =", round(data), sign)
else:
    print("Salah coeg..")


