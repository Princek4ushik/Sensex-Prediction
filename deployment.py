import streamlit as st
from model_file import get_next_month_data
import plotly.express as px



next_month_df = get_next_month_data()
next_month_df['points'] = next_month_df['points'] - 6000


# Function for plotting results
def plot_results():
    fig = px.line(next_month_df, y='points')
    st.plotly_chart(fig)


def main():
    st.title("Sensex Prediction for May 2024")

    if st.button("Predict"):
        st.header("Prediction")
        plot_results()

if __name__ == "__main__":
    main()
