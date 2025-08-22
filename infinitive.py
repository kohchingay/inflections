import streamlit as st
import pandas as pd

st.title("Imperative Mood of λύω")

# = CSS styling =
st.markdown("""
    <style>
        .block-container {
            max-width: unset;
            padding-left: 15rem;
            padding-right: 15rem;
            padding-top: 2rem;
            padding-bottom: 1rem;
            overflow-x: auto;
        }

        @media (max-width: 768px) {
            .block-container {
                padding-left: 0.5rem;
                padding-right: 0.5rem;
            }
            table {
                font-size: 0.85rem;
            }
        }

        table {
            width: auto;
            margin: auto;
            border-collapse: collapse;
        }
        th, td {
            padding: 0.4rem 1rem;
            text-align: center;
            white-space: nowrap;
            border-bottom: 1px solid #ddd;
        }
        th {
            font-weight: bold;
            border-bottom: 2px solid #666;
        }
        h1, h2, h3 {
            font-size: 1.2rem;
            margin-bottom: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# = Tooltip-enhanced imperative data =
imperative_data = {
    "Present": {
        "Act. 2nd": '<span title="Present Active Imperative, 2nd Person">λύε</span>',
        "Act. 3rd": '<span title="Present Active Imperative, 3rd Person">λυέτω</span>',
        "Mid./Pass. 2nd": '<span title="Present Middle/Passive Imperative, 2nd Person">λύου</span>',
        "Mid./Pass. 3rd": '<span title="Present Middle/Passive Imperative, 3rd Person">λυέσθω</span>'
    },
    "Aorist": {
        "Act. 2nd": '<span title="Aorist Active Imperative, 2nd Person">λῦσον</span>',
        "Act. 3rd": '<span title="Aorist Active Imperative, 3rd Person">λυσάτω</span>',
        "Mid. 2nd": '<span title="Aorist Middle Imperative, 2nd Person">λύσαι</span>',
        "Mid. 3rd": '<span title="Aorist Middle Imperative, 3rd Person">λυσάσθω</span>',
        "Pass. 2nd": '<span title="Aorist Passive Imperative, 2nd Person">λύθητι</span>',
        "Pass. 3rd": '<span title="Aorist Passive Imperative, 3rd Person">λυθήτω</span>'
    }
}

# Convert to DataFrame
df = pd.DataFrame(imperative_data)

# Display table with tooltips
st.markdown("### Imperative Forms of λύω (with Tense, Voice & Person Tooltips)")
st.markdown(df.to_html(escape=False), unsafe_allow_html=True)
