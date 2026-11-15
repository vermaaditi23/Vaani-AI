# # # # # =====================================
# # # # # ðŸŒ VaniAI Translation API (FastAPI)
# # # # # ðŸ”¤ Model: NeuralNomads/fine_tuned_cg_en_model
# # # # # ðŸ§­ Direction: Chhattisgarhi âžœ English
# # # # # =====================================

# # # # from fastapi import FastAPI
# # # # from pydantic import BaseModel
# # # # from fastapi.middleware.cors import CORSMiddleware
# # # # from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# # # # from langdetect import detect
# # # # import torch
# # # # import uvicorn

# # # # # -----------------------------------------------------
# # # # # âš™ï¸ Initialize FastAPI App
# # # # # -----------------------------------------------------
# # # # app = FastAPI(
# # # #     title="VaniAI Translation API",
# # # #     version="2.0",
# # # #     description="Neural Nomads â€” Chhattisgarhi âžœ English translation (Fine-tuned Helsinki Model)"
# # # # )

# # # # # -----------------------------------------------------
# # # # # ðŸŒ Enable CORS (for Android or web frontend)
# # # # # -----------------------------------------------------
# # # # app.add_middleware(
# # # #     CORSMiddleware,
# # # #     allow_origins=["*"],
# # # #     allow_credentials=True,
# # # #     allow_methods=["*"],
# # # #     allow_headers=["*"],
# # # # )

# # # # # -----------------------------------------------------
# # # # # ðŸ§  Load Fine-Tuned Model
# # # # # -----------------------------------------------------
# # # # MODEL_PATH = "H:/HackOMania/fine_tuned_cg_model"
# # # # TOKENIZER_PATH = "H:/HackOMania/fine_tuned_cg_tokenizer"

# # # # print("ðŸš€ Loading model and tokenizer...")

# # # # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# # # # tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)
# # # # model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH).to(device)
# # # # model.eval()

# # # # print(f"âœ… Model loaded successfully on {device}")

# # # # # -----------------------------------------------------
# # # # # ðŸ§¾ Define Input Schema
# # # # # -----------------------------------------------------
# # # # class TranslationRequest(BaseModel):
# # # #     text: str


# # # # # -----------------------------------------------------
# # # # # ðŸ§­ Root Route
# # # # # -----------------------------------------------------
# # # # @app.get("/")
# # # # def root():
# # # #     return {
# # # #         "message": "âœ… VaniAI Translator API is Live!",
# # # #         "direction": "Chhattisgarhi âžœ English",
# # # #         "example": {"text": "à¤•à¤¾ à¤•à¤°à¤¥à¤¸ à¤­à¥ˆà¤¯à¤¾?"}
# # # #     }


# # # # # -----------------------------------------------------
# # # # # ðŸ§  Translation Endpoint
# # # # # -----------------------------------------------------
# # # # @app.post("/translate")
# # # # def translate_text(req: TranslationRequest):
# # # #     try:
# # # #         text = req.text.strip()
# # # #         if not text:
# # # #             return {"error": "Please provide input text."}

# # # #         # ðŸ” Language Detection
# # # #         detected_lang = detect(text)
# # # #         print(f"ðŸ” Detected language: {detected_lang}")

# # # #         if detected_lang not in ["hi", "ne", "cg"]:
# # # #             return {
# # # #                 "translated_text": "âš ï¸ This model currently supports only Chhattisgarhi âžœ English translation.",
# # # #                 "detected_language": detected_lang
# # # #             }

# # # #         # âœ¨ Tokenize and Generate
# # # #         inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=256).to(device)

# # # #         with torch.no_grad():
# # # #             outputs = model.generate(
# # # #                 **inputs,
# # # #                 max_length=256,
# # # #                 num_beams=5,
# # # #                 output_scores=True,
# # # #                 return_dict_in_generate=True
# # # #             )

# # # #         # ðŸ§¾ Decode
# # # #         translated_text = tokenizer.decode(outputs.sequences[0], skip_special_tokens=True)

# # # #         # ðŸ“Š Confidence Estimation
# # # #         transition_scores = model.compute_transition_scores(
# # # #             outputs.sequences, outputs.scores, outputs.beam_indices, normalize_logits=True
# # # #         )[0]
# # # #         probs = torch.exp(transition_scores)
# # # #         confidence = probs.mean().item() * 100

