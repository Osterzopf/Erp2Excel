## Erp2Excel
Dieses Projekt sollte Daten aus einem ERP-Programm extrahieren, da nicht alle über eine vorhandene Exportfunktion auslesbar waren.
Das GUI war ein eine nur über Intenet Explorer aufrufbare Website, aus deren html-Code die Daten ausgelesen werden sollten.
Es war keine API und laut der Firma, deren Daten gebraucht wurden, auch kein anderer Weg vorhanden, um einfacher an die Daten zu kommen.

Wie sich herausgestellt hat, konnten auf den Rechnern der Firma keine externen Programme ausgeführt werden. Das Projekt wurde dann abgebrochen.

- htmlScraper.py: <br/>
Hilfsprogramm, um den genauen Aufbau der Seite herauszufinden.

- app.py: <br/>
Das eigentliche Programm. Die Daten sollten aus dem html-Code ausgelesen und in einer Excel Datei gespeichert werden.
