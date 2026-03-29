import random
import webbrowser
import time

urls = [
    "https://chrisv93.github.io/rechner/netto-2000-brutto.html",
    "https://chrisv93.github.io/rechner/netto-2500-brutto.html",
    "https://chrisv93.github.io/rechner/netto-3000-brutto.html",
    "https://chrisv93.github.io/rechner/netto-3500-brutto.html",
]

texts = [
    "Ich hab einen simplen Brutto Netto Rechner gebaut, vielleicht hilft es jemandem:",
    "Falls jemand schnell sein Netto berechnen will, hab das hier gebaut:",
    "Einfacher Rechner ohne Werbung, vielleicht nützlich:",
]

for i in range(5):
    url = random.choice(urls)
    text = random.choice(texts)

    print("\nPOST TEXT:\n")
    print(text)
    print(url)

    webbrowser.open(url)
    time.sleep(10)
