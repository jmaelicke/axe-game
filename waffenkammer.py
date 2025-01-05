import random

waffen = {
    "axe":    "Axt      (2 - 4 Schaden)",
    "hammer": "Hammer   (0 - 5 Schaden)",
    "knife":  "Messer   (3 Schaden)",
    "catana": "Katana   (2 - 5 Schaden)"
}

def schaden(waffenart):
    if waffenart == "axe":
        spielerschaden = random.randint(2, 4)
    elif waffenart == "hammer":
        spielerschaden = random.randint(0, 5)
    elif waffenart == "knife":
        spielerschaden = 3
    elif waffenart == "catana":
        spielerschaden = random.randint(2, 5)
    else:
        raise Exception(f"Waffe '{waffenart}' gibt es nicht.")
    
    return spielerschaden

