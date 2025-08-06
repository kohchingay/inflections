import streamlit as st
import pandas as pd

st.title("Conjugation of λύω")
st.write("Full indicative inflections of λύω organized by tense and voice.")

# Helper to show two tables side by side
def show_two(title1, data1, title2, data2):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader(title1)
        df1 = pd.DataFrame(data1, columns=["Person", "Singular", "Plural"])
        st.table(df1)
    with col2:
        st.subheader(title2)
        df2 = pd.DataFrame(data2, columns=["Person", "Singular", "Plural"])
        st.table(df2)

# Helper to show three tables side by side
def show_three(title1, data1, title2, data2, title3, data3):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader(title1)
        df1 = pd.DataFrame(data1, columns=["Person", "Singular", "Plural"])
        st.table(df1)
    with col2:
        st.subheader(title2)
        df2 = pd.DataFrame(data2, columns=["Person", "Singular", "Plural"])
        st.table(df2)
    with col3:
        st.subheader(title3)
        df3 = pd.DataFrame(data3, columns=["Person", "Singular", "Plural"])
        st.table(df3)

# Present Subjunctive
present_active = [
    ["1st", "λύω", "λύωμεν"],
    ["2nd", "λύῃς", "λύητε"],
    ["3rd", "λύῃ", "λύωσι(ν)"]
]
present_mp = [
    ["1st", "λύωμαι", "λυώμεθα"],
    ["2nd", "λύῃ", "λύησθε"],
    ["3rd", "λύηται", "λύωνται"]
]
show_two("Present Subjunctive Active", present_active, "Present Subjunctive Middle/Passive", present_mp)

# Aorist Subjunctive
aorist_active = [
    ["1st", "λύσω", "λύσωμεν"],
    ["2nd", "λύσῃς", "λύσητε"],
    ["3rd", "λύσῃ", "λύσωσι(ν)"]
]
aorist_middle = [
    ["1st", "λύσωμαι", "λυσώμεθα"],
    ["2nd", "λύσῃ", "λύσησθε"],
    ["3rd", "λύσηται", "λύσωνται"]
]
aorist_passive = [
    ["1st", "λυθῶ", "λυθῶμεν"],
    ["2nd", "λυθῇς", "λυθῆτε"],
    ["3rd", "λυθῇ", "λυθῶσι(ν)"]
]
show_three("Aorist Subjunctive Active", aorist_active, "Aorist Subjunctive Middle", aorist_middle, "Aorist Subjunctive Passive", aorist_passive)

# Perfect Subjunctive
perfect_active = [
    ["1st", "λελύκω", "λελύκωμεν"],
    ["2nd", "λελύκῃς", "λελύκητε"],
    ["3rd", "λελύκῃ", "λελύκωσι(ν)"]
]
perfect_mp = [
    ["1st", "λελύκωμαι", "λελυκώμεθα"],
    ["2nd", "λελύκῃ", "λελύκησθε"],
    ["3rd", "λελύκηται", "λελυκῶνται"]
]
show_two("Perfect Subjunctive Active", perfect_active, "Perfect Subjunctive Middle/Passive", perfect_mp)
