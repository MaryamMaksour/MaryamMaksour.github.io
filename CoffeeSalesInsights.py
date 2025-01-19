import streamlit as st


def CoffeeSalesInsights():


    # Header
    st.title("Coffee Sales Insights")
    st.write("---")

    # About the project


    st.header("Coffee Sales Insights Project")

    st.markdown("""
    This project analyzes coffee sales data for Queens Café to uncover insights into customer behavior, 
    product performance, and pricing strategies. It demonstrates the use of business analytics to 
    drive data-informed decisions, such as optimizing product pricing and targeting underperforming regions.

    Key features include:
    
    1- **Data cleansing and preparation** 
    
    2- **Sales analysis by region and product type** 
    
    3- **Customer segmentation and profiling** 
    
    4- **Actionable recommendations for business growth**
    """)

    st.write("---")

    # Technologies
    st.header("**Technologies Used**")
    st.write("Excel: Data manipulation, formulas, and visualizations")

    st.write("---")
    

    st.image('coffeeSales/dash1.png')


 

    st.write("---")

    # Contact
    st.header("linke for python code")
    st.write(
        """
        [Coffee Sales Insights code](https://github.com/MaryamMaksour/Coffee--order)  
    
        """
    )



if __name__ == "__CoffeeSalesInsights__":
    CoffeeSalesInsights()