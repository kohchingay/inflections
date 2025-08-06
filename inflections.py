import streamlit as st
import pandas as pd

st.title("Conjugation of λύω")
st.write("Grouped by tense and voice, with duplicate forms removed for clarity.")

# Helper to show two tables side by side
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

# Present & Imperfect Indicative Active (grouped)
indicative_active = [
    ["1st", "λύω / ἔλυον", "λύομεν / ἐλύομεν"],
    ["2nd", "λύεις / ἔλυες", "λύετε / ἐλύετε"],
    ["3rd", "λύει / ἔλυε(ν)", "λύουσι(ν) / ἔλυον"]
]

# Present & Imperfect Indicative Middle/Passive (grouped)
indicative_mp = [
    ["1st", "λύομαι / ἐλυόμην", "λυόμεθα / ἐλυόμεθα"],
    ["2nd", "λύῃ / ἐλύου", "λύεσθε / ἐλύεσθε"],
    ["3rd", "λύεται / ἐλύετο", "λύονται / ἐλύοντο"]
]

show_side_by_side("Present & Imperfect Indicative Active", indicative_active,
                  "Present & Imperfect Indicative Middle/Passive", indicative_mp)

# Future Indicative Active
future_active = [
    ["1st", "λύσω", "λύσομεν"],
    ["2nd", "λύσεις", "λύσετε"],
    ["3rd", "λύσει", "λύσουσι(ν)"]
]

# Future Indicative Middle
future_middle = [
    ["1st", "λύσομαι", "λυσόμεθα"],
    ["2nd", "λύσῃ", "λύσεσθε"],
    ["3rd", "λύσεται", "λύσονται"]
]

# Future Indicative Passive
future_passive = [
    ["1st", "λυθήσομαι", "λυθησόμεθα"],
    ["2nd", "λυθήσῃ", "λυθήσεσθε"],
    ["3rd", "λυθήσεται", "λυθήσονται"]
]

show_side_by_side("Future Indicative Active", future_active,
                  "Future Indicative Middle", future_middle)

show_side_by_side("Future Indicative Passive", future_passive, "", [])