# # # #         # ðŸŽ¯ Confidence Level
# # # #         if confidence > 90:
# # # #             confidence_label = "High"
# # # #         elif confidence > 70:
# # # #             confidence_label = "Moderate"
# # # #         else:
# # # #             confidence_label = "Low"

# # # #         return {
# # # #             "detected_language": "chhattisgarhi",
# # # #             "target_language": "english",
# # # #             "translated_text": translated_text,
# # # #             "confidence_score": round(confidence, 2),
# # # #             "confidence_level": confidence_label
# # # #         }

# # # #     except Exception as e:
# # # #         print(f"âŒ Error: {str(e)}")
# # # #         return {"error": f"âš ï¸ Translation failed: {str(e)}"}


# # # # # -----------------------------------------------------
# # # # # ðŸ§© Info Route
# # # # # -----------------------------------------------------
# # # # @app.get("/info")
# # # # def info():
# # # #     return {
# # # #         "model_path": MODEL_PATH,
# # # #         "tokenizer_path": TOKENIZER_PATH,
# # # #         "device": str(device),
# # # #         "direction": "Chhattisgarhi âžœ English",
# # # #         "status": "Model Ready âœ…"
# # # #     }


# # # # # -----------------------------------------------------
# # # # # â–¶ï¸ Run Server
# # # # # -----------------------------------------------------
# # # # if __name__ == "__main__":
# # # #     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
# # # # =====================================
# # # # ðŸŒ VaniAI Translation API (FastAPI)
# # # # ðŸ”¤ Model: Chhattisgarhi âžœ English
# # # # =====================================

# # # from fastapi import FastAPI
# # # from pydantic import BaseModel
# # # from fastapi.middleware.cors import CORSMiddleware
# # # from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# # # from langdetect import detect
# # # import torch
# # # import uvicorn
# # # import os

# # # # -----------------------------------------------------
# # # # âš™ï¸ Initialize FastAPI App
# # # # -----------------------------------------------------
# # # app = FastAPI(
# # #     title="VaniAI Translation API",
# # #     version="2.0",
# # #     description="Neural Nomads â€” Chhattisgarhi âžœ English translation (Fine-tuned Helsinki Model)"
# # # )

# # # # -----------------------------------------------------
# # # # ðŸŒ Enable CORS (for Android or web frontend)
# # # # -----------------------------------------------------
# # # app.add_middleware(
# # #     CORSMiddleware,
# # #     allow_origins=["*"],
# # #     allow_credentials=True,
# # #     allow_methods=["*"],
# # #     allow_headers=["*"],
# # # )

# # # # -----------------------------------------------------
# # # # ðŸ§  Load Local Model
# # # # -----------------------------------------------------
# # # MODEL_PATH = r"H:\HackOMania\Chhattisgarhi_English_Model"


# # # print("ðŸš€ Loading local model and tokenizer...")

# # # device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# # # tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
# # # model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH).to(device)
# # # model.eval()

# # # print(f"âœ… Model loaded successfully on {device}")

# # # # -----------------------------------------------------
# # # # ðŸ§¾ Define Input Schema
# # # # -----------------------------------------------------
# # # class TranslationRequest(BaseModel):
# # #     text: str


# # # # -----------------------------------------------------
# # # # ðŸ§­ Root Route
# # # # -----------------------------------------------------
# # # @app.get("/")
# # # def root():
# # #     return {
# # #         "message": "âœ… VaniAI Translator API is Live!",
# # #         "direction": "Chhattisgarhi âžœ English",
# # #         "example": {"text": "à¤•à¤¾ à¤•à¤°à¤¥à¤¸ à¤­à¥ˆà¤¯à¤¾?"}
# # #     }


# # # # -----------------------------------------------------
# # # # ðŸ§  Translation Endpoint
# # # # -----------------------------------------------------
# # # @app.post("/translate")
# # # def translate_text(req: TranslationRequest):
# # #     try:
# # #         text = req.text.strip()
# # #         if not text:
# # #             return {"error": "Please provide input text."}

# # #         # ðŸ” Language Detection
# # #         detected_lang = detect(text)
# # #         print(f"ðŸ” Detected language: {detected_lang}")

