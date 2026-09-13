# Intelligent Garbage Classification System

## Project Overview
Waste management is a critical environmental challenge globally. Efficiently separating recyclable materials from general waste can significantly reduce environmental impact and improve recycling rates. However, manual sorting is time-consuming and prone to human error. In this highly dynamic landscape, automated classification is a crucial asset. 

A State-of-the-Art Computer Vision approach. Transforming visual data into actionable environmental solutions using a fine-tuned **EfficientNetV2B0** Deep Learning architecture for real-time garbage image classification.

---

## Objectives
1. **Automating Waste Sorting:** Quantifying and classifying waste images into 10 distinct categories such as plastic, glass, paper, and organic waste.
2. **Improving Recycling Efficiency:** Extracting visual patterns to identify recyclable versus non-recyclable materials accurately.
3. **Providing Scalable Solutions:** Deploying the trained model across various platforms (Backend API, Web Frontend, and Edge devices) for widespread accessibility.

---

## Tech Stack
* **Machine Learning/Computer Vision:** TensorFlow, Keras (EfficientNetV2B0), Scikit-learn, Split-folders.
* **Backend:** FastAPI, Uvicorn, Python-dotenv.
* **Frontend:** Streamlit, PIL (Pillow).
* **Data Processing:** Pandas, NumPy, Matplotlib, Seaborn.

---

## Project Structure
```text
.
├── backend/
|   ├── models/
│   |   └── best_model_finetuned.keras
│   ├── main.py
│   ├── .env.example
│   └── requirements.txt
├── frontend/
│   ├── assets/
│   │   ├── certificate.png
│   │   └── distribution.png
│   ├── app.py
│   ├── .env.example
│   └── requirements.txt
├── notebook/
│   └── Garbage_Classification.ipynb
└── README.md
```

## Getting Started
**Prerequisites**
- Python 3.9 or higher
- Virtual Environment (Recommended)

### 1. Clone the Repository
```bash
git clone https://github.com/gentahape/garbage-classification.git
cd garbage-classification
```

### 2. Setup Environment Variables
Copy `.env.example` to `.env` in both `backend` and `frontend` directories and adjust the values:
```bash
# Setup Backend ENV
cd backend
cp .env.example .env

# Setup Frontend ENV
cd ../frontend
cp .env.example .env
cd ..
```

### 3. Backend Installation & Run
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 4. Frontend Installation & Run
Open new terminal:
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

## Project Origins
This Deep Learning project originated as a final submission for the **Belajar Fundamental Deep Learning** certification at [Dicoding](https://www.dicoding.com/academies/185). It was rigorously reviewed by industry experts, and I actively implemented their feedback to further deepen my practical understanding of advanced neural networks and Computer Vision.