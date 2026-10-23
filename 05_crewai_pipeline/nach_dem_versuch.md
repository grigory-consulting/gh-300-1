# Übung 5: Nach dem Versuch

## Beispiel-Auftrag

Agent: **Agent**, Harness **Local**. Vergleichen Sie: Was steht hier, das in Ihrem Auftrag fehlt, und umgekehrt?

> Lege in 05_crewai_pipeline/starter eine Datei pipeline.py an. Aufruf: python pipeline.py rechnungen/rechnung_1.pdf.
> Lies den Text des PDF mit pypdf. Kein Vektorindex, keine Embeddings, kein PDFSearchTool.
> Baue mit CrewAI 1.15.28 zwei Agenten: einen, der die Rechnungsdaten exakt übernimmt und nichts erfindet, und einen, der die Rechnung in drei Sätzen für die Freigabe zusammenfasst. Der zweite bekommt neben den Feldern auch den Rechnungstext, damit er Zahlungsfrist und Skonto nennen kann.
> Das Modell kommt aus .env im Ordner starter (python-dotenv): LLM_BASE_URL, LLM_API_KEY, LLM_MODEL. Für CrewAI: LLM(model=f"openai/{LLM_MODEL}", base_url=..., api_key=..., temperature=0).
> Die Ausgabe des ersten Agenten ist ein Pydantic-Modell mit den Feldern absender (nur Firmenname, ohne Anschrift), rechnungsnummer, rechnungsdatum (JJJJ-MM-TT), betrag_netto, umsatzsteuer, betrag_brutto und positionen (bezeichnung, menge, betrag). Schreibe es als ergebnis/<Name der PDF>.json.
> Installiere nichts, was nicht in requirements.txt steht. Ändere tests/ nicht.
> Lass danach die Pipeline für beide Rechnungen laufen und dann python -m pytest.

## Fragen für die Nachbesprechung

1. Welche Teile der CrewAI-API hat Copilot richtig verwendet, und wo musste er nachbessern? Woran hätten Sie einen Fehler erkannt, ohne die Doku zu lesen?
2. Welche Felder von `rechnung_2.pdf` waren knifflig? Hat das Modell Lieferdatum und Rechnungsdatum oder Rechnungsbetrag und Zahlbetrag mit Skonto verwechselt?
3. Haben Sie das Problem im Code gelöst oder in der Formulierung an das Modell? Was davon prüfen die Tests, was nicht?
4. Was stand in der Kurzfassung zum Skonto? Sieht der zweite Agent in Ihrer Pipeline den Rechnungstext oder nur die Felder des ersten?
5. Waren die Ergebnisse beim zweiten Lauf gleich? Was bedeutet das für einen Einsatz im Rechnungseingang?
6. Wo stand der Schlüssel, und wer konnte ihn sehen: Sie, der Copilot-Agent, das Repository?
