import os
import tkinter
from tkinter import filedialog
from tkinter import ttk
from tkinter.messagebox import showinfo
import pandas as pd

PERCENT = False
COLUMNS = ['ARTIKEL', 'NAME', 'ARTIKELGRUPPE', 'L_NAME', 'PLATZ', 'min. Bestellgröße', 
           'Abgänge 12', 'Abgänge 3', 'Zugänge 12', 'Zugänge 3', 'WBZ', 'Min. Bestand', 
           'Gewicht', 'Rahmenvertrag', 'Kanban']

def chooseFile():
    global filepath
    filepath = filedialog.askopenfilename(initialdir=os.path.expanduser("~"), title="Tabellendokument auswählen", 
                                          filetypes=(("Alle Dateien", "*.*"), ("Excel 97 - 2003", "*.xls"), ("Excel 2007 - 365", "*.xlsx"), ("ODF-Tabellendokument", "*.ods")))
    if filepath:
        label_chooseFile.configure(text="Gewählte Datei: " + filepath)
        print(filepath)
        loadFile(filepath)
    else:
        print("no file chosen")

def loadFile(filename):
    global sheet
    sheet = pd.read_excel(filename)
    pb_progress["maximum"] = sheet.shape[0]
    updateProgressLabel()

    print(sheet)
    print("Zeilen: %s" %(sheet.shape[0]))

def saveFile(path):
    splitPath = path.split(".")
    sheet.to_excel(splitPath[0] + "_out." + splitPath[1], index=False)

def obtainInformation(article):
    #get stuff from scraper
    #requests.get('link1+artikel')
    #requests.get('link2+artikel')

    #Vorläufig
    return [article, "B", "C", "D", 4, 5, 6, 7, 8, 9, 10, 11, 12, True, False]

def doStuff():
    if pb_progress["value"] < pb_progress["maximum"]:
        for index, row in sheet.iterrows():
            #index = Zeile in dataframe
            #row = Daten
            print(row[COLUMNS[0]])

            info = obtainInformation(row[COLUMNS[0]])
            sheet.loc[index, COLUMNS] = info


            pb_progress["value"] += 1
            updateProgressLabel()
        saveFile(filepath)
    showinfo(message="Done!")

def updateProgressLabel():
    if PERCENT:
        x = pb_progress["value"] / pb_progress["maximum"] * 100
        label_progress.configure(text=f"Fotschritt: {x:.1f}")
    else:
        label_progress.configure(text=f"Fortschritt: {pb_progress['value']:.0f} / {pb_progress['maximum']}")


progress = 0

win = tkinter.Tk()
win.title("erp2excel")
win.geometry('400x250')
win.minsize(320, 150)
win.maxsize(800, 400)

label_chooseFile = tkinter.Label(win, text="Gewählte Datei: ")
label_chooseFile.pack(expand=True)

button_explore = tkinter.Button(win, text="Datei auswählen", command=chooseFile)
button_explore.pack(expand=True)

pb_progress = ttk.Progressbar(win, orient="horizontal", mode="determinate", length=300) #TODO: variable auf schritt setzen, maximum setzen
pb_progress.pack(expand=True)

label_progress = tkinter.Label(win, text="")
label_progress.pack(expand=True)

button_doStuff = tkinter.Button(win, text="Do Stuff", command=doStuff)
button_doStuff.pack(expand=True)

win.mainloop()
