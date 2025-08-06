import streamlit as st
import pandas as pd

st.title("Full Conjugation of λύω")
st.write("This table shows the full inflection of the Greek verb λύω across tense, voice, mood, person, and number.")

# Define the data
data = [
    # Present Indicative Active
    ["Present", "Indicative", "Active", "1st", "Singular", "λύω"],
    ["Present", "Indicative", "Active", "2nd", "Singular", "λύεις"],
    ["Present", "Indicative", "Active", "3rd", "Singular", "λύει"],
    ["Present", "Indicative", "Active", "1st", "Plural", "λύομεν"],
    ["Present", "Indicative", "Active", "2nd", "Plural", "λύετε"],
    ["Present", "Indicative", "Active", "3rd", "Plural", "λύουσι(ν)"],

    # Present Indicative Middle/Passive
    ["Present", "Indicative", "Middle/Passive", "1st", "Singular", "λύομαι"],
    ["Present", "Indicative", "Middle/Passive", "2nd", "Singular", "λύει"],
    ["Present", "Indicative", "Middle/Passive", "3rd", "Singular", "λύεται"],
    ["Present", "Indicative", "Middle/Passive", "1st", "Plural", "λυόμεθα"],
    ["Present", "Indicative", "Middle/Passive", "2nd", "Plural", "λύεσθε"],
    ["Present", "Indicative", "Middle/Passive", "3rd", "Plural", "λύονται"],

    # Imperfect Indicative Active
    ["Imperfect", "Indicative", "Active", "1st", "Singular", "ἔλυον"],
    ["Imperfect", "Indicative", "Active", "2nd", "Singular", "ἔλυες"],
    ["Imperfect", "Indicative", "Active", "3rd", "Singular", "ἔλυε(ν)"],
    ["Imperfect", "Indicative", "Active", "1st", "Plural", "ἐλύομεν"],
    ["Imperfect", "Indicative", "Active", "2nd", "Plural", "ἐλύετε"],
    ["Imperfect", "Indicative", "Active", "3rd", "Plural", "ἔλυον"],

    # Imperfect Indicative Middle/Passive
    ["Imperfect", "Indicative", "Middle/Passive", "1st", "Singular", "ἐλυόμην"],
    ["Imperfect", "Indicative", "Middle/Passive", "2nd", "Singular", "ἐλύου"],
    ["Imperfect", "Indicative", "Middle/Passive", "3rd", "Singular", "ἐλύετο"],
    ["Imperfect", "Indicative", "Middle/Passive", "1st", "Plural", "ἐλυόμεθα"],
    ["Imperfect", "Indicative", "Middle/Passive", "2nd", "Plural", "ἐλύεσθε"],
    ["Imperfect", "Indicative", "Middle/Passive", "3rd", "Plural", "ἐλύοντο"],

    # Future Indicative Active
    ["Future", "Indicative", "Active", "1st", "Singular", "λύσω"],
    ["Future", "Indicative", "Active", "2nd", "Singular", "λύσεις"],
    ["Future", "Indicative", "Active", "3rd", "Singular", "λύσει"],
    ["Future", "Indicative", "Active", "1st", "Plural", "λύσομεν"],
    ["Future", "Indicative", "Active", "2nd", "Plural", "λύσετε"],
    ["Future", "Indicative", "Active", "3rd", "Plural", "λύσουσι(ν)"],

    # Future Indicative Middle
    ["Future", "Indicative", "Middle", "1st", "Singular", "λύσομαι"],
    ["Future", "Indicative", "Middle", "2nd", "Singular", "λύσῃ"],
    ["Future", "Indicative", "Middle", "3rd", "Singular", "λύσεται"],
    ["Future", "Indicative", "Middle", "1st", "Plural", "λυσόμεθα"],
    ["Future", "Indicative", "Middle", "2nd", "Plural", "λύσεσθε"],
    ["Future", "Indicative", "Middle", "3rd", "Plural", "λύσονται"],

    # Future Indicative Passive
    ["Future", "Indicative", "Passive", "1st", "Singular", "λυθήσομαι"],
    ["Future", "Indicative", "Passive", "2nd", "Singular", "λυθήσῃ"],
    ["Future", "Indicative", "Passive", "3rd", "Singular", "λυθήσεται"],
    ["Future", "Indicative", "Passive", "1st", "Plural", "λυθησόμεθα"],
    ["Future", "Indicative", "Passive", "2nd", "Plural", "λυθήσεσθε"],
    ["Future", "Indicative", "Passive", "3rd", "Plural", "λυθήσονται"],
]

# Create DataFrame
columns = ["Tense", "Mood", "Voice", "Person", "Number", "Form"]
df = pd.DataFrame(data, columns=columns)

# Display the table
st.dataframe(df)
