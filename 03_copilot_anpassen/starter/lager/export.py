import csv
import os


def export_bestand(artikel, verzeichnis, dateiname="bestand.csv"):
    # Bestandsliste fuer die Buchhaltung
    if not os.path.isdir(verzeichnis):
        raise Exception("directory not found: " + verzeichnis)
    pfad = os.path.join(verzeichnis, dateiname)
    f = open(pfad, "w", newline="", encoding="utf-8")
    w = csv.writer(f, delimiter=";")
    w.writerow(["nummer", "bezeichnung", "lagerort", "bestand"])
    for a in artikel:
        w.writerow([a.nummer, a.bezeichnung, a.lagerort, a.bestand])
    f.close()
    print("exported %d articles to %s" % (len(artikel), pfad))
    return pfad
