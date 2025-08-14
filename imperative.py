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
            padding-left: 15rem;
            padding-right: 15rem;
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

# === Second Aorist Imperative ===
second_aorist_active = [
    ["2nd", "λάβε", "λάβετε"],
    ["3rd", "λαβέτω", "λαβέτωσαν"]
]
second_aorist_middle = [
    ["2nd", "λαβοῦ", "λάβεσθε"],
    ["3rd", "λαβέσθω", "λαβέσθωσαν"]
]
show_two("2nd Aorist Act. Imp.", second_aorist_active,
         "2nd Aorist Mid./Pass. Imp.", second_aorist_middle)


from st_aggrid import AgGrid, GridOptionsBuilder

# Sample data: Greek words in a DataFrame
data = {
    "GreekWord": ["λῦε", "λύετε", "λυέτω", "λυέτωσαν", "λέγω"],
    "TableName": ["Noun Table", "Verb Table", "Text Table", "Verb Table", "Other Table"],
}
df = pd.DataFrame(data)

# Precomputed mapping of Greek word form to the list of tables it appears in
greek_form_tables = {
    "λόγος": ["Noun Table", "Text Table"],
    "λέγω": ["Verb Table", "Other Table"],
    "γράφω": ["Verb Table"]
}

# Function to provide tooltip content for each Greek word cell:
def get_tooltip(word, current_table):
    tables = greek_form_tables.get(word, [])
    # Exclude the current table from the tooltip list (optional)
    other_tables = [t for t in tables if t != current_table]
    if other_tables:
        return "Also in: " + ", ".join(other_tables)
    else:
        return "No other tables"

# Add a tooltip column corresponding to the GreekWord with tooltip text
df["Tooltip"] = df.apply(lambda row: get_tooltip(row["GreekWord"], row["TableName"]), axis=1)

# Configure AgGrid with tooltip on GreekWord column using tooltipField
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_column("GreekWord", tooltipField="Tooltip", header_name="Greek Word")
gb.configure_column("TableName", header_name="Table Name")
grid_options = gb.build()

st.write("Greek words table with tooltips showing other tables containing the same word form:")

AgGrid(df, gridOptions=grid_options, height=250, fit_columns_on_grid_load=True)
