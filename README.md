# Mini-RAG: Technical Documentation Assistant

A hands-on learning project focused on building a Retrieval-Augmented Generation (RAG) application with Python, LangChain, a vector database, and a locally running Large Language Model (LLM).

The goal is to develop a technical documentation assistant that answers questions based on the content of a technical manual rather than relying solely on the model's general knowledge.

## Project Overview

Technical documentation often contains detailed information that users need to find quickly and accurately. This project explores how a RAG system can make that information accessible through natural-language questions.

The application will:

1. Load a technical manual from a text file.
2. Split the document into smaller, meaningful text chunks.
3. Convert the chunks into numerical representations called embeddings.
4. Retrieve relevant passages using semantic search.
5. Provide the retrieved context and the user's question to an LLM.
6. Generate an answer grounded in the retrieved documentation.
7. Display source references and handle questions that cannot be answered from the available documents.

The implementation is developed incrementally, with an emphasis on understanding each component and its role in the overall system.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | Orchestration of the RAG pipeline |
| Ollama | Running an LLM locally |
| Qwen2.5 1.5B | Local language model |
| ChromaDB | Vector storage and similarity search |
| Hugging Face Sentence Transformers | Local text embeddings |
| Git & GitHub | Version control and project documentation |

*The stack reflects the current development setup. Individual components may be refined as the project evolves.*

## Architecture

The planned RAG pipeline follows these steps:

```text
Technical Manual
      |
      v
 Document Loading
      |
      v
 Text Chunking
      |
      v
 Embedding Generation
      |
      v
 Vector Database
      |
      v
 User Question
      |
      v
 Relevant Context Retrieval
      |
      v
 Question + Retrieved Context
      |
      v
 Local LLM (Ollama)
      |
      v
 Grounded Answer + Sources
```

The key principle is that the language model receives relevant passages retrieved from the documentation and uses them as context when generating its answer.

## Repository Structure

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

Additional modules and tests will be introduced as the application grows.

## Getting Started

### Prerequisites

- Python 3.14 (current development environment)
- Git
- Ollama
- Sufficient memory to run the selected local language model

### 1. Clone the repository

```bash
git clone https://github.com/floratetinou/rag-lernprojekt.git
cd rag-lernprojekt
```

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Install and run the local language model

Install Ollama from the official website:

https://ollama.com/

Download and start the model:

```bash
ollama run qwen2.5:1.5b
```

The model runs locally, so this development setup does not require an OpenAI API key.

### 5. Run the application

The RAG application is currently under development. Execution instructions will be added once the application entry point is implemented.

## Learning Objectives

This project is designed to build practical knowledge of:

- Retrieval-Augmented Generation (RAG)
- Document loading and text preprocessing
- Chunking strategies and their impact on retrieval quality
- Embeddings and semantic similarity search
- Vector databases and document retrieval
- LLM integration with LangChain
- Grounded generation and source attribution
- Testing and evaluating RAG pipelines
- Python project structure and Git-based development

## Development Approach

The application is built incrementally rather than provided as a complete, ready-made solution.

Each stage focuses on understanding the underlying concepts, implementing the relevant component, and verifying its behavior before moving to the next step.

This approach supports both practical Python development and a deeper understanding of how RAG systems work.

## Privacy and Security

- The language model is configured to run locally through Ollama.
- No OpenAI API key is required for the planned local setup.
- Do not use confidential company documents or sensitive personal information.
- Never commit API keys, passwords, or other secrets to GitHub.
- Local execution of the LLM does not automatically guarantee that every other component of an application operates offline.

## Current Status

**Status:** In active development.

The initial development environment is set up, the required LangChain and ChromaDB packages have been installed, and the local Qwen2.5 1.5B model has been downloaded through Ollama.

The next milestone is to connect the local model to Python and begin implementing the document-processing pipeline.

## Author

**Flora Tetinou-Sawouo**

This repository documents a practical learning project exploring Python, Generative AI, and Retrieval-Augmented Generation.


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
