import streamlit as st
import pandas as pd

# Title and description
st.title("Conjugation of λύω")
st.write("This table shows the Greek verb λύω conjugated across various tenses, voices, and moods.")

# Define the data
data = {
    "Tense": ["Present", "Imperfect", "Future", "Aorist", "Perfect", "Pluperfect"],
    "Active": ["λύω", "ἔλυον", "λύσω", "ἔλυσα", "λέλυκα", "ἐλελύκειν"],
    "Middle": ["λύομαι", "ἐλυόμην", "λύσομαι", "ἐλυσάμην", "λέλυμαι", "ἐλελύμην"],
    "Passive": ["λύομαι", "ἐλυόμην", "λυθήσομαι", "ἐλύθην", "λέλυμαι", "ἐλελύμην"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the table
st.table(df)
