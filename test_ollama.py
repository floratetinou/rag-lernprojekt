
from langchain_ollama import ChatOllama

# Lokales KI-Modell auswählen
llm = ChatOllama(
    model="qwen2.5:1.5b",
    temperature=0
)

# Frage an das Modell senden
antwort = llm.invoke(
    "Erkläre auf Deutsch in zwei Sätzen, was ein RAG-System ist."
)

# Antwort ausgeben
print(antwort.content)
