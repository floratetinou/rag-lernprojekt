# Mini-RAG: Technischer Dokumentationsassistent

Ein Lernprojekt, in dem wir gemeinsam Schritt für Schritt eine kleine RAG-Anwendung mit Python, LangChain und einem LLM entwickeln.

## Ziel

Ein Nutzer stellt eine Frage zu einem kurzen technischen Handbuch. Die Anwendung sucht relevante Textabschnitte und lässt ein Sprachmodell eine Antwort **auf Grundlage dieser Abschnitte** formulieren. Später ergänzen wir Quellenangaben und Tests.

## Projektplan

Wir implementieren das Projekt gemeinsam in kleinen Etappen:

1. **Projekt verstehen:** Aufgabenstellung, Ordnerstruktur und virtuelle Umgebung.
2. **Dokument laden:** Text aus `data/handbuch.txt` einlesen.
3. **Chunking:** den Text in kleinere Abschnitte aufteilen.
4. **Embeddings und Vektorsuche:** Textabschnitte durchsuchbar machen.
5. **Retrieval testen:** prüfen, ob die richtigen Abschnitte gefunden werden.
6. **LLM verbinden:** Frage und gefundene Abschnitte an das Sprachmodell übergeben.
7. **Antworten mit Quellen:** Fundstellen anzeigen und fehlende Informationen ehrlich behandeln.
8. **Qualität sichern:** Testfragen, Fehlerfälle und eine kurze Projektdokumentation.

Wir schreiben die eigentliche RAG-Implementierung absichtlich **noch nicht komplett vor**. So kannst du jede Komponente selbst nachvollziehen und wir können sie gemeinsam aufbauen.

## Voraussetzungen

- Python 3.10 oder neuer
- Git und ein GitHub-Konto
- Ein API-Schlüssel für einen unterstützten LLM-/Embedding-Anbieter, falls wir einen Cloud-Anbieter verwenden
- Alternativ können wir später auf ein lokales Modell umstellen

**Wichtig:** Verwende keine vertraulichen Dokumente oder Unternehmensdaten. Lege API-Schlüssel niemals in GitHub ab.

## Einrichtung

### 1. Virtuelle Umgebung erstellen

Linux/macOS:
```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Abhängigkeiten installieren

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Umgebungsvariablen vorbereiten

Kopiere `.env.example` nach `.env` und trage den API-Schlüssel nur dann ein, wenn wir den Cloud-Anbieter tatsächlich verwenden. Die Datei `.env` wird durch `.gitignore` ausgeschlossen.

## Projektstruktur

```text
rag_lernprojekt/
├── data/
│   └── handbuch.txt
├── src/
│   └── app.py
├── .env.example
├── .gitignore
├── aufgabenstellung.md
├── requirements.txt
└── README.md
```

## Lernprinzip

Wir gehen Datei für Datei vor. Du sollst nicht nur Code kopieren, sondern verstehen, was Loader, Chunking, Embeddings, Retriever und LLM jeweils tun.
