
"""Erstellt und verwaltet die Chroma-Vektordatenbank."""

from pathlib import Path

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings


def create_vector_store(chunks):
    project_dir = Path(__file__).resolve().parent.parent
    db_path = project_dir / "chroma_db"

    embeddings = OllamaEmbeddings(
        model="nomic-embed-text"
    )

    vector_store = Chroma(
        collection_name="handbuch_collection",
        embedding_function=embeddings,
        persist_directory=str(db_path),
    )

    # Vorhandene Einträge entfernen, damit keine Duplikate entstehen
    existing_data = vector_store.get()

    if existing_data["ids"]:
        vector_store.delete(ids=existing_data["ids"])

    # Chunks in ChromaDB speichern
    vector_store.add_texts(chunks)

    return vector_store
