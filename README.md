# Ulanzi-Newsreader
Anzeige "Neuer Beiträge des Solaranzeige.de Forums" auf der Ulanzi Clock!

Das Script liest (z.B. per Cron zu jeder vollen Stunde aufgerufen!) die Headlines der "neuen Beiträge" aus dem Forum, macht durch "piepsen" (Sound kann man das echt nicht nennen!) auf sich aufmerksam und schiebt eine einstellbare Menge dieser "News" über's Ulanzi!

Das Script benötigt folgende Abhängigkeiten:

```
 pip3 install selenium
 pip3 install requests
 pip3 install json
```

Als erstes muß man das Script save_cookies.py aufrufen. 

```
 python3 save_cookies.py
```

Das Script startet den Webbrowser Firefox und man kann sich nun am Forum anmelden! Hintergrund ist es das dabei erstellte "Cookie" abzugreifen und beim Aufruf des eigentlichen Scriptes zur Authentfizierung zu verwenden! Hat man sich erfolgreich angemeldet wechselt man zum Terminal und speichert durch "Enter" das Cookie ab!
Bei jedem Aufruf des Hauptscriptes wird das Cookie aktualisiert! 
Da das Cookie nur 24 Stunden gültig ist muß das Programm mindestens 1x innerhalb der Zeit laufen! Verpasst man das muss das Cookie durch erneutes "laufenlassen" des save_cookies.py Scriptes erneuert werden!

Das eigentliche Hauptscript "newsreader.py" lässt man dann am besten durch Cron automatisch aufrufen!

```
*/30 8-18 * * * cd /home/pi/scripts/Ulanzi-Newsreader && /usr/bin/python3 newsreader.py >/dev/null
```
Hier im Beispiel erfolgt der Aufruf des Scriptes täglich zwischen 8 und 18 Uhr aller halbe Stunde!
