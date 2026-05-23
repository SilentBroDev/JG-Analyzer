import sys
import re
from pathlib import Path

RULES = [
    {
        "name": "Fehlendes Python-Modul",
        "patterns": [r"ModuleNotFoundError: No module named '(\w+)'"],
        "severity": "kritisch",
        "fix": "Fehlendes Paket in requirements.txt eintragen und neu starten"
    },
    {
        "name": "Discord-Token ungültig",
        "patterns": [r"LoginFailure", r"Improper token", r"static token"],
        "severity": "kritisch",
        "fix": "DISCORD_TOKEN in .env überprüfen. Keine Leeerzeichen, kein faslcher Bot-Token."
    },
    {
        "name": "TOKEN nicht geladen",
        "patterns":[r"TOKEN is None", r"expeced token to be a string, but got NoneType"],
        "severity":"KRITISCH",
         "fix":".env prüfen: DISCORD_TOKEN=dein_token und load_dotnev() im Code"
    },
    {
        "name": "Command-Fehler",
        "patterns":[r"CommandInvokeError", r"Appplication Command raised an exception"],
        "servity":"HOCH",
        "fix":"Den betreffenden Salsh-Coammand prüfen. Meist Fehler im Parameter, Embed oder Berechnung."
    },
    {
        "name": "Disacord Gateway Problem",
        "patterns":[r"Shard ID .* has disconnected", r"Gateway.*disconnected", r"ConnectionResetError"],
        "severity":"MITTEL",
         "fix":"Meist Netzwerk/Hoster. Bot beobachten; Auto-restart aaktivieren."
    },
    {
        "name": "Rate Limit",
        "patterns":[r"RateLimited", r"Too Many Requests"],
        "severity":"MITTEL",
        "fix":"Colldowns einabauen und Command-Spam begrenzen."
    },
    {
        "name": "Fehlende Bot-Berechtigung",
        "patterns": [r"Missing Permissions", r"403 Forbidden", r"discord.errors.Forbidden"],
        "severity": "HOCH",
        "fix": "Bot-Rolle prüfen: Administrator testweise aktivieren oder benötigte Rechte gezielt setzen.",
    },
    {
        "name": "Fehlende Intents",
        "patterns": [r"PrivilegedIntentsRequired", r"intents are not enabled", r"members intent"],
        "severity": "HOCH",
        "fix": "Im Discord Developer Portal die benötigten Privileged Gateway Intents aktivieren.",
    },
    {
        "name": "Interaction fehlgeschlagen",
        "patterns": [r"InteractionResponded", r"Unknown interaction", r"interaction failed"],
        "severity": "MITTEL",
        "fix": "Prüfen, ob interaction.response mehrfach genutzt wird. Ggf. followup.send verwenden.",
    },
    {
        "name": "HTTP Exception",
        "patterns": [r"discord.errors.HTTPException", r"HTTPException", r"400 Bad Request"],
        "severity": "MITTEL",
        "fix": "Discord API Request prüfen. Häufig: Embed zu lang, ungültige Felder oder falsche Channel-ID.",
    },
    {
        "name": "JSON Fehler",
        "patterns": [r"JSONDecodeError", r"Expecting value", r"Invalid JSON"],
        "severity": "MITTEL",
        "fix": "JSON-Datei prüfen: Kommas, Anführungszeichen, Klammern und leere Dateien kontrollieren.",
    },
]

def analyze_log(text: str):
    findings = []

    for rule in RULES:
        hits = []
        for pattern in rule["patterns"]:
            matches = re.findall(pattern,text, flags=re.IGNORECASE)
            if matches:
                hits.extend(matches if isinstance(matches, list) else [matches])

        if hits:
            findings.append({
                "name": rule["name"],
                "severity": rule["severity"],
                "count": len(hits),
                "fix": rule["fix"],  
            })

    traceback_count = text.count("Traceback (most recent call last):")
    if traceback_count:
        findings.append({
            "name": "Allgemeiner Fehler",
            "severity": "HOCH",
            "count": traceback_count,
            "fix": "Traceback analysieren, um die genaue Fehlerursache zu identifizieren."
        })

    return findings

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <logfile>")
        return

    log_path = Path(sys.argv[1])
    if not log_path.is_file():
        print(f"Datei {log_path} nicht gefunden.")
        return

    with log_path.open(encoding="utf-8") as f:
        log_content = f.read()

    results = analyze_log(log_content)
    for result in results:
        print(f"{result['name']} (Schweregrad: {result['severity']}, Anzahl: {result['count']})")
        print(f"  Lösungsvorschlag: {result['fix']}\n")

if __name__ == "__main__":
    main()

