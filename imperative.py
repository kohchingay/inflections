# Imperative Mood

import streamlit as st
import pandas as pd

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

# Present Imperative
present_active = [
    ["2nd", "λύε", "λύετε"],
    ["3rd", "λυέτω", "λυόντων"]
]
present_middle = [
    ["2nd", "λύου", "λύεσθε"],
    ["3rd", "λυέσθω", "λυέσθων"]
]
present_passive = present_middle  # identical in form
show_three("Present Imperative Active", present_active, "Present Imperative Middle", present_middle, "Present Imperative Passive", present_passive)

# Aorist Imperative
aorist_active = [
    ["2nd", "λῦσον", "λύσατε"],
    ["3rd", "λυσάτω", "λυσάντων"]
]
aorist_middle = [
    ["2nd", "λύσαι", "λύσασθε"],
    ["3rd", "λυσάσθω", "λυσάσθων"]
]
aorist_passive = [
    ["2nd", "λύθητι", "λύθητε"],
    ["3rd", "λυθήτω", "λυθέντων"]
]
show_three("Aorist Imperative Active", aorist_active, "Aorist Imperative Middle", aorist_middle, "Aorist Imperative Passive", aorist_passive)

# Perfect Imperative
perfect_active = [
    ["2nd", "λελύκε", "λελύκετε"],
    ["3rd", "λελυκέτω", "λελυκόντων"]
]
perfect_middle = [
    ["2nd", "λελύσο", "λελύσθε"],
    ["3rd", "λελύσθω", "λελύσθων"]
]
perfect_passive = [
    ["2nd", "λελύσο", "λελύσθε"],
    ["3rd", "λελύσθω", "λελύσθων"]
]
show_three("Perfect Imperative Active", perfect_active, "Perfect Imperative Middle", perfect_middle, "Perfect Imperative Passive", perfect_passive)