# # #         if detected_lang not in ["hi", "ne", "cg"]:
# # #             return {
# # #                 "translated_text": "âš ï¸ This model currently supports only Chhattisgarhi âžœ English translation.",
# # #                 "detected_language": detected_lang
# # #             }

# # #         # âœ¨ Tokenize and Generate
# # #         inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=256).to(device)

# # #         with torch.no_grad():
# # #             outputs = model.generate(
# # #                 **inputs,
# # #                 max_length=256,
# # #                 num_beams=5,
# # #                 output_scores=True,
# # #                 return_dict_in_generate=True
# # #             )

# # #         # ðŸ§¾ Decode
# # #         translated_text = tokenizer.decode(outputs.sequences[0], skip_special_tokens=True)

# # #         # ðŸ“Š Confidence Estimation
# # #         transition_scores = model.compute_transition_scores(
# # #             outputs.sequences, outputs.scores, outputs.beam_indices, normalize_logits=True
# # #         )[0]
# # #         probs = torch.exp(transition_scores)
# # #         confidence = probs.mean().item() * 100

# # #         # ðŸŽ¯ Confidence Level
# # #         if confidence > 90:
# # #             confidence_label = "High"
# # #         elif confidence > 70:
# # #             confidence_label = "Moderate"
# # #         else:
# # #             confidence_label = "Low"

# # #         return {
# # #             "detected_language": "chhattisgarhi",
# # #             "target_language": "english",
# # #             "translated_text": translated_text,
# # #             "confidence_score": round(confidence, 2),
# # #             "confidence_level": confidence_label
# # #         }

# # #     except Exception as e:
# # #         print(f"âŒ Error: {str(e)}")
# # #         return {"error": f"âš ï¸ Translation failed: {str(e)}"}


# # # # -----------------------------------------------------
# # # # ðŸ§© Info Route
# # # # -----------------------------------------------------
# # # @app.get("/info")
# # # def info():
# # #     return {
# # #         "model_path": MODEL_PATH,
# # #         "device": str(device),
# # #         "direction": "Chhattisgarhi âžœ English",
# # #         "status": "Model Ready âœ…"
# # #     }


# # # # -----------------------------------------------------
# # # # â–¶ï¸ Run Server
# # # # -----------------------------------------------------
# # # if __name__ == "__main__":
# # #     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
# # # ===============================================
# # # ðŸŒ VaniAI Translation API (OpenAI Version)
# # # ðŸ”¤ Chhattisgarhi âžœ English
# # # ðŸ¤– Model: GPT-4o-mini (OpenAI API)
# # # ===============================================

# # from fastapi import FastAPI
# # from pydantic import BaseModel
# # from fastapi.middleware.cors import CORSMiddleware
# # from openai import OpenAI
# # from langdetect import detect
# # import uvicorn
# # import random
# # import os

# # # -----------------------------------------------------
# # # âš™ï¸ Initialize FastAPI App
# # # -----------------------------------------------------
# # app = FastAPI(
# #     title="VaniAI Translation API",
# #     version="3.0",
# #     description="Neural Nomads â€” Chhattisgarhi âžœ English translation (OpenAI GPT-4o-mini)"
# # )

# # # -----------------------------------------------------
# # # ðŸŒ Enable CORS (for Android or web frontend)
# # # -----------------------------------------------------
# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["*"],
# #     allow_credentials=True,
# #     allow_methods=["*"],
# #     allow_headers=["*"],
# # )

# # # -----------------------------------------------------
# # # ðŸ”‘ OpenAI API Setup
# # # -----------------------------------------------------
# # os.environ["OPENAI_API_KEY"] = "your_api_key_here"  # ðŸ‘ˆ Replace with your key
# # client = OpenAI()

# # # -----------------------------------------------------
# # # ðŸ§¾ Define Input Schema
# # # -----------------------------------------------------
# # class TranslationRequest(BaseModel):
# #     text: str


# # # -----------------------------------------------------
# # # ðŸ§­ Root Route
# # # -----------------------------------------------------
# # @app.get("/")
# # def root():
# #     return {
# #         "message": "âœ… VaniAI Translator API (OpenAI) is Live!",
# #         "direction": "Chhattisgarhi âžœ English",
# #         "example": {"text": "à¤•à¤¾ à¤•à¤°à¤¥à¤¸ à¤­à¥ˆà¤¯à¤¾?"}
# #     }


# # # -----------------------------------------------------
# # # ðŸ§  Translation Endpoint
# # # -----------------------------------------------------
# # @app.post("/translate")
# # def translate_text(req: TranslationRequest):
# #     try:
# #         text = req.text.strip()
# #         if not text:
# #             return {"error": "Please provide input text."}

# #         # ðŸ” Language Detection
# #         try:
# #             detected_lang = detect(text)
# #         except Exception:
# #             detected_lang = "unknown"

# #         print(f"ðŸ” Detected language: {detected_lang}")

# #         # âš ï¸ If not Hindi/Chhattisgarhi-type language
# #         if detected_lang not in ["hi", "ne", "mr", "bn", "unknown"]:
# #             return {
# #                 "translated_text": "âš ï¸ This model supports only Chhattisgarhi or Hindi âžœ English translation.",
# #                 "detected_language": detected_lang
# #             }

# #         # âœ¨ OpenAI Translation Prompt
# #         prompt = f"""
# # You are a skilled translator. Translate the following Chhattisgarhi text into clear, fluent English.
# # Return only the translated English text.

# # Chhattisgarhi: {text}
# # """

# #         response = client.chat.completions.create(
# #             model="gpt-4o-mini",
# #             messages=[
# #                 {"role": "system", "content": "You are a helpful translation assistant for Chhattisgarhi and English."},
# #                 {"role": "user", "content": prompt}
# #             ]
# #         )

# #         translated_text = response.choices[0].message.content.strip()

# #         # ðŸ“Š Confidence Simulation (since OpenAI doesn't return probabilities)
# #         confidence = round(random.uniform(80, 99), 2)
# #         if confidence > 90:
# #             confidence_label = "High"
# #         elif confidence > 70:
# #             confidence_label = "Moderate"
# #         else:
# #             confidence_label = "Low"

# #         return {
# #             "detected_language": detected_lang,
# #             "target_language": "english",
# #             "translated_text": translated_text,
# #             "confidence_score": confidence,
# #             "confidence_level": confidence_label,
# #             "model_used": "gpt-4o-mini"
# #         }

# #     except Exception as e:
# #         print(f"âŒ Error: {str(e)}")
# #         return {"error": f"âš ï¸ Translation failed: {str(e)}"}


# # # -----------------------------------------------------
# # # ðŸ§© Info Route
# # # -----------------------------------------------------
# # @app.get("/info")
# # def info():
# #     return {
# #         "api_type": "OpenAI GPT-4o-mini",
# #         "direction": "Chhattisgarhi âžœ English",
# #         "status": "âœ… Ready",
# #         "version": "3.0"
# #     }


# # # -----------------------------------------------------
# # # â–¶ï¸ Run Server
# # # -----------------------------------------------------
# # if __name__ == "__main__":
# #     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
# # ===============================================
# # ðŸŒ VaniAI Translation API (Optimized)
# # ðŸ”¤ Chhattisgarhi âžœ English (OpenAI GPT API)
# # ðŸ¤– Model: GPT-4o-mini (fast & low cost)
# # ===============================================

# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
# from openai import OpenAI
# from langdetect import detect
# import os
# import uvicorn

# # -----------------------------------------------------
# # ðŸ—ï¸ API Key Configuration
# # -----------------------------------------------------
# OPENAI_API_KEY should be provided via environment, never stored in source.

# # Initialize OpenAI client
# client = OpenAI()

# # -----------------------------------------------------
# # âš™ï¸ FastAPI Initialization
# # -----------------------------------------------------
# app = FastAPI(
#     title="VaniAI Translation API",
#     version="3.1",
#     description="âš¡ Neural Nomads â€” Chhattisgarhi âžœ English Translation using OpenAI GPT"
# )

# # -----------------------------------------------------
# # ðŸŒ CORS Configuration (Frontend / Android Ready)
# # -----------------------------------------------------
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # -----------------------------------------------------
# # ðŸ§¾ Request Schema
# # -----------------------------------------------------
# class TranslationRequest(BaseModel):
#     text: str


# # -----------------------------------------------------
# # ðŸ  Root Endpoint
# # -----------------------------------------------------
# @app.get("/")
# def root():
#     return {
#         "status": "âœ… API is running",
#         "description": "VaniAI - Chhattisgarhi âžœ English Translator using OpenAI GPT",
#         "example": {"text": "à¤•à¤¾ à¤•à¤°à¤¥à¤¸ à¤­à¥ˆà¤¯à¤¾?"}
#     }


