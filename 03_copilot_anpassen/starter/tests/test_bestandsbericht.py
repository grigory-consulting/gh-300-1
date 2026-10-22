from pathlib import Path

from scripts.bestandsbericht import main


def test_bericht_zeigt_knappe_artikel_mit_bestellmenge(bestandsdatei: Path, capsys) -> None:
    exit_code = main([str(bestandsdatei)])

    ausgabe = capsys.readouterr().out
    assert exit_code == 0
    assert "1 Artikel unter Mindestbestand" in ausgabe
    assert "BR-1043" in ausgabe
    assert "bestellen  20" in ausgabe
    assert "KT-0900" not in ausgabe


def test_fehler_geht_nach_stderr_mit_exit_code_1(tmp_path: Path, capsys) -> None:
    exit_code = main([str(tmp_path / "fehlt.csv")])

    ausgaben = capsys.readouterr()
    assert exit_code == 1
    assert ausgaben.out == ""
    assert "Fehler: Bestandsdatei nicht gefunden" in ausgaben.err


def test_ohne_knappe_artikel_kurze_meldung(schreibe_bestand, capsys) -> None:
    pfad = schreibe_bestand("KT-0900;Kette 9-fach;C1;9;5;12")

    assert main([str(pfad)]) == 0
    assert capsys.readouterr().out == "Alle Artikel über Mindestbestand.\n"
