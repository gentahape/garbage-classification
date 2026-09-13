import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

import sys
stderr_fd = sys.stderr.fileno()
saved_stderr_fd = os.dup(stderr_fd)
devnull_fd = os.open(os.devnull, os.O_WRONLY)
os.dup2(devnull_fd, stderr_fd)

import tensorflow as tf

os.dup2(saved_stderr_fd, stderr_fd)
os.close(devnull_fd)
os.close(saved_stderr_fd)

from PIL import Image
import numpy as np
import io

app = FastAPI(title="Garbage Classification API")

client_url_env = os.getenv("CLIENT_URL", "*")
origins = client_url_env.split(",") if client_url_env != "*" else ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = "models/best_model_finetuned.keras"
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

CLASS_NAMES = ['battery', 'biological', 'cardboard', 'clothes', 'glass', 'metal', 'paper', 'plastic', 'shoes', 'trash']

@app.get("/")
def home():
    return {"message": "Garbage Classification API is Running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if model is None:
        return {"error": "Model failed to load."}
    
    if not file.filename:
        return {"error": "No file uploaded. Please select an image file."}
    
    if not file.content_type.startswith("image/"):
        return {"error": "Invalid file format. Only image files are allowed."}
    
    try:
        contents = await file.read()
        
        if len(contents) > 2 * 1024 * 1024:
            return {"error": "File size exceeds the 2MB limit."}
        
        image = Image.open(io.BytesIO(contents))
        
        if image.mode != "RGB":
            image = image.convert("RGB")
        image = image.resize((224, 224))
        
        img_array = np.array(image, dtype=np.float32)
        img_array = np.expand_dims(img_array, axis=0)
        
        predictions = model.predict(img_array)
        predicted_class_index = np.argmax(predictions, axis=1)[0]
        confidence = float(predictions[0][predicted_class_index]) * 100
        
        predicted_label = CLASS_NAMES[predicted_class_index]
        
        return {
            "filename": file.filename,
            "predicted_class": predicted_label,
            "confidence": f"{confidence:.2f}%"
        }
    except Exception as e:
         return {"error": str(e)}
