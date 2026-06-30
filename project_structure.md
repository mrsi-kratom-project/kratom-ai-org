kratom-network-app/
├── app/                  # Core application code
│   ├── __init__.py
│   ├── routes.py         # Flask route definitions
│   ├── graph_engine.py   # NetworkX logic for processing citations
│   ├── rag_engine.py     # Future RAG/Vector DB logic (placeholder)
│   ├── static/           # CSS, JS (Vis.js files), images
│   └── templates/        # HTML files (your index.html)
├── data/                 # Raw data files (CSVs, PDFs of journals)
├── tests/                # Unit tests for your graph calculations
├── .dockerignore         # Exclude files like venv or __pycache__ from Docker
├── Dockerfile            # Your container build instructions
├── requirements.txt      # Project dependencies
└── run.py                # Entry point for the application