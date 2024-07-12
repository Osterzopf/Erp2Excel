import tkinter as tk
import requests
import time

def scrape():
    label_status.config(text="")
    link = entry_link.get()
    #print("scraping")
    if link == "":
        label_status.config(text="Kein Link eingegeben")
        return
    
    r = requests.get(link)

    #print(r.url)
    #print(r.status_code)

    timestamp = time.strftime('%H:%M:%S')

    filename = "scrape_" + timestamp + ".txt"

    file = open(filename, "w")
    text = [r.url, r.status_code, r.content]
    file.writelines("% s\n" % data for data in text)
    label_status.config(text="Gespeichert in " + filename)


win = tk.Tk()

label_link = tk.Label(win, text="Link:")
entry_link = tk.Entry(win)
button_scrape = tk.Button(win, text="Scrape", command=scrape)
label_status = tk.Label(win)

label_link.pack(pady=10)
entry_link.pack(pady=10)
button_scrape.pack(pady=10)
label_status.pack(pady=10)


win.title("htmlScraper")
win.geometry('400x250')
win.minsize(320, 150)
win.maxsize(800, 400)


win.mainloop()