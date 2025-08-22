import streamlit as st

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
        td:first-child {
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# = Tooltip-enhanced HTML table =
table_html = """
<table>
    <tr>
        <th></th>
        <th>Present</th>
        <th>Aorist</th>
        <th>Perfect</th>
    </tr>
    <tr>
        <td>Act.</td>
        <td><span title="Present Active Infinitive">λύειν</span></td>
        <td><span title="Aorist Active Infinitive">λῦσαι</span></td>
        <td><span title="Perfect Active Infinitive">λελυκέναι</span></td>
    </tr>
    <tr>
        <td>Mid.</td>
        <td><span title="Present Middle Infinitive">λύεσθαι</span></td>
        <td><span title="Aorist Middle Infinitive">λύσασθαι</span></td>
        <td><span title="Perfect Middle Infinitive">λελύσθαι</span></td>
    </tr>
    <tr>
        <td>Pass.</td>
        <td><span title="Present Passive Infinitive">λύεσθαι</span></td>
        <td><span title="Aorist Passive Infinitive">λυθῆναι</span></td>
        <td><span title="Perfect Passive Infinitive">λελύσθαι</span></td>
    </tr>
</table>
"""

# Display table
st.markdown("### Infinitive Forms of λύω (with Hover Tooltips)")
st.markdown(table_html, unsafe_allow_html=True)
