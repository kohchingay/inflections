import streamlit as st
import pandas as pd

st.title("Conjugation of λύω")
st.write("Inflections displayed in the format from the original reference PDF, with tense pairs side by side.")

# Helper function to show two tables side by side
def show_side_by_side(title_left, data_left, title_right, data_right):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(title_left)
        df_left = pd.DataFrame(data_left, columns=["Person", "Singular", "Plural"])
        st.table(df_left)
    with col2:
        st.subheader(title_right)
        df_right = pd.DataFrame(data_right, columns=["Person", "Singular", "Plural"])
        st.table(df_right)

# Present Indicative
present_active = [
    ["1st", "λύω", "λύομεν"],
    ["2nd", "λύεις", "λύετε"],
    ["3rd", "λύει", "λύουσι(ν)"]
]
present_mp = [
    ["1st", "λύομαι", "λυόμεθα"],
    ["2nd", "λύῃ", "λύεσθε"],
    ["3rd", "λύεται", "λύονται"]
]
show_side_by_side("Present Indicative Active", present_active, "Present Indicative Middle/Passive", present_mp)

# Imperfect Indicative
imperfect_active = [
    ["1st", "ἔλυον", "ἐλύομεν"],
    ["2nd", "ἔλυες", "ἐλύετε"],
    ["3rd", "ἔλυε(ν)", "ἔλυον"]
]
imperfect_mp = [
    ["1st", "ἐλυόμην", "ἐλυόμεθα"],
    ["2nd", "ἐλύου", "ἐλύεσθε"],
    ["3rd", "ἐλύετο", "ἐλύοντο"]
]
show_side_by_side("Imperfect Indicative Active", imperfect_active, "Imperfect Indicative Middle/Passive", imperfect_mp)

# Future Indicative
future_active = [
    ["1st", "λύσω", "λύσομεν"],
    ["2nd", "λύσεις", "λύσετε"],
    ["3rd", "λύσει", "λύσουσι(ν)"]
]
future_middle = [
    ["1st", "λύσομαι", "λυσόμεθα"],
    ["2nd", "λύσῃ", "λύσεσθε"],
    ["3rd", "λύσεται", "λύσονται"]
]
future_passive = [
    ["1st", "λυθήσομαι", "λυθησόμεθα"],
    ["2nd", "λυθήσῃ", "λυθήσεσθε"],
    ["3rd", "λυθήσεται", "λυθήσονται"]
]

# Future: show Middle and Passive side by side
show_side_by_side("Future Indicative Active", future_active, "Future Indicative Middle", future_middle)
show_side_by_side("Future Indicative Passive", future_passive, "", [])
