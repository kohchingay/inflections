# Imperative Mood

import streamlit as st
import pandas as pd

st.title("Imperative of λύω")

# === Reduce margins and allow more space ===
st.markdown(
    """
    <style>
        /* Reduce main content max-width */
        .block-container {
            max-width: 95%;
            padding-left: 2rem;
            padding-right: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

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

# === Present Imperative ===
present_active = [
    ["2nd", "λῦε", "λύετε"],
    ["3rd", "λυέτω", "λυέτωσαν"]
]
present_middle_passive = [
    ["2nd", "λύου", "λύεσθε"],
    ["3rd", "λυέσθω", "λυέσθωσαν"]
]

# Show Present: Active + Middle/Passive merged
show_two("Pres. Αct. Imp.", present_active,
         "Pres. Mid./Pass. Imp.", present_middle_passive)

# === Aorist Imperative ===
aorist_active = [
    ["2nd", "λῦσον", "λύσατε"],
    ["3rd", "λυσάτω", "λυσάτωσαν"]
]
aorist_middle = [
    ["2nd", "λῦσαι", "λύσασθε"],
    ["3rd", "λυσάσθω", "λυσάσθωσαν"]
]
aorist_passive = [
    ["2nd", "λύθητι", "λύθητε"],
    ["3rd", "λυθήτω", "λυθήτωσαν"]
]

# Show Aorist as three separate tables
show_three("Aor. Act. Imp.", aorist_active,
           "Aor. Mid. Imp.", aorist_middle,
           "Aor. Pass. Imp.", aorist_passive)
