Quickstart (local, CPU)

1. Unzip the repo and create a venv:
   python3 -m venv venv
   source venv/bin/activate
2. Install deps (edit requirements.txt if needed):
   pip install -r requirements.txt
3. Generate sample data:
   python src/ingest/ingest_sample.py
4. Run a quick smoke training:
   python train_quick.py
5. Start API server:
   python src/server/app.py

For GPU builds and distributed training, see docs/gpu.md
