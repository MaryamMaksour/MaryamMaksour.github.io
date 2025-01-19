import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def AudioClassification():

      
    # Title and Introduction
    st.title("Audio Classification: AST vs. HuBERT")
    st.write("---")
    
    st.header("Audio Classification: AST vs. HuBERT")

    st.write("""
    This project compares the performance of **Audio Spectrogram Transformer (AST)** and **HuBERT** on the Speech Commands dataset.
    We evaluate the models based on key metrics such as accuracy, F1-score, precision, and recall.
    """)

    st.write("---")
    # Metrics Data
    metrics = ['Eval Loss', 'Eval Accuracy', 'Eval F1 Score', 'Eval Precision', 'Eval Recall', 'Eval Runtime', 'Samples per Second', 'Epochs']
    ast_results = [0.1296, 0.9805, 0.9805, 0.9808, 0.9805, 5.63, 54.75, 3]
    hubert_results = [0.9912, 0.8831, 0.8570, 0.8447, 0.8831, 4.42, 69.75, 3]
    Observations = ["AST achieves a much lower loss, indicating better convergence.",
                    "AST outperforms HuBERT significantly in accuracy.",
                    "AST is better at balancing precision and recall.",
	                "AST is better at avoiding false positives.",
	                "AST is better at correctly identifying positive samples.",
                    "HuBERT is faster during evaluation, likely due to simpler input processing.",
	                "HuBERT processes more samples per second, likely due to raw waveform inputs.",
	                "Both models were trained for the same number of epochs."]
    
    st.write("---")
    # Visualization: Bar Chart
    st.subheader("Performance Metrics Comparison")

    # Create Bar Chart
    x = np.arange(len(metrics[:-3]))
    width = 0.35
    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(x - width/2, ast_results[:-3], width, label='AST', color='#000B58')
    rects2 = ax.bar(x + width/2, hubert_results[:-3], width, label='HuBERT', color='#006A67')
    ax.set_xlabel('Metrics')
    ax.set_title('Model Performance Comparison: AST vs. HuBERT')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics[:-3])
    ax.legend()

    # Annotate Bars
    for rect in rects1 + rects2:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}', 
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), 
                    textcoords="offset points", 
                    ha='center', va='bottom')

    # Display Plot
    st.pyplot(fig)

    st.write("---")
    # Detailed Results Table
    st.subheader("Detailed Results")
    st.write("""
    Below is the detailed evaluation results for each model:
    """)

    results_table = {
        "Metric": metrics,
        "AST": ast_results,
        "HuBERT": hubert_results,
        "Observations" : Observations
    }

       

    df = pd.DataFrame(results_table)

    st.write(df.to_html(index=False), unsafe_allow_html=True)
    st.write("---")
    # Conclusion
    st.subheader("Conclusion")
    st.write("""
    - **AST** outperforms **HuBERT** across all metrics, achieving higher accuracy, precision, recall, and F1-score.
    - While HuBERT is faster during evaluation, AST's use of Mel Spectrograms enables better overall performance on the Speech Commands dataset.
    """)
    st.write("---")
    st.header("linke for python code")
    st.write(
        """
        [Audio Classification: AST vs. HuBERT code](https://github.com/MaryamMaksour/Audio-Classification-AST-vs.-HuBERT/tree/main)  
    
        """
    )



if __name__ == "__AudioClassification__":
    AudioClassification()