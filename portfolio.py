import streamlit as st
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="Gaurav Deshmukh | Portfolio", layout="wide")

# --- HEADER ---
st.title("Gaurav Deshmukh")
st.subheader("Data Analyst | Machine Learning Engineer | Python Developer")
st.write("Pune, India | gauravdeshmukh9970@gmail.com")

# --- ABOUT ---
st.header("About Me")
st.write("""
I'm a B.Tech Artificial Intelligence student passionate about **data analysis**, **machine learning**, 
and **social impact analytics**.  
I create dashboards and models that convert raw data into meaningful insights.
""")

# --- SKILLS ---
st.header("Technical Skills")
skills = {
    "Python (Pandas, NumPy, Scikit-learn)": 95,
    "Data Visualization (Power BI, Tableau, Plotly)": 92,
    "Machine Learning (Random Forest, XGBoost)": 85,
    "Natural Language Processing (NLTK, VADER)": 80,
    "SQL & Databases": 75
}
for skill, val in skills.items():
    st.write(f"{skill}")
    st.progress(val / 100)

# --- PROJECTS SECTION ---
st.header("Featured Projects")

# CSR Dashboard
st.subheader("1. Social Impact Data Dashboard (CSR Analytics)")
st.write("""
- **Tools:** Power BI, Python (Pandas, Plotly)
- Analyzed 50K+ CSR records to track beneficiaries and fund utilization across 6 states.
- Improved decision-making efficiency by **30%**.
""")

# Women Empowerment NLP
st.subheader("2. Women Empowerment Sentiment Analysis (NLP)")
st.write("""
- **Tools:** Python (NLTK, VADER), Tableau  
- Processed 15K+ posts and survey responses to evaluate public sentiment.  
- Achieved **82% accuracy** in sentiment classification.
""")

# NGO Fund Prediction
st.subheader("3. NGO Fund Allocation Prediction (ML)")
st.write("""
- **Tools:** Python (Scikit-learn, Power BI)  
- Built predictive model estimating project impact score.  
- Improved allocation efficiency by **20%**.
""")

# --- RESUME & CERTIFICATES ---
st.header("Resume & Certificates")
st.download_button(
    label="Download My Resume",
    data=open("assets/RESUME.docx", "rb").read(),
    file_name="RESUME.docx"
)
st.write("- Data Science with GenAI – NareshIT")
st.write("- Machine Learning with Python – FreeCodeCamp")
st.write("- The Joy of Computing using Python – NPTEL")
st.write("- Data Analytics – Deloitte")

# --- CONTACT ---
st.header("Contact Me")
st.write("""
Email: [gauravdeshmukh9970@gmail.com](mailto:gauravdeshmukh9970@gmail.com)  
LinkedIn: [linkedin.com/in/gauravdeshmukh](https://linkedin.com/in/gauravdeshmukh)  
GitHub: [github.com/gauravdeshmukh9970](https://github.com/gauravdeshmukh9970)
""")

st.success("Thank you for visiting my portfolio!")
