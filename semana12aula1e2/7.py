temperatura = int(input("Qual é a temperatura atual? "))
esta_chovendo = input("Está chovendo? (sim/não) ") == "sim"

if temperatura > 30 and esta_chovendo:
    print("Está quente. E também está chovendo. Você deve ficar dentro de casa.")
elif temperatura > 30:
    print("Está quente.")
elif 20 <= temperatura <= 30 and esta_chovendo:
    print("A temperatura está agradável. Mas está chovendo. Leve um guarda-chuva.")
elif 20 <= temperatura <= 30:
    print("A temperatura está agradável.")
elif esta_chovendo:
    print("Está frio. E também está chovendo. Fique quente e seco dentro de casa.")
else:
    print("Está frio.")
