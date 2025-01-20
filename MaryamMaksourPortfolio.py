import streamlit as st
import CustomerChurnAnalysis, CoffeeSalesInsights, CarPriceAnalysis
import PDFIntelligentAssistant, AudioClassification, GenderBiasClassificationModels
import AIPersonalTrainer, VolumeControl

# Page Configuration
st.set_page_config(page_title="Maryam Maksour Portfolio", page_icon=":sparkles:", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f5f5;
        background: linear-gradient(180deg, rgba(0,45,105,1) 0%, rgba(0,98,130,1) 50%, rgba(0,155,145,1) 100%);

        background-size: cover;
        background-position: center;
    }

    div.stButton > button:first-child {
        background-color: transparent;
        color: #ffffff;
        border: 2px solid #0073e6;
        border-radius: 4px;
        padding: 8px 20px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
    }
    div.stButton > button:first-child:hover {
        background-color: #0073e6;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Header
st.title("Maryam Maksour Portfolio")
st.write("Data Scientist | Machine Learning | AI Developer")
st.write("---")

# About Me
about_me = """
    I am a passionate Data Scientist with expertise in machine learning, natural language processing (NLP), and data analysis. My technical skills include
    Python, C++, and advanced data tools, enabling me to build predictive models, analyze complex datasets, and derive actionable insights.

    Over the years, I have gained hands-on experience in AI development, competitive programming, and mentoring, 
    which has sharpened my problem-solving and collaboration skills. I am driven by a desire to tackle real-world challenges, 
    innovate with data-driven solutions, and contribute to impactful projects.

    Currently, I am seeking opportunities to apply my skills in dynamic and collaborative environments, helping organizations leverage data to achieve their strategic goals.
    """

st.header("About Me")
st.write(about_me)

st.write("---")

# Experience

experiences = [ 
    (
        "Competitive Programming Coach**, Arab Private University for Science and Technology (2024)",
        ["Led teams in competitive programming, achieving notable qualifications in SCPCP and ACPC.",  
         "Mentored students in problem-solving and critical thinking."
        ]
    ),
    (
        "Machine Learning Intern**, SMSM AI (March 2024 - June 2024)",
        ["Preprocessed and analyzed audio data to fine-tune Whisper AI models."]
    ),
    (
        "AI Engineer Intern**, RightClick Company (2020 - 2021)",
        ["Collaborated on AI projects, contributing to real-world applications as the youngest AI engineer in the company."]
    ),
]

st.header("Experience")

for title, experiences_list in experiences:
    st.write(f"**{title}")
    for experience in experiences_list:
        st.write(f"- {experience}")

st.write("---")

# Projects
st.header("Projects")
st.write("Here are some of my notable projects:")


run = "null"

columns = st.columns(3)

    
columns[0].write("#### **Data Scince / Data Analysis**")
if columns[0].button("Customer Churn Analysis"):
    run = CustomerChurnAnalysis.CustomerChurnAnalysis
if columns[0].button("Car Price Analysis"):
    run = CarPriceAnalysis.CarPriceAnalysis
if columns[0].button("Coffee Sales Insights"):
    run = CoffeeSalesInsights.CoffeeSalesInsights

columns[1].write("#### **AI project**")
if columns[1].button("PDF Intelligent Assistant"):
    run = PDFIntelligentAssistant.PDFIntelligentAssistant
if columns[1].button("Audio classification"):
    run = AudioClassification.AudioClassification
if columns[1].button("Gender bias classification models"):
    run = GenderBiasClassificationModels.GenderBiasClassificationModels

columns[2].write("#### **Computer Vision project**")
if columns[2].button("AI Personal Trainer"):
    run = AIPersonalTrainer.AIPersonalTrainer
if columns[2].button("Gesture Volume Control"):
    run = VolumeControl.VolumeControl


if run != "null":
    run()



st.write("---")





# Skills
st.header("Skills")
columns = st.columns(3)

columns[0].write("### Programming Languages")
columns[0].write(
    """
    - Python (Pandas, NumPy, Matplotlib, Seaborn)
    - C++ (Advanced)
    - SQL
    - R (Basics)
    """
)

columns[1].write("### Machine Learning & AI")
columns[1].write(
    """    
    - TensorFlow, Scikit-learn
    - Natural Language Processing (NLP)
    - LangChain, HuggingFace
    - Linear Regression, K-means Clustering, SVM
    """
)

columns[2].write("### Data Analysis & Visualization")
columns[2].write(
    """    
    - Data Cleaning and Wrangling (Pandas, Excel)
    - Visualization Tools (Matplotlib, Seaborn, Power BI)
    """
)
st.write("---")
columns = st.columns(3)

columns[0].write("### Development Tools & Frameworks")
columns[0].write(
    """
    - FastAPI, REST APIs
    - JSON
    - Streamlit
    """
)

columns[1].write("### Soft Skills")
columns[1].write(
    """    
    - Problem-solving and critical thinking
    - Leadership and mentoring
    - Collaboration and communication
    """
)

columns[2].write("### Languages")
columns[2].write(
    """    
    - Arabic (Native)
    - English (Advanced - B2 Level)
    """
)



st.write("---")

# Contact
st.header("Contact Me")
st.write(
    """
    - Email: [maryammaksour@gmail.com](mailto:maryammaksour@gmail.com)  
    - LinkedIn: [linkedin.com/in/maryam-maksour](https://www.linkedin.com/in/maryam-maksour)  
    - GitHub: [github.com/MaryamMaksour](https://github.com/MaryamMaksour)  
    - Codeforces: [codeforces.com/profile/Mmak](https://codeforces.com/profile/Mmak)  
    - Phone: +971561209106  
    """
)
