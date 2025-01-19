import streamlit as st
import CustomerChurnAnalysis, CoffeeSalesInsights, CarPriceAnalysis
import PDFIntelligentAssistant, AudioClassification, GenderBiasClassificationModels
import AIPersonalTrainer, VolumeControl

# Page Configuration
st.set_page_config(page_title="Maryam Maksour Portfolio", page_icon=":sparkles:", layout="wide")


# Header
st.title("Maryam Maksour Portfolio")
st.write("Results-driven Data Scientist | Machine Learning Enthusiast | AI Developer")
st.write("---")

# About Me
about_me = """
    I am a Data Scientist with expertise in machine learning, natural language processing (NLP), and data analysis. 
    Proficient in Python, C++, and advanced data tools, I am passionate about solving real-world challenges and mentoring others in the field. 
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
    
#    #("Student Admission Prediction", "https://github.com/MaryamMaksour/Admission-Prediction-/tree/main"),
# chat bot
# Finger counter project Code


#############################################


st.write("---")

# Skills
st.header("Skills")
columns = st.columns(2)

columns[0].write("### Programming & Tools")
columns[0].write(
    """
    - Python, C++
    - Pandas, NumPy, Matplotlib, Seaborn
    - TensorFlow, Scikit-learn, HuggingFace, LangChain
    - SQL, FastAPI, REST APIs
    """
)

columns[1].write("### Additional Skills")
columns[1].write(
    """
    - Power BI (Basics)
    - R (Basics)
    - Excel (Advanced)
    - Arabic (Native), English (B2)
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
