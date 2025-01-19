import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def GenderBiasClassificationModels():
 
    # App title and introduction
    st.title("Gender Bias Classification")
    st.write("---")

    st.header("Gender Bias Classification Project") 

    st.markdown(
        """
        ### Overview
        This project aims to classify gender bias in textual data using advanced machine learning and deep learning models. 
        Developed as part of the **HerWill Datathon**, it showcases expertise in data handling, model training, and performance evaluation.
        
        #### Data
        The dataset used consists of text samples annotated for gender bias. It was preprocessed to remove noise and tokenized to prepare it for model input.
        
        #### Goal
        The goal is to build efficient models that can accurately identify gender bias in text while considering the trade-off between model complexity and performance.
        """
    )

    st.write("---")

    # Model Description
    st.header("Models Used")
    st.markdown(
        """
        Five transformer-based models were trained and evaluated:
        - **roberta-base**
        - **bert-base-uncased**
        - **XLNet**
        - **bert-tiny**
        - **Albert**

        These models were chosen to explore a balance between performance (accuracy and F1-score) and computational cost (number of parameters).
        """
    )
    st.write("---")
    # Model Comparison Section
    st.header("Model Comparison")

    # Example data for visualization
    model_names = ['roberta-base', 'bert-base-uncased', 'XLNet', 'bert-tiny', 'Albert']
    nop_values = [85649668.0, 85649668.0,57299716.0, 413828.0, 7780868.0] 
    accuracy_values = [0.9707142857142858, 0.9635714285714285,0.9678571428571429, 0.9492857142857143, 0.9642857142857143]  
    f1_values = [0.9709422855623562, 0.9636008112584432, 0.9681725335409271, 0.9481329292441959, 0.9643132557773489]  



    # Visualization
    st.markdown("### Number of Parameters vs Model Performance")
    fig, axes = plt.subplots(2, 1, figsize=(10, 6))

    # Plot NOP values
    axes[0].bar(model_names, nop_values, color='blue')
    axes[0].set_xlabel("Models")
    axes[0].set_ylabel("Number of Parameters (NOP)")
    axes[0].set_title("Number of Parameters for each model")

    # Plot Accuracy and F1 values
    axes[1].plot(model_names, accuracy_values, marker='o', label="Accuracy")
    axes[1].plot(model_names, f1_values, marker='o', label="F1-score")
    axes[1].set_xlabel("Models")
    axes[1].set_ylabel("Metrics")
    axes[1].set_title("Accuracy and F1-score for each model")
    axes[1].legend()

    plt.tight_layout()
    st.pyplot(fig)

    st.write("---")
    # Analysis
    st.markdown(
        """
        ### Analysis
        - **bert-tiny** has the smallest number of parameters, but it also has a significantly lower F1-score.
        - **XLNet** has fewer parameters than roberta-base and bert-base-uncased but still maintains a high F1-score.
        - **Albert** provides a good balance between model size and performance, making it an efficient choice for practical applications.

        ### Conclusion
        XLNet and Albert emerge as strong contenders for balancing computational cost and model performance in this task.
        """
    )
    st.write("---")

    st.header("linke for python code")
    st.write(
        """
        [Gender Bias Classification code](https://github.com/MaryamMaksour/gender-bias-classification-model/tree/main)  
    
        """
    )


if __name__ == "__GenderBiasClassificationModels__":
    GenderBiasClassificationModels()