import streamlit as st


def CarPriceAnalysis():


    # Header
    st.title("Car Price Analysis")
    st.write("---")

    # About the project


    st.header("Car Price Analysis Project")

    st.markdown("""
    This project focuses on analyzing and predicting car prices using various data analysis and machine learning techniques. 
    It aims to provide insights into the factors influencing car prices and to develop predictive models for accurate price estimation.
    Key features include:

    1- **Exploratory Data Analysis (EDA):** Detailed analysis of the dataset to uncover patterns and relationships between features like brand, mileage, year, and price.
    
    2- **Data Cleaning and Preprocessing:** Handling missing values, encoding categorical features, and scaling data for model training.
    
    3- **Machine Learning Models:** Implementation of regression models (e.g., Linear Regression, Decision Trees, Random Forest) to predict car prices.
    
    4- **Feature Importance Analysis:** Identifying the most critical features that impact car prices.
    
    5- **Visualization:** Graphical representation of data and model results for better interpretability.
    
    6- **Model Evaluation:** Assessing the models' performance using metrics like Mean Absolute Error (MAE) and R-squared.
    """)

    st.write("---")

    # Technologies
    st.header("**Technologies Used**")
    st.write("Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn)")

    st.write("---")
    
    st.header("**Objective**")
    st.markdown('''
        To develop a data-driven solution that helps users or businesses estimate the price of a car based on its attributes. 
        This project can be useful for buyers, sellers, and dealerships aiming to make informed pricing decisions.
    ''')

    st.write("---")

    st.header("Correlation between price and other variables")

    st.write('-** With numerical Variables**:')


    columns = st.columns(3)

    columns[0].markdown('''
    **1- engine size:**

            As the engine-size goes up, the price goes up: this indicates a positive direct correlation between these two variables.   
            Engine size seems like a pretty good predictor of price since the regression line is almost a perfect diagonal line.
    ''')
    columns[0].image('CarPriceAnalysis/CarPriceAnalysis1.png', width = 300)
    

    columns[1].markdown('''
    **2- highway mpg:**

            As highway-mpg goes up, the price goes down: this indicates an inverse/negative relationship between these two variables. 
            Highway mpg could potentially be a predictor of price.
    ''')
    columns[1].image('CarPriceAnalysis/CarPriceAnalysis2.png', width = 300)


    columns[2].markdown('''
    **3- Peak rpm:**

            Peak rpm does not seem like a good predictor of the price at all since the regression line is close to horizontal. 
            Also, the data points are very scattered and far from the fitted line, showing lots of variability.
    ''')
    columns[2].image('CarPriceAnalysis/CarPriceAnalysis3.png', width = 300)
 

    st.write("---")

    st.write("- **With categorical Variables**:")

    columns = st.columns(2)
    columns[0].markdown('''
            **1- Body style:**

            We see that the distributions of price between the different body-style categories have a significant overlap,
            so body-style would not be a good predictor of price. Let's examine engine "engine-location" and "price"
    ''')
    columns[0].image('CarPriceAnalysis/CarPriceAnalysis4.png', width = 300)
    
    columns[1].markdown('''
            **2- Engine location:**

            we see that the distribution of price between these two engine-location categories, 
            front and rear, are distinct enough to take engine-location as a potential good predictor of price.

    ''')
    columns[1].image('CarPriceAnalysis/CarPriceAnalysis5.png', width = 300)

    st.write("---")


    st.markdown('''
            The main question we want to answer in this module is, "What are the main characteristics which have the most impact on the car price?".

            To get a better measure of the important characteristics, we look at the correlation of these variables with the car price. 
            In other words: how is the car price dependent on this variable?
            ''')

    st.write("---")

    columns = st.columns(2)
    columns[0].markdown('''
        This plot compares the actual car prices with the predicted prices. 
        Ideally, points should lie close to the red diagonal line, which represents perfect predictions. 
        In this case:
            Many points are near the line, indicating that the model predicts well for most cases.
            However, some deviations show where the model struggles to predict accurately.
    ''')
    columns[1].image('CarPriceAnalysis/CarPriceAnalysis6.png', width = 500)


    # Contact
    st.header("linke for python code")
    st.write(
        """
        [Coffee Sales Insights code](https://github.com/MaryamMaksour/Data_analysis_2_car_price/tree/main)  
    
        """
    )



if __name__ == "__CarPriceAnalysis__":
    CarPriceAnalysis()