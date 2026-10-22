"""Betriebsparameter für die Lieferterminberechnung."""

from datetime import time

# Bestellungen, die vor 15:00 Uhr eingehen, verlassen das Lager noch am selben
# Versandtag. Der Paketdienst holt um 16:30 Uhr ab.
ANNAHMESCHLUSS = time(15, 0)

# Zustelltage nach dem Versandtag, je Versandart.
ZUSTELLTAGE = {
    "standard": 2,
    "express": 1,
}
