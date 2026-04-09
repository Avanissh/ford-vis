# 🚗 Ford Automotive AI Assistant

## 📌 Overview

An AI-powered automotive assistant that answers vehicle-related queries using **semantic search, retrieval-augmented generation (RAG), and rule-based recommendation logic**.

---

## ⚙️ Tech Stack

* Python
* FastAPI
* FAISS (Vector Search)
* Sentence Transformers (MiniLM)
* Groq LLM (LLaMA 3.1)
* Docker

---

## 🧠 System Architecture

The system follows a **modular AI pipeline**:

1. Query → Embedding
2. Embedding → FAISS retrieval
3. Retrieved context → LLM (for `/ask`)
4. Structured logic → Recommendation engine

---

## 🚀 Features

### 🔍 `/search`

* Semantic search using embeddings
* Retrieves relevant vehicle, service, and manual data

---

### 🤖 `/ask` (RAG System)

* Context-aware answering using LLM
* Prevents hallucination using strict prompt constraints
* Returns grounded responses

---

### 🚘 `/recommend`

* Rule-based recommendation engine
* Uses user intent → vehicle attributes
* Returns top 2 vehicles with reasoning

---

## 📊 Dataset Design

Synthetic dataset includes:

* Vehicle specifications
* Service schedules
* Owner manual content

Hybrid structure:

* Structured fields → recommendations
* Text fields → embeddings

---

## 🧠 Key Design Decisions

### 🔹 Why FAISS?

Fast, local, and efficient vector search for small datasets.

### 🔹 Why MiniLM embeddings?

Lightweight, fast, and effective for semantic similarity.

### 🔹 Why RAG?

Ensures responses are grounded in actual data instead of model memory.

### 🔹 Why rule-based recommendation?

Small dataset → deterministic and interpretable solution.

---

## ⚠️ Hallucination Mitigation

* Strict prompt constraints
* Context-only answering
* Low temperature (0.1)
* Fallback response for unknown queries

---

## 🐳 Docker Support

Run the application with:

```bash
docker build -t ford-vis .
docker run -p 8000:8000 --env-file .env ford-vis
```

---

## 🔗 API Endpoints

| Endpoint     | Description            |
| ------------ | ---------------------- |
| `/search`    | Semantic search        |
| `/ask`       | RAG-based Q&A          |
| `/recommend` | Vehicle recommendation |

---

## ⚠️ Limitations

* Small synthetic dataset
* No performance metrics (speed, horsepower)
* Recommendation logic is rule-based

---

## 🚀 Future Improvements

* Hybrid search (BM25 + embeddings)
* ML-based recommendation system
* Larger real-world dataset
* UI dashboard

---

## 👨‍💻 Author

Avanissh GK