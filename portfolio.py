import streamlit as st
from PIL import Image

# --- PAGE CONFIG ---
st.set_page_config(page_title="Gaurav Deshmukh | Portfolio", layout="wide")

# --- HEADER ---
st.title("Gaurav Deshmukh")
st.subheader("Data Science | Data Analyst | Machine Learning Engineer")
st.write("Pune, India | gauravdeshmukh9970@gmail.com")

# --- ABOUT ---
st.header("About Me")
st.write("""
I'm a B.Tech Artificial Intelligence student passionate about **data science**, **machine learning**, **GEN Ai**, 
and **social impact analytics**.  
I create dashboards and models that convert raw data into meaningful insights.
""")

# --- SKILLS ---
st.header("Technical Skills")
skills ={
    "- Python : Pandas, NumPy, Scikit-learn":95,
    "- Data Visualization :Power BI, Tableau, Plotly,":90,
    "- Machine Learning :Random Forest, XGBoost":90,
    "- Natural Language Processing : NLTK, VADER":85,
    "- SQL & Databases":90,
    "- EXCEL":90,
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
- [PROJECT-1](https://github.com/gauravdeshmukh9970)
""")

# Women Empowerment NLP
st.subheader("2. Women Empowerment Sentiment Analysis (NLP)")
st.write("""
- **Tools:** Python (NLTK, VADER), Tableau  
- Processed 15K+ posts and survey responses to evaluate public sentiment.  
- Achieved **82% accuracy** in sentiment classification.
- [PROJECT-2](https://github.com/gauravdeshmukh9970)
""")

# NGO Fund Prediction
st.subheader("3. NGO Fund Allocation Prediction (ML)")
st.write("""
- **Tools:** Python (Scikit-learn, Power BI)  
- Built predictive model estimating project impact score.  
- Improved allocation efficiency by **20%**.
- [PROJECT-3](https://github.com/gauravdeshmukh9970)
""")

# --- RESUME & CERTIFICATES ---
st.header("Resume & Certificates")
st.download_button(
    label="Download My Resume",
    data=open("assets/RESUME.pdf", "rb").read(),
    file_name="RESUME.pdf"
)
st.write("- Data Science with GenAI – NareshIT")
st.write("- Machine Learning with Python – FreeCodeCamp")
st.download_button(
        label="CERTIFICATE - FreeCodeCamp",
        data=open("assets/freecodecamp.pdf", "rb").read(),
        file_name="freecodecamp.pdf"
)
st.write("- The Joy of Computing using Python – NPTEL")
st.download_button(
        label="CERTIFICATE - NPTEL",
        data=open("assets/NPTEL.pdf", "rb").read(),
        file_name="NPTEL.pdf"
)
st.write("- Data Analytics – Deloitte")
st.download_button(
        label="CERTIFICATE - Deloitte",
        data=open("assets/Deloitte.pdf", "rb").read(),
        file_name="Deloitte.pdf"
)
# --- CONTACT ---
st.header("Contact Me")
st.write("""
Email: [gauravdeshmukh9970@gmail.com](mailto:gauravdeshmukh9970@gmail.com)  
LinkedIn: [linkedin.com/in/gauravdeshmukh](https://linkedin.com/in/gauravdeshmukh)  
GitHub: [github.com/gauravdeshmukh9970](https://github.com/gauravdeshmukh9970)
""")

st.success("Thank you for visiting my portfolio!")
