
import streamlit as st
import pandas as pd
import ollama

st.set_page_config(page_title="Factory Ghost", page_icon="🏭")

st.title("🏭 Factory Ghost")
st.subheader("Industrial Motor Monitoring Dashboard")

try:
    data = pd.read_csv("motor_data.csv")

    latest = data.iloc[-1]

    col1, col2, col3 = st.columns(3)

    col1.metric("Temperature", f"{latest['Temperature_C']} °C")
    col2.metric("Vibration", f"{latest['Vibration_mm_s']} mm/s")
    col3.metric("Current", f"{latest['Current_A']} A")

    if (data["Status"] == "WARNING").any():
        st.warning("Motor warning detected in the simulation!")
    else:
        st.success("All simulated readings are normal.")

    
    st.subheader("🤖 AI Motor Assistant")

    if st.button("Explain Motor Condition with AI"):
        with st.spinner("Gemma is analyzing the simulated readings..."):
            try:
                response = ollama.chat(
                    model="gemma2:2b",
                    messages=[
                        {
                            "role": "user",
                            "content": (
                                f"Explain these simulated motor readings "
                                f"in simple English. Temperature: "
                                f"{latest['Temperature_C']} °C, vibration: "
                                f"{latest['Vibration_mm_s']} mm/s, current: "
                                f"{latest['Current_A']} A, status: "
                                f"{latest['Status']}. Explain possible "
                                f"causes and safe next steps. These are "
                                f"simulated readings, not a real diagnosis."
                            )
                        }
                    ]
                )
                st.write(response["message"]["content"])
            except Exception as e:
                st.error(f"AI connection error: {e}")


    st.subheader("Temperature History")
    st.line_chart(data.set_index("Reading")["Temperature_C"])

    st.subheader("Vibration History")
    st.line_chart(data.set_index("Reading")["Vibration_mm_s"])

    st.subheader("All Motor Readings")
    st.dataframe(data, width="stretch")

except FileNotFoundError:
    st.error("motor_data.csv not found. Run motor_simulator.py first.")

