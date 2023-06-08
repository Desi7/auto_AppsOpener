import subprocess
import socket


def at_school():
    # Hier werden die Befehle zum Schließen der Programme eingegeben
    subprocess.call(["taskkill", "/F", "/IM", "C:/Users/Desirée Hilti/AppData/Local/Discord/Update.exe"])
    subprocess.call(["taskkill", "/F", "/IM", "C:/XboxGames/Minecraft Launcher/Content/Minecraft.exe"])
    subprocess.call(["taskkill", "/F", "/IM", "C:/Program Files/Krita (x64)/bin/krita.exe"])
    subprocess.call(["taskkill", "/F", "IM", "C:/Users/Desirée Hilti/AppData/Local/Programs/Opera/launcher.exe"])
    # Hier werden die Befehle zum Öffnen von Teams, OneNote, Docker und Outlook eingegeben
    subprocess.Popen("C:/Users/Desirée Hilti/AppData/Local/Microsoft/Teams/Update.exe")
    subprocess.Popen("C:/Program Files/Microsoft/Office/root/Office16/ONENOTE.EXE")
    subprocess.Popen("C:/Program Files/Docker/Docker/Docker Desktop.exe")
    subprocess.Popen("C:/Program Files/Microsoft/Office/root/Office16/OUTLOOK.EXE")


def at_home():
    # Hier werden die Befehle zum Schließen der Programme, wenn ich zu Hause bin, eingegeben
    subprocess.call(["taskkill", "/F", "/IM", "C:/Users/Desirée Hilti/AppData/Local/Microsoft/Teams/Update.exe"])
    subprocess.call(["taskkill", "/F", "/IM", "C:/Program Files/Microsoft/Office/root/Office16/ONENOTE.EXE"])
    subprocess.call(["taskkill", "/F", "/IM", "C:/Program Files/Docker/Docker/Docker Desktop.exe"])
    # Hier werden die Befehle zum Öffnen der Programme, die ich zu Hause verwenden werde, eingegeben
    subprocess.Popen("C:/XboxGames/Minecraft Launcher/Content/Minecraft.exe")
    subprocess.Popen("C:/Users/Desirée Hilti/AppData/Local/Programs/Opera/launcher.exe")
    subprocess.Popen("C:/Users/Desirée Hilti/AppData/Local/Discord/Update.exe")


def check_network():
    try:
        # Überprüfen der IP-Adresse des Standard-Gateways der Schule (BBW)
        school_gateway_ip = ""  # Meine IP-Adresse im Schulnetzwerk in einer Variable speichern | Behalte ich privat
        # Eine Verbindung zum Schul-Gateway-IP auf Port 80 herstellen, mit einem timeout von 5 Sekunden
        socket.create_connection((school_gateway_ip, 80), timeout=5)  # import des Modules für die Netzwerkkommunikation
        return "Schulnetzwerk"
    except OSError:
        pass  # Damit es keine Error-Meldung gibt

    try:
        # Überprüfen der IP-Adresse des Standard-Gateways von meinem Heimnetzwerk
        home_gateway_ip = ""  # Meine IP-Adresse im Heimnetzwerk in einer Variable speichern | Behalte ich privat
        # Eine Verbindung zum Schul-Gateway-IP auf Port 80 herstellen, mit einem timeout von 5 Sekunden
        socket.create_connection((home_gateway_ip, 80), timeout=5)  # import des Modules für die Netzwerkkommunikation
        return "Heimnetzwerk"
    except OSError:
        pass  # Damit es keine Error-Meldung gibt

    # Falls es keins von den oben genannten Netzwerken ist
    return "Unbekanntes Netzwerk"


# Hauptprogramm
network = check_network()  # Speichere die Funktion in einer Variable
if network == "Schulnetzwerk":  # Von der Funktion 'check_network' dem Return-Statement überprüfen
    at_school()  # Öffnet die zugewiesene Funktion
    with open("netzwerkstatus.txt", "w") as file:  # Öffnet das File in write-Mode ("w")
        file.write("Ich befinde mich im Schulnetzwerk.")  # Erstellt eine Log-Datei
    subprocess.Popen(["notepad++", "netzwerkstatus.txt"])  # Öffnet die Log-Datei
elif network == "Heimnetzwerk":  # Von der Funktion 'check_network' dem Return-Statement überprüfen
    at_home()  # Öffnet die zugewiesene Funktion
    with open("netzwerkstatus.txt", "w") as file:  # Öffnet das File in write-Mode ("w")
        file.write("Ich befinde mich im Heimnetzwerk.")  # Erstellt eine Log-Datei
    subprocess.Popen(["notepad++", "netzwerkstatus.txt"])  # Öffnet die Log-Datei
else:
    with open("netzwerkstatus.txt", "w") as file:  # Öffnet das File in write-Mode ("w")
        file.write("Unbekanntes Netzwerk")  # Falls ich mich in keinem der Beiden genannten Netzwerke befinde
