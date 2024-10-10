import streamlit as st

def home_page():
    st.title("Welcome to the Earthquake Detection App")
    
    st.write("""
        This application provides insights and predictions related to earthquake events.
        You can input data about specific incidents to receive predictions on their potential impact.
    """)

    st.subheader("How to Use This App")
    st.write("""
        1. Navigate to the **Prediction** page from the sidebar to enter the earthquake data.
        2. Fill in the required fields, including location and disaster type.
        3. Click **Submit** to get predictions based on your inputs.
    """)

    st.image("App.py/broken-road-separating-into-two-parts-by-earthquake-city-ai-generative_123827-23739.jpg", caption="Earthquake Detection", use_column_width=True)

    # Interesting facts
    st.subheader("Did You Know?")
    st.write("""
        - Earthquakes can occur at any time and can happen anywhere in the world.
        - The largest earthquake ever recorded was a magnitude 9.5 in Chile in 1960.
        - Approximately 80% of the world's earthquakes occur along the Pacific Ring of Fire.
    """)

    # Additional resources or links
    st.subheader("Learn More")
    st.write("[US Geological Survey - Earthquake Hazards](https://www.usgs.gov/natural-hazards/earthquake-hazards)")
    st.write("[Earthquake Safety Tips](https://www.ready.gov/earthquakes)")

    # Optional: Interactive button for navigation with a unique key
    if st.button("Go to Prediction Page", key="go_to_prediction"):
        st.session_state.selected = 'Prediction'  # Assuming you handle navigation in the main app
