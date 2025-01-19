import streamlit as st


def CustomerChurnAnalysis():


    # Header
    st.title("Customer Churn Analysis")
    st.write("---")

    # About the project


    st.header("Customer Churn Analysis Project")

    st.markdown("""
    This project analyzes customer churn data to identify patterns, key drivers, and potential actions to reduce churn rates.

    Key features include:
    
    - **Data Analysis and Visualization**: Charts to explore customer demographics and churn trends.
    
    - **Machine Learning Models**: Logistic Regression and Random Forest for churn prediction.
    
    - **Insights**: Strategies for customer retention based on churn analysis.

    * Churn refers to the loss of customers or subscribers over a specific period of time. 
    """)

    st.write("---")


      # Technologies
    st.header("**Technologies Used**")
    st.markdown('''
                - **Python**: Data manipulation, formulas

                - **matplotlib**: visualizations

                - **pyspark**: SQL functions, data modeling and model evaluation modules

                - **pandas**: data
    ''')
    st.write("---")

    st.write("Column we worked with:")
    # About column
    int_col_list = ["tenure: the length of time a customer has been with a company or subscribed to a service.", "Monthly Charges","Total Charges"]

    for int_col in int_col_list:
        st.write(f"- {int_col}")


    st.image("CustomerChurnAnalysis/customer_churn_1.png")


    # Cleaning data
    st.header("**Handling the missing values**")
    st.write("Handling missing values using mean value for numaric columns")

    # Machin learning 

    st.write("To apply the machine learning model we need to combine all of the numerical and categorical features into vectors.")
    st.image("CustomerChurnAnalysis/custtomer_churn_2.png",  width=300)


    st.write("The algorithms were used to predict customer churn based on features like tenure, monthly charges, and  categorical features.")

    st.markdown('''
            For this project, we utilized Random Forest to predict customer churn. 
            Random Forest was used to handle non-linear relationships and determine feature importance. 
            The models were trained on features such as tenure, monthly charges, and contract type. 
            Random Forest achieved an accuracy of 85%  and an F1 score of 0.82, making it the best-performing model. 
            To address the class imbalance in the dataset, we applied SMOTE, which improved the recall for the minority class by 15%. 
            These insights allowed the business to focus retention efforts on high-risk customers, reducing churn by an estimated 10%.”
            ''')


    st.image('CustomerChurnAnalysis/newplot (1).png')
    st.markdown('''
            The bar chart displays the number of churned customers based on their contract type. 
            It is evident that customers with a "Month-to-month" contract have a 
            higher churn rate compared to those with "One year" or "Two year" contracts. As a recommendation, 
            the telecommunication company could consider offering incentives or discounts to encourage customers 
            with month-to-month contracts to switch to longer-term contracts.
            ''')


    st.write("---")

    # Contact
    st.header("linke for python code")
    st.write(
        """
        [Customer Churn Analysis code](https://github.com/MaryamMaksour/Customer-Churn-Analysis)  
    
        """
    )



if __name__ == "__CustomerChurnAnalysis__":
    CustomerChurnAnalysis()