import streamlit as st
import pandas as pd

st.title("Infinitive Mood of λύω")

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

# = Tooltip-enhanced data =
infinitive_data = {
    "Present": {
        "Act.": '<span title="Present Active Infinitive">λύειν</span>',
        "Mid.": '<span title="Present Middle Infinitive">λύεσθαι</span>',
        "Pass.": '<span title="Present Passive Infinitive">λύεσθαι</span>'
    },
    "Aorist": {
        "Act.": '<span title="Aorist Active Infinitive">λῦσαι</span>',
        "Mid.": '<span title="Aorist Middle Infinitive">λύσασθαι</span>',
        "Pass.": '<span title="Aorist Passive Infinitive">λυθῆναι</span>'
    },
    "Perfect": {
        "Act.": '<span title="Perfect Active Infinitive">λελυκέναι</span>',
        "Mid.": '<span title="Perfect Middle Infinitive">λελύσθαι</span>',
        "Pass.": '<span title="Perfect Passive Infinitive">λελύσθαι</span>'
    }
}

# Convert to DataFrame
df = pd.DataFrame(infinitive_data)

# Display table with tooltips
st.markdown("### Infinitive Forms of λύω (with Tense & Voice Tooltips)")
st.markdown(df.to_html(escape=False), unsafe_allow_html=True)
