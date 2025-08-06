import streamlit as st
import pandas as pd

st.title("Conjugation of λύω")
st.write("Inflections displayed in the format from the original reference PDF.")

# Helper function to display each table
def show_table(title, forms):
    st.subheader(title)
    df = pd.DataFrame(forms, columns=["Person", "Singular", "Plural"])
    st.table(df)

# Present Indicative Active
present_indicative_active = [
    ["1st", "λύω", "λύομεν"],
    ["2nd", "λύεις", "λύετε"],
    ["3rd", "λύει", "λύουσι(ν)"]
]
show_table("Present Indicative Active", present_indicative_active)

# Present Indicative Middle/Passive
present_indicative_mp = [
    ["1st", "λύομαι", "λυόμεθα"],
    ["2nd", "λύῃ", "λύεσθε"],
    ["3rd", "λύεται", "λύονται"]
]
show_table("Present Indicative Middle/Passive", present_indicative_mp)

# Imperfect Indicative Active
imperfect_indicative_active = [
    ["1st", "ἔλυον", "ἐλύομεν"],
    ["2nd", "ἔλυες", "ἐλύετε"],
    ["3rd", "ἔλυε(ν)", "ἔλυον"]
]
show_table("Imperfect Indicative Active", imperfect_indicative_active)

# Imperfect Indicative Middle/Passive
imperfect_indicative_mp = [
    ["1st", "ἐλυόμην", "ἐλυόμεθα"],
    ["2nd", "ἐλύου", "ἐλύεσθε"],
    ["3rd", "ἐλύετο", "ἐλύοντο"]
]
show_table("Imperfect Indicative Middle/Passive", imperfect_indicative_mp)

# Future Indicative Active
future_indicative_active = [
    ["1st", "λύσω", "λύσομεν"],
    ["2nd", "λύσεις", "λύσετε"],
    ["3rd", "λύσει", "λύσουσι(ν)"]
]
show_table("Future Indicative Active", future_indicative_active)

# Future Indicative Middle
future_indicative_middle = [
    ["1st", "λύσομαι", "λυσόμεθα"],
    ["2nd", "λύσῃ", "λύσεσθε"],
    ["3rd", "λύσεται", "λύσονται"]
]
show_table("Future Indicative Middle", future_indicative_middle)

# Future Indicative Passive
future_indicative_passive = [
    ["1st", "λυθήσομαι", "λυθησόμεθα"],
    ["2nd", "λυθήσῃ", "λυθήσεσθε"],
    ["3rd", "λυθήσεται", "λυθήσονται"]
]
show_table("Future Indicative Passive", future_indicative_passive)
