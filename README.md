JG Analyzer,
Ein einfacher Log-Analyzer für Enteickler eigener Discord-Bots

Der Analyzer durchsucht Log-Dateien nach bekannten Fehlern und gibt:
Fehlername,
Schweregrad,
Anzahl der Treffer,
Lösungsvorschlag,

aus.

Unterstützte Fehler,
Kritisch,
Fehlendes Python-Modul,
Discord-Token ungültig,
TOKEN nicht geladen,

Hoch,
Command-Fehler,
Fehlende Bot-Berechtigung,
Fehlende Intents,

Mittel,
Discord Gateway Problem,
Rate Limit,
Interaction fehlgeschlagen,
HTTP Exception,
JSON Fehler,

---

Eigene Logs analysieren,
Fehler oder Konsolen-Output in einer .log Datei speichern und anschließend analysieren:

py analyzer.py error.log

Beispiel:

JG_ANALYZER/
│
├── analyzer.py
├── error.log
└── README.md

---

Projektstruktur,
JG_ANALYZER/
│
├── analyzer.py
├── README.md
│
└── logs/
    ├── module_error.log
    ├── token_error.log
    └── gateway_error.log

---

Verwendung,
Log analysieren:

py analyzer.py logs/module_error.log


Beispiel:

py analyzer.py logs/token_error.log


---

Beispielausgabe,
Discord-Token ungültig
Schweregrad: kritisch
Anzahl: 2

Lösungsvorschlag:
DISCORD_TOKEN in .env überprüfen.
Keine Leerzeichen, kein falscher Bot-Token.

---

Version,
Aktuelle Version:
v0.1 Alpha

Hinweise

Dies ist eine Alpha-Version.,
Es werden derzeit nur bekannte Fehlermuster erkannt.,
Falsch-positive oder nicht erkannte Fehler sind möglich.,
Feedback und Bugreports sind ausdrücklich erwünscht.

Entwickler,
J. Braun
JG Systems