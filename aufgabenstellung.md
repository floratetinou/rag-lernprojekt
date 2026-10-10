# Aufgabenstellung: Mini-RAG für technische Dokumentation

## Ausgangssituation

Ein fiktives Unternehmen besitzt ein kurzes technisches Handbuch für ein Datenerfassungssystem. Mitarbeitende möchten Fragen dazu stellen, ohne das ganze Dokument durchsuchen zu müssen.

## Aufgabe

Entwickle eine kleine Python-Anwendung mit LangChain und einem Large Language Model (LLM). Die Anwendung soll Fragen zum bereitgestellten Handbuch beantworten und dabei die gefundenen Textstellen als Kontext verwenden.

## Funktionale Anforderungen

1. Die Anwendung kann `data/handbuch.txt` laden.
2. Der Text wird in kleinere Abschnitte (Chunks) zerlegt.
3. Für die Abschnitte werden Embeddings erzeugt und eine semantische Suche wird eingerichtet.
4. Bei einer Nutzerfrage werden relevante Abschnitte abgerufen (Retrieval).
5. Die Frage und die gefundenen Abschnitte werden an ein LLM übergeben.
6. Die Antwort basiert auf dem bereitgestellten Kontext.
7. Wenn der Kontext die Frage nicht beantwortet, soll die Anwendung das ausdrücklich sagen, statt Informationen zu erfinden.
8. Die Anwendung zeigt die verwendeten Quellabschnitte an.

## Nicht-funktionale Anforderungen

- Der Code ist in verständliche Funktionen aufgeteilt.
- API-Schlüssel werden über Umgebungsvariablen geladen und nicht im Quellcode gespeichert.
- Abhängigkeiten sind in `requirements.txt` dokumentiert.
- Die README erklärt Installation, Ausführung und Grenzen der Anwendung.
- Es werden nur Beispieldaten verwendet, keine vertraulichen Unternehmensdaten.

## Abnahmekriterien

Die Anwendung soll mindestens diese Fragen sinnvoll behandeln:

1. **„Welche Dateien kann das Datenerfassungssystem speichern?“**  
   Erwartung: Die Antwort erwähnt BLF-, MDF- und PCAPNG-Dateien, sofern die passende Passage gefunden wird.

2. **„Wie lange bleiben Daten standardmäßig gespeichert?“**  
   Erwartung: Die Antwort nennt die im Beispieldokument beschriebene Standardaufbewahrung und weist auf die dort genannten Ausnahmen hin.

3. **„Welche Farbe hat das Bürogebäude?“**  
   Erwartung: Die Anwendung erklärt, dass das Handbuch diese Information nicht enthält.

## Vorgeschlagene Etappen

- Etappe 1: Projektstruktur und Python-Umgebung
- Etappe 2: Dokument laden und Inhalt prüfen
- Etappe 3: Chunking
- Etappe 4: Embeddings und Vektorspeicher
- Etappe 5: Retriever testen
- Etappe 6: LLM und Prompt verbinden
- Etappe 7: Quellen und Tests ergänzen

## Hinweis

Das Handbuch und alle darin genannten Regeln sind frei erfunden und dienen nur dem Lernen. Sie sind keine realen Unternehmensvorgaben.