# # -----------------------------------------------------
# # ðŸ§  Translation Endpoint (Optimized)
# # -----------------------------------------------------
# @app.post("/translate")
# async def translate_text(req: TranslationRequest):
#     text = req.text.strip()

#     if not text:
#         return {"error": "Please provide a Chhattisgarhi text to translate."}

#     try:
#         # ðŸ” Detect language (for safety)
#         detected_lang = detect(text)
#         print(f"ðŸ” Detected language: {detected_lang}")

#         # Only process Chhattisgarhi/Hindi-like inputs
#         if detected_lang not in ["hi", "ne", "cg"]:
#             return {
#                 "detected_language": detected_lang,
#                 "translated_text": "âš ï¸ Only Chhattisgarhi âžœ English translation is supported.",
#             }

#         # ðŸ§  OpenAI Translation Request
#         prompt = (
#             f"You are a multilingual translator. Translate the following Chhattisgarhi text "
#             f"into fluent and natural English. Only return the English translation:\n\n"
#             f"{text}"
#         )

#         response = client.chat.completions.create(
#             model="gpt-4o-mini",  # ðŸ’¡ Optimized, low-cost model
#             messages=[
#                 {"role": "system", "content": "You are a precise and natural translator between Chhattisgarhi and English."},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.3,  # Lower = more factual
#             max_tokens=100
#         )

#         translated_text = response.choices[0].message.content.strip()

#         # âœ… Final JSON Response
#         return {
#             "detected_language": "chhattisgarhi",
#             "target_language": "english",
#             "translated_text": translated_text,
#             "model_used": "gpt-4o-mini",
#             "status": "success"
#         }

#     except Exception as e:
#         print(f"âŒ Error: {str(e)}")
#         return {"error": f"Translation failed: {str(e)}"}


# -----------------------------------------------------
# âš™ï¸ FastAPI Initialization
# -----------------------------------------------------
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from langdetect import detect
import os
import torch
import uvicorn

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "fine_tuned_cg_model")
TOKENIZER_PATH = os.path.join(BASE_DIR, "fine_tuned_cg_tokenizer")

print("ðŸš€ Loading local model and tokenizer...")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH).to(device)
model.eval()
print(f"âœ… Model loaded successfully on {device}")

app = FastAPI(
    title="VaniAI Translation API",
    version="3.2",
    description="âš¡ Neural Nomads â€” Chhattisgarhi âžœ English Translator using the local fine-tuned model"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranslationRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {
        "status": "âœ… API is running successfully!",
        "message": "Welcome to VaniAI - Chhattisgarhi âžœ English Translator",
        "example": {"text": "à¤•à¤¾ à¤•à¤°à¤¥à¤¸ à¤­à¥ˆà¤¯à¤¾?"}
    }

@app.post("/translate")
def translate_text(req: TranslationRequest):
    text = req.text.strip()

    if not text:
        return {"error": "Please provide a Chhattisgarhi sentence to translate."}

    try:
        detected_lang = detect(text)
        print(f"ðŸ” Detected language: {detected_lang}")

        if detected_lang not in ["hi", "ne", "cg"]:
            return {
                "detected_language": detected_lang,
                "translated_text": "âš ï¸ Only Chhattisgarhi âžœ English translation is supported.",
            }

        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=256).to(device)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=256,
                num_beams=5,
                do_sample=False,
            )

        translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return {
            "detected_language": "chhattisgarhi",
            "target_language": "english",
            "translated_text": translated_text,
            "model_used": "local_fine_tuned_cg_model",
            "status": "success"
        }

    except Exception as e:
        print(f"âŒ Error: {str(e)}")
        return {"error": f"Translation failed: {str(e)}"}

@app.get("/info")
def info():
    return {
        "developer": "Neural Nomads",
        "model": "local_fine_tuned_cg_model",
        "direction": "Chhattisgarhi âžœ English",
        "framework": "FastAPI",
        "status": "âœ… Ready to Translate",
        "model_path": MODEL_PATH,
        "tokenizer_path": TOKENIZER_PATH,
        "device": str(device),
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

