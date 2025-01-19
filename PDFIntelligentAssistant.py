import streamlit as st


def PDFIntelligentAssistant():


    # Header
    st.title("PDF Intelligent Assistant")
    st.write("---")

    # About the project


    st.header("PDF Intelligent Assistant Project")

    st.video("PDFs/chatPDFAPP.mp4", loop=True, autoplay=True, muted=True)

    st.title("Interactive PDF Chatbot")
    st.markdown(
        """
        ### About the Project

        This application allows users to upload PDF documents and interact with their content via a chatbot interface.
        Using advanced AI models, it processes the uploaded PDFs, extracts their content, and enables users to ask questions
        and receive accurate, context-aware answers.

        **Key Features:**
        - Upload multiple PDFs for content analysis.
        - Semantic search powered by embeddings from Google Generative AI.
        - Contextual question-answering with detailed, accurate responses.
        - User-friendly interface for easy interaction.

        **Technologies Used:**
        - **Streamlit**: For building the web interface.
        - **PyPDF2**: For extracting text from PDF files.
        - **LangChain**: For embedding and QA chain integration.
        - **Google Generative AI**: For embeddings and conversational models.
        - **FAISS**: Local vector database for semantic search.

        **How It Works:**
        1. Upload your PDFs.
        2. Process the content to create embeddings and store them in a vector database.
        3. Ask questions and get precise answers based on the document content.

        **Use Cases:**
        - Corporate knowledge management.
        - Educational tools for interactive learning.
        - Document search and query for legal or research purposes.

        """
    )

    st.write("---")


    # Contact
    st.header("linke for python code")
    st.write(
        """
        [PDF Intelligent Assistant](https://github.com/MaryamMaksour/Chat-with-multiple-PDFs)  
    
        """
    )



if __name__ == "__PDFIntelligentAssistant__":
    PDFIntelligentAssistant()