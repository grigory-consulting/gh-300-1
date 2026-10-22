from raumplan.__main__ import main

KOPF = "raum;beginn;ende;gebucht_von\n"


def test_pruefen_ohne_konflikt_gibt_0(tmp_path, capsys):
    datei = tmp_path / "buchungen.csv"
    datei.write_text(
        KOPF
        + "1.05;2026-10-14 09:00;2026-10-14 10:00;Personal\n"
        + "1.05;2026-10-14 13:00;2026-10-14 14:00;Schulung\n",
        encoding="utf-8",
    )
    assert main(["pruefen", str(datei)]) == 0
    assert "Keine Konflikte gefunden." in capsys.readouterr().out


def test_pruefen_mit_konflikt_gibt_1(tmp_path, capsys):
    datei = tmp_path / "buchungen.csv"
    datei.write_text(
        KOPF
        + "1.05;2026-10-14 09:00;2026-10-14 10:30;Personal\n"
        + "1.05;2026-10-14 10:00;2026-10-14 11:00;Schulung\n",
        encoding="utf-8",
    )
    assert main(["pruefen", str(datei)]) == 1
    ausgabe = capsys.readouterr().out
    assert "Konflikt in Raum 1.05: 14.10.2026 09:00-10:30 (Personal)" in ausgabe
    assert "1 Konflikt gefunden." in ausgabe
