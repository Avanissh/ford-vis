# 🚗 Ford Automotive AI Assistant (Vehicle Intelligence System)

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

```text
                ┌──────────────────────┐
                │     User Query       │
                └─────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │  Embedding Model       │
              │ (MiniLM - Transformer) │
              └─────────┬──────────────┘
                        │
                        ▼
              ┌────────────────────────┐
              │   FAISS Vector Store   │
              │ (Semantic Retrieval)   │
              └─────────┬──────────────┘
                        │
             ┌──────────┴───────────┐
             │                      │
             ▼                      ▼
     ┌──────────────┐      ┌────────────────┐
     │   /search    │      │   /ask (RAG)   │
     │  Endpoint    │      │                │
     └──────────────┘      │  Context + LLM │
                           └────────┬───────┘
                                    │
                                    ▼
                          ┌──────────────────┐
                          │   LLM (Groq)     │
                          │  Grounded Answer │
                          └──────────────────┘

             ┌────────────────────────┐
             │  /recommend Endpoint   │
             │ Rule-Based Filtering   │
             └────────────────────────┘
```

The system follows a **modular AI pipeline**:

1. Query → Embedding
2. Embedding → FAISS retrieval
3. Retrieved context → LLM (for `/ask`)
4. Structured logic → Recommendation engine

---

## 🔧 Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/Avanissh/ford-vis
cd ford-vis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment variables
cp .env.example .env
# Add your GROQ_API_KEY to .env

# 4. Run the app (index builds automatically on first run)
uvicorn app.main:app --reload
```

---

## 🐳 Docker Setup

```bash
docker build -t ford-vis .
docker run -p 8000:8000 --env-file .env ford-vis
```

---

## 🚀 API Endpoints

| Endpoint | Method | Description |
| ------------ | ------ | ---------------------- |
| `/search` | GET | Semantic search |
| `/ask` | GET | RAG-based Q&A |
| `/recommend` | GET | Vehicle recommendation |

### Example Queries

```bash
# Search
curl "http://localhost:8000/search?query=Which Ford SUV has 7 seats"

# Ask
curl "http://localhost:8000/ask?query=What does engine warning light mean"

# Recommend
curl "http://localhost:8000/recommend?query=I need a family SUV"
```

---

## 📊 Dataset Design

Synthetic dataset includes:

* Vehicle specifications (engine, transmission, fuel type, safety features)
* Service schedules (oil change, tire rotation, brake inspection, warranty)
* Owner manual content (dashboard warnings, maintenance reminders, troubleshooting)

Hybrid structure:

* Structured fields → recommendation engine
* Text fields → embeddings + FAISS retrieval

---

## 🧠 Key Design Decisions

### 🔹 Why FAISS?

Fast, local, and efficient vector search for small datasets — no network dependency or API cost.

### 🔹 Why MiniLM embeddings?

Lightweight (22M params), fast inference, and strong semantic similarity performance for factual Q&A tasks.

### 🔹 Why RAG over pure LLM?

Prevents hallucination by grounding every response in actual retrieved data. Critical for automotive domain where wrong advice (e.g. wrong service interval) has real consequences.

### 🔹 Why rule-based recommendation?

Small, structured dataset → deterministic and fully interpretable. An ML-based approach would overfit with this data size.

### 🔹 Why hybrid filtering in search?

Pure semantic search can return irrelevant chunks when user intent is clear (e.g. "family SUV" should filter to SUV-type chunks). Intent extraction + semantic fallback gives best of both.

---

## ⚠️ Hallucination Mitigation

* Strict system prompt — model instructed to only use provided context
* Context injection — only retrieved chunks passed to LLM
* Low temperature (0.1) — reduces creative/generative drift
* Explicit fallback — "I don't have enough information" for out-of-context queries

---

## ⚠️ Limitations

* Small synthetic dataset — real deployment needs larger corpus
* No performance metrics (horsepower, 0-60 speed) in current dataset
* Recommendation logic is rule-based — won't handle nuanced multi-attribute queries

---

## 🚀 Future Improvements

* Hybrid search (BM25 + dense embeddings) for better keyword recall
* ML-based recommendation model with more vehicle attributes
* Larger real-world dataset (actual Ford owner manuals)
* Persistent vector store (Pinecone/Weaviate) for production scale
* UI dashboard for non-technical users

---

## 👨‍💻 Author

Avanissh GK