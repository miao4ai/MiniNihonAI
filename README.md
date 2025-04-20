# MiniNihonAI

> Lightweight AI Infrastructure for Japanese-Language Applications, Built for Extensible Multimodal Agents

---

## Overview

**MiniNihonAI** is a modular, lightweight AI infrastructure framework tailored for Japanese-language applications. It is optimized for local deployment (e.g., RTX 4090) and cloud elasticity, and serves as a robust backend engine for building retrieval-augmented generation (RAG) systems, multimodal assistants, and future autonomous agent applications.

This repository focuses **solely on the Infra layer**—apps like tourism assistants or autonomous driving agents will be built *on top* of this infrastructure using its modular APIs.

---

## Core Features

- ✅ Local-first deployment with optional cloud extensions
- ✅ Japanese LLM support (Mistral 7B, Phi-2, Elyza-Japanese)
- ✅ Embedding & RAG engine with FAISS/Qdrant
- ✅ Optional multimodal processing (CLIP, BLIP2)
- ✅ Modular FastAPI endpoints (e.g., `/ask`, `/embed`, `/image_caption`)
- ✅ PEFT-friendly architecture (LoRA/QLoRA compatible)
- ✅ Extensible for downstream Agents: tourism bots, autonomous vehicle assistants, etc.

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
├── agent/                     # (Experimental) Agent logic
│   ├── intent_router.py       # Convert natural language into structured control commands
│   └── motion_planner.py      # Motion planning module for autonomous navigation
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

## Use Cases Enabled by This Infra

- 🗺️ **Tourism Agents** – Japanese Q&A over local spots, routes, food
- 🖼️ **Multimodal Search** – Upload images and retrieve nearby location info
- 💬 **RAG QA Bots** – Retrieval-augmented answering over structured or unstructured Japanese knowledge
- 🈳 **On-Device LLM Inference** – Low-latency GPT-style response generation
- 🚘 **Autonomous Driving Agents (Prototype)** – Natural language intent → driving task interpretation pipeline
- 🛣️ **Motion Planning for Autonomous Agents** – Waypoint-based path planning and behavioral routing (WIP)

---

## Agent-Oriented Extensions

This infra also supports building **autonomous or semi-autonomous agents**, such as:

### 🧳 "Japanese Tourism Guide Agent"
> A cultural and location-aware assistant that handles tourist queries like “推荐京都春天拍照的景点有哪些？” and:
- Answers using location-tagged documents, embedding search, and optional image input
- Recommends spots, routes, and real-time considerations like weather or crowding
- Can power mobile apps, web guides, or LINE bots

### 🧭 "Japanese Autonomous Driving Agent"
> A prototype that interprets voice or text commands like “代々木公園まで連れてって” and:
- Translates → extracts intent → queries embedded location docs
- Returns planned route or task
- Optionally connects to real/simulated vehicle SDKs

### 🤖 "Japanese-English Translation Agent"
> A service agent capable of performing lightweight real-time or batch translation using a combination of LLMs, NLLB models, and a retrieval base.
- Translates and rewrites based on user intent and tone
- Can integrate with browser plugins or chat interfaces

### 🍱 "Hotel Concierge Robot Agent"
> A multimodal assistant that receives text or image inputs to:
- Recommend nearby restaurants or services
- Answer common questions about bookings or hotel rules
- Generate suggested replies to Japanese-language guest queries

Modules used:
- `llm_loader.py`, `translator.py`, `vector_store/`
- `agent/intent_router.py`, `agent/motion_planner.py`
- Future extensions: `speech_interface.py`, `vehicle_api.py`, `task_manager.py`, `tts_engine.py`Future extensions: `speech_interface.py`, `vehicle_api.py`

---


---

## Deployment Targets

- ✅ Local machine (Linux with CUDA, Windows WSL2 supported)
- ✅ Docker Compose setup
- 🔜 AWS EC2 GPU spot instance launcher

---

## License

MIT License (c) 2025 Miao Jiang.

