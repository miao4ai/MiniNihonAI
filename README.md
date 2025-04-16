# MiniNihonAI

> Lightweight AI Infrastructure for Japanese-Language Applications

---

## Overview

**MiniNihonAI** is a lightweight, modular AI infrastructure built to support Japanese-language AI applications, with features optimized for local deployment (e.g., RTX 4090) and optional cloud extensions. This repo focuses solely on the infrastructure layer, and is designed to serve as a backend engine for applications such as semantic search, tourism assistants, RAG systems, and multimodal chat.

> Future apps (like **"Nihon Travel Buddy" / 日本貼心旅遊醬**) will utilize this infra to provide actual services and user interfaces.

---

## Core Features

- ✅ Lightweight deployment on a single GPU (e.g., RTX 4090)
- ✅ Support for Japanese LLMs (Phi-2, Mistral 7B, etc.)
- ✅ Pluggable embedding models (SBERT, OpenCLIP)
- ✅ Optional multimodal processing (CLIP, BLIP2)
- ✅ Vector DB integration (FAISS or Qdrant)
- ✅ RAG pipeline with retriever abstraction
- ✅ FastAPI-based RESTful API for downstream app consumption
- ✅ Configurable cloud deployment scripts (AWS / Docker Compose)

---

## Directory Structure (Full)

```
MiniNihonAI/
├── api/                        # FastAPI server and route logic
│   └── main.py                # Entry point for API
│   └── routers/               # Route modules
│       └── qa_router.py       # QA endpoint logic
│
├── configs/                   # Configurations
│   └── config.yaml            # All model and service configs
│
├── data/                      # Data storage and examples
│   ├── documents/             # Raw and cleaned knowledge docs
│   ├── images/                # Sample tourist images
│   └── index/                 # FAISS / Qdrant vector indexes
│
├── deploy/                    # Deployment scripts
│   ├── docker-compose.yml     # Docker infra
│   └── aws_launcher.sh        # AWS EC2 setup script
│
├── models/                    # Model loaders
│   ├── llm_loader.py          # Load and run LLMs
│   ├── embed_loader.py        # Load embedding models
│   ├── clip_loader.py         # For multimodal (image-text)
│   └── translator.py          # Optional multilingual tools
│
├── rag/                       # Retrieval-Augmented Generation
│   ├── retriever.py           # Vector search logic
│   └── rag_pipeline.py        # QA pipeline with generator
│
├── ui/                        # (Optional) Gradio/Streamlit UI
│   ├── gradio_ui.py
│   └── streamlit_ui.py
│
├── utils/                     # Utilities
│   ├── logger.py              # Logging utility
│   ├── splitter.py            # Text splitter for RAG
│   └── file_loader.py         # File and doc loader
│
├── vector_store/             # Vector DB interfaces
│   ├── faiss_engine.py        # FAISS wrapper
│   └── qdrant_engine.py       # Qdrant wrapper
│
├── logs/                     # Logging outputs
│
├── .env                      # Environment variables (API keys, etc)
├── requirements.txt          # Python dependencies
└── README.md
```

---

## Use Cases (Supported by Infra)

While this repo is not an app itself, it enables downstream applications such as:

- 🗺️ **Tourism Assistants** – Japanese Q&A over local spots
- 🖼️ **Multimodal Search** – Upload images and retrieve nearby locations
- 💬 **RAG QA Bots** – Enhanced Q&A with document retrieval
- 🈳 **Local Language Models** – Japanese GPT inference on edge

---

## Future Integration Example

A separate application, e.g. `nihon-travel-buddy`, will:
- Call `MiniNihonAI` REST APIs for LLM inference and search
- Provide a frontend (web, mobile, or chatbot)
- Possibly trigger fine-tuning or retraining via this infra

---

## Deployment Targets

- ✅ Local machine (Linux with CUDA, Windows WSL2 supported)
- ✅ Docker Compose setup
- 🔜 AWS EC2 GPU spot instance launcher

---

## License

MIT License (c) 2025 Miao Jiang

