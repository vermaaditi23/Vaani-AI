# VaaniAI

VaaniAI is a Chhattisgarhi-to-English translation API built with FastAPI and a locally fine-tuned sequence-to-sequence model.

## Run locally

```powershell
.\.venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000/docs to try `POST /translate` with `{"text":"..."}`. The model and tokenizer files are included in this repository using Git LFS.

## Deploy on Render

Connect this repository as a Python web service. The included `render.yaml` installs `requirements.txt` and starts the API on Render's assigned port. The model is loaded into memory when the service starts. Check Render's current instance memory limits before choosing a plan; the model weights are approximately 308 MB.

## Translation direction

The included model and API support Chhattisgarhi to English. They do not provide English-to-Chhattisgarhi translation.
