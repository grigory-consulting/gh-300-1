#!/usr/bin/env bash
# Nächtliche Prüfung aller Buchungsdateien in daten/.
# Exit-Code 1, sobald eine Datei Konflikte enthält.
set -euo pipefail
cd "$(dirname "$0")/.."

rc=0
for datei in daten/*.csv; do
  echo "nachtlauf: pruefe $datei"
  python -m raumplan pruefen "$datei" || rc=$?
done

echo "nachtlauf: fertig, rc=$rc"
exit "$rc"
