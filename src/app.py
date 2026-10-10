"""Einstiegspunkt für das Mini-RAG-Lernprojekt.

Wir implementieren die Anwendung gemeinsam schrittweise.
"""


"""Einstiegspunkt für das Mini-RAG-Lernprojekt."""


"""Einstiegspunkt für das Mini-RAG-Lernprojekt."""

"""Einstiegspunkt für das Mini-RAG-Lernprojekt."""


"""Einstiegspunkt für das Mini-RAG-Lernprojekt."""

from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama

from vector_store import create_vector_store


def load_document():
    """Lädt das Handbuch."""
    project_dir = Path(__file__).resolve().parent.parent
    document_path = project_dir / "data" / "handbuch.txt"
    return document_path.read_text(encoding="utf-8")


def split_document(text):
    """Teilt das Dokument in kleinere Textabschnitte."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    return splitter.split_text(text)


def generate_answer(question, vector_store, llm):
    """Sucht relevante Textabschnitte und generiert eine Antwort."""

    # 1. Relevante Textabschnitte suchen
    results = vector_store.similarity_search(question, k=2)

    # 2. Gefundene Textabschnitte als Kontext zusammenfügen
    context = "\n\n".join(
        document.page_content for document in results
    )

    # 3. Frage und Kontext an das Sprachmodell übergeben
    prompt = f"""
Du bist ein hilfreicher Assistent.
Beantworte die Frage ausschließlich anhand des folgenden Kontexts.
Wenn die Antwort nicht im Kontext steht, sage, dass die Information
im Handbuch nicht gefunden wurde.
Erfinde keine Informationen.

Kontext:
{context}

Frage:
{question}

Antwort auf Deutsch:
"""

    response = llm.invoke(prompt)
    return response.content, results


def main():
    print("Mini-RAG-Lernprojekt")

    # Dokument laden und in Chunks aufteilen
    text = load_document()
    chunks = split_document(text)

    print(f"Dokument geladen: {len(text)} Zeichen")
    print(f"Anzahl der Chunks: {len(chunks)}")

    # Vektordatenbank erstellen
    vector_store = create_vector_store(chunks)
    print("Vektordatenbank erfolgreich erstellt!")

    # Lokales Sprachmodell laden
    llm = ChatOllama(
        model="qwen2.5:1.5b",
        temperature=0,
    )

    
    # Interaktive Fragen an das RAG-System
    while True:
        question = input(
            "\nDeine Frage zum Handbuch (oder 'exit' zum Beenden): "
        ).strip()

        if question.lower() in ["exit", "quit", "ende"]:
            print("RAG-System beendet.")
            break

        if not question:
            continue

        answer, sources = generate_answer(
            question, vector_store, llm
        )

        print(f"\nAntwort:\n{answer}")

        print("\nVerwendete Textabschnitte:")
        for i, document in enumerate(sources, start=1):
            print(f"\n--- Quelle {i} ---")
            print(document.page_content)


if __name__ == "__main__":
    main()





