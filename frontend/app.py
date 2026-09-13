import streamlit as st
import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from PIL import Image

load_dotenv()

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

BASE_DIR = Path(__file__).resolve().parent

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Intelligent Garbage Classification System",
    page_icon="♻️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CUSTOM CSS INJECTION
# ==========================================
st.markdown("""
    <style>
        .hero-title {
            text-align: center;
            font-size: 3.2rem;
            font-weight: 800;
            margin-bottom: 0px;
            padding-top: 2rem;
        }
        .hero-subtitle {
            text-align: center;
            font-size: 1.2rem;
            color: #666;
            margin-top: 15px;
            margin-bottom: 40px;
            padding: 0 10%;
            line-height: 1.6;
        }

        .stButton>button[kind="primary"] {
            background-color: #059669;
            border-color: #059669;
            color: #fff;
        }
        
        .challenge-card {
            background-color: #f8f9fa;
            padding: 2.5rem;
            border-radius: 12px;
            border-left: 6px solid #059669;
            margin-bottom: 2rem;
        }
        .challenge-card h4 {
            margin-top: 0;
            color: #059669;
        }
        
        @media (prefers-color-scheme: dark) {
            .challenge-card {
                background-color: #1e1e1e;
                border-left: 6px solid #10b981;
            }
            .challenge-card h4 {
                color: #10b981;
            }
            .hero-subtitle {
                color: #aaaaaa;
            }
        }
            
        .tech-card {
            background-color: #f1f3f6;
            padding: 1.5rem;
            border-radius: 10px;
            height: 100%;
        }
        @media (prefers-color-scheme: dark) {
            .tech-card {
                background-color: #262730;
            }
        }
            
        .result-box-safe { padding: 20px; border-radius: 10px; background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
        .result-box-danger { padding: 20px; border-radius: 10px; background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; }
        .result-box-neutral { padding: 20px; border-radius: 10px; background-color: #f8f9fa; color: #6c757d; border: 1px dashed #ced4da; text-align: center; }
            
        .footer {
            text-align: center;
            padding: 20px;
            color: #666;
            border-top: 1px solid #eaeaea;
            margin-top: 50px;
        }
        .footer a {
            color: #059669;
            text-decoration: none;
            margin: 0 10px;
            font-weight: 500;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SECTION: HERO
# ==========================================
st.markdown('<h1 class="hero-title">Intelligent Garbage Classification System</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">A Computer Vision approach using Transfer Learning (EfficientNetV2) to automatically categorize waste into 10 distinct classes for better recycling management.</p>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([2.5, 1.5, 1.5, 2.5])

with col2:
    st.markdown("""
    <a href="#interactive-classifier" target="_self" style="text-decoration: none;">
        <div style="
            background-color: #059669; 
            color: white; 
            padding: 0.45rem 1rem; 
            border-radius: 0.5rem; 
            text-align: center; 
            font-weight: 600;
            border: 1px solid #059669;
            transition: 0.3s;
        ">
            Start Simulation
        </div>
    </a>
    """, unsafe_allow_html=True)

with col3:
    st.link_button("View Research Notebook", url="https://colab.research.google.com/drive/1c3mMZntKuBEN02iZjtcS9DH4Vkwp6IQP?usp=sharing", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()

# ==========================================
# SECTION: Project Background
# ==========================================
st.header("Project Background")

st.markdown("""
<div class="challenge-card">
    <p>Modern waste management relies heavily on accurate sorting. Manual sorting is not only inefficient but also hazardous. Proper segregation at the source is critical for maximizing recycling rates and minimizing landfill impact. This project aims to automate visual waste sorting. The primary objectives are:</p>
    <h4>Automated Visual Sorting</h4>
    <p>Categorizing waste items that come in highly irregular shapes, colors, and physical conditions (crushed, torn, dirty).</p>
    <h4>Improving Recycling Rates</h4>
    <p>Distinguishing between recyclable materials and residual/hazardous waste.</p>
    <h4>Robust Generalization</h4>
    <p>Using a comprehensive dataset of over 12,000 images across 10 classes to train a highly accurate Deep Learning model.</p>
</div>
""", unsafe_allow_html=True)

# ==========================================
# SECTION: THE ENGINE (TECH STACK)
# ==========================================
st.header("The Engine (Tech Stack)")
st.markdown("Showcasing the full-stack architecture and deep learning tools powering this application.")

col_t1, col_t2, col_t3, col_t4 = st.columns(4)

with col_t1:
    st.markdown("""
    <div class="tech-card">
        <h4>Backend</h4>
        <ul>
            <li><b>FastAPI</b></li>
            <li>High-Performance Python API</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_t2:
    st.markdown("""
    <div class="tech-card">
        <h4>Frontend</h4>
        <ul>
            <li><b>Streamlit</b></li>
            <li>Interactive Data Web App</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_t3:
    st.markdown("""
    <div class="tech-card">
        <h4>ML Framework</h4>
        <ul>
            <li><b>TensorFlow</b> & Keras</li>
            <li>EfficientNetV2 Transfer Learning</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col_t4:
    st.markdown("""
    <div class="tech-card">
        <h4>Data & Tools</h4>
        <ul>
            <li>Scikit-Learn, Pillow</li>
            <li>Seaborn, Matplotlib</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()

# ==========================================
# SECTION: LIVE DEMO (Interactive Classifier)
# ==========================================
st.header("Interactive Classifier")
st.markdown("Test the accuracy of my Deep Learning model in real-time. Upload an image of a garbage item to classify it.")

col_form, col_result = st.columns([1.2, 1])

with col_form:
    st.markdown("#### Upload Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image Preview', width=350)
        st.markdown("<br>", unsafe_allow_html=True)
        analyze_button = st.button("Analysis Image", type="primary", use_container_width=True)
    else:
        analyze_button = False

with col_result:
    st.markdown("#### Live Analysis Result")

    if analyze_button and uploaded_file is not None:
        with st.spinner("Analyzing image..."):
            try:
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                response = requests.post(f"{API_URL}/predict", files=files)
                
                if response.status_code == 200:
                    res_data = response.json()
                    
                    if "error" in res_data:
                        st.error(f"Error: {res_data['error']}")
                    else:
                        predicted_class = res_data.get('predicted_class', 'Unknown')
                        confidence = res_data.get('confidence', '0.00%')
                        
                        recyclable_classes = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'clothes']
                        
                        if predicted_class.lower() in recyclable_classes:
                            st.markdown(f"""
                            <div class="result-box-safe">
                                <h3 style="margin-top:0; color:#155724; text-transform: uppercase;">♻️ {predicted_class}</h3>
                                <p><b>Confidence Score:</b> {confidence}</p>
                                <p><b>Category:</b> Recyclable / Reusable Material</p>
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.markdown(f"""
                            <div class="result-box-danger">
                                <h3 style="margin-top:0; color:#856404; text-transform: uppercase;">🗑️ {predicted_class}</h3>
                                <p><b>Confidence Score:</b> {confidence}</p>
                                <p><b>Category:</b> Residual or Hazardous Waste</p>
                            </div>
                            """, unsafe_allow_html=True)
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except requests.exceptions.ConnectionError:
                st.error("🚨 Failed to connect with backend!")
                st.info(f"Make sure the FastAPI server is running on `{API_URL}`.")
    else:
        st.markdown('<div class="result-box-neutral">Waiting for image upload...<br>Upload an image and click the "Analysis Image" button to get started.</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()

# ==========================================
# DATA SCRAPING & VISUALIZATION (EDA)
# ==========================================
st.header("Data Extraction & Visualizations")
st.markdown("Understanding the underlying distribution of the dataset before modeling.")

col_text, col_img = st.columns([1, 1.2])

with col_text:
    st.subheader("Image Distribution")
    st.markdown("This visualization shows the distribution of images across the 10 garbage classes.")
    st.markdown("The dataset exhibits a natural class imbalance. For instance, categories like *Clothes* and *Glass* have significantly more samples compared to *Trash* and *Battery*.")
    st.markdown("To ensure the model learns fairly across all categories without bias towards the majority class, I implemented **Class Weighting** during the training phase.")
    
with col_img:
    distribution_path = os.path.join(BASE_DIR, "assets", "distribution.png")
    if os.path.exists(distribution_path):
        st.image(distribution_path, caption="Image Distribution across 10 Garbage Classes", use_container_width=True)
    else:
        st.info("📊 Image Distribution graph will be displayed here. Please place `distribution.png` in the `frontend/assets/` folder.")

st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()

# ==========================================
# SECTION: PROJECT ORIGIN & CERTIFICATION
# ==========================================
st.header("Project Origin & Certification")
st.markdown("Serves as proof of foundational DL skills and proactive engineering initiative.")

col_cert_img, col_cert_text = st.columns([1, 1.5])

with col_cert_img:
    cert_path = os.path.join(BASE_DIR, "assets", "certificate.png")
    if os.path.exists(cert_path):
        st.image(cert_path, use_container_width=True)
    else:
        st.info("🎓 Certificate image will be displayed here. Please place `certificate.png` in the `frontend/assets/` folder.")

with col_cert_text:
    st.markdown("This project was built as a final submission for the **'Belajar Fundamental Deep Learning'** certification at Dicoding. Evaluated by industry experts, I actively applied their constructive feedback to elevate the model's performance and deepen my grasp of core Deep Learning architectures.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        st.link_button("View Course Syllabus", "https://www.dicoding.com/academies/185", use_container_width=True) 
    with btn_col2:
        st.link_button("Verify Certificate Credential", "https://www.dicoding.com/certificates/0LZ05641NX65", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ==========================================
# SECTION: FOOTER & PROJECT META
# ==========================================
st.markdown("""
    <div class="footer">
        <p>Built by <b>Genta Haetami Putra</b> — Fullstack Web Developer & ML Enthusiast</p>
        <p>
            <a href="https://gentahp.my.id" target="_blank">Personal Website</a> | 
            <a href="https://linkedin.com/in/gentahp" target="_blank">LinkedIn</a> | 
            <a href="https://github.com/gentahape/garbage-classification" target="_blank">GitHub Repository</a> | 
            <a href="https://colab.research.google.com/drive/1c3mMZntKuBEN02iZjtcS9DH4Vkwp6IQP?usp=sharing" target="_blank">Google Colab Research</a>
        </p>
    </div>
""", unsafe_allow_html=True)
