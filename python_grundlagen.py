# Dies ist ein umfassendes Beispielskript, das grundlegende Python-Konzepte erklärt.
# Zeilen, die mit '#' beginnen, sind Kommentare und werden von Python nicht ausgeführt.

# 1. Variablen und Zuweisungen
# Variablen sind wie Behälter, in denen wir Daten speichern können.
zahl = 10  # Integer (Ganzzahl)
kommazahl = 3.14  # Float (Gleitkommazahl)
text = "Hallo, Welt!"  # String (Zeichenkette)
liste = [1, 2, 3, 4, 5]  # Liste (veränderbare Sequenz von Elementen)

# Bei Zuweisungen wird zuerst der Ausdruck rechts vom '=' ausgewertet, 
# dann wird das Ergebnis der Variable links zugewiesen.
a = b = c = 1 + 2 * 3  # Zuerst 2*3, dann 1+6, dann Zuweisungen von rechts nach links
print(f"a = {a}, b = {b}, c = {c}")

# 2. Funktionen
# Funktionen sind wiederverwendbare Codeblöcke.
def addiere(a, b):
    return a + b  # 'return' gibt das Ergebnis der Funktion zurück

# Funktionen werden erst bei Aufruf ausgeführt, nicht bei der Definition
ergebnis = addiere(5, 3)
print(f"5 + 3 = {ergebnis}")

# 3. Kontrollstrukturen
# If-Anweisung: Bedingte Ausführung von Code
if zahl == 10:  # '==' wird für Vergleiche verwendet, '=' für Zuweisungen
    print("Die Zahl ist 10")
else:
    print("Die Zahl ist nicht 10")

# For-Schleife: Iteration über eine Sequenz
for i in range(5):  # 'range(5)' erzeugt die Zahlen 0, 1, 2, 3, 4
    print(f"Schleifendurchlauf: {i}")

# While-Schleife: Wiederholung, solange eine Bedingung wahr ist
counter = 0
while counter < 3:
    print(f"While-Schleife: Zähler = {counter}")
    counter += 1  # Erhöht den Zähler um 1

# 4. Klassen und Objekte
# Eine Klasse ist wie ein Bauplan für Objekte.
class Auto:
    def __init__(self, marke, modell):
        # '__init__' ist der Konstruktor, aufgerufen bei Objekterstellung
        # 'self' bezieht sich auf das aktuelle Objekt
        self.marke = marke
        self.modell = modell
    
    def fahren(self):
        print(f"{self.marke} {self.modell} fährt.")

# Objekterstellung und -verwendung
mein_auto = Auto("VW", "Golf")
mein_auto.fahren()

# Erklärung zu 'self':
# 'self' ist wie ein Zeiger auf das aktuelle Objekt.
# Es ermöglicht den Zugriff auf Attribute und Methoden des spezifischen Objekts.

# 5. Gültigkeitsbereich (Scope)
globale_variable = "Ich bin global"

def funktion_mit_lokaler_variable():
    lokale_variable = "Ich bin lokal"
    print(globale_variable)  # Zugriff auf globale Variable ist möglich
    print(lokale_variable)

funktion_mit_lokaler_variable()
# print(lokale_variable)  # Dies würde einen NameError verursachen

# 6. Ausführungsreihenfolge und Besonderheiten
print("\nAusführungsreihenfolge und Besonderheiten:")

def beispiel_funktion():
    print("Diese Funktion wurde aufgerufen")

# Funktionsdefinitionen werden gelesen, aber nicht sofort ausgeführt
print("1. Dies wird zuerst ausgeführt")

if False:
    print("2. Dieser Code wird nie ausgeführt")

for i in range(0):
    print("3. Dieser Code wird auch nie ausgeführt")

print("4. Dies wird als Zweites ausgeführt")

# Jetzt rufen wir die Funktion auf
beispiel_funktion()

print("\nProgramm beendet")