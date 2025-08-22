import streamlit as st

st.title("Infinitive Mood of λύω")

# = CSS styling with custom tooltip =
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

        /* Tooltip styling */
        .tooltip {
            position: relative;
            display: inline-block;
            cursor: help;
        }

        .tooltip .tooltiptext {
            visibility: hidden;
            width: max-content;
            background-color: #333;
            color: #fff;
            text-align: center;
            border-radius: 4px;
            padding: 4px 8px;
            position: absolute;
            z-index: 1;
            bottom: 125%; /* Position above */
            left: 50%;
            transform: translateX(-50%);
            opacity: 0;
            transition: opacity 0.3s;
            font-size: 0.8rem;
        }

        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
    </style>
""", unsafe_allow_html=True)

# = HTML table with CSS tooltips =
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
        <td><span class="tooltip">λύειν<span class="tooltiptext">Present Active Infinitive</span></span></td>
        <td><span class="tooltip">λῦσαι<span class="tooltiptext">Aorist Active Infinitive</span></span></td>
        <td><span class="tooltip">λελυκέναι<span class="tooltiptext">Perfect Active Infinitive</span></span></td>
    </tr>
    <tr>
        <td>Mid.</td>
        <td><span class="tooltip">λύεσθαι<span class="tooltiptext">Present Middle Infinitive</span></span></td>
        <td><span class="tooltip">λύσασθαι<span class="tooltiptext">Aorist Middle Infinitive</span></span></td>
        <td><span class="tooltip">λελύσθαι<span class="tooltiptext">Perfect Middle Infinitive</span></span></td>
    </tr>
    <tr>
        <td>Pass.</td>
        <td><span class="tooltip">λύεσθαι<span class="tooltiptext">Present Passive Infinitive</span></span></td>
        <td><span class="tooltip">λυθῆναι<span class="tooltiptext">Aorist Passive Infinitive</span></span></td>
        <td><span class="tooltip">λελύσθαι<span class="tooltiptext">Perfect Passive Infinitive</span></span></td>
    </tr>
</table>
"""

# Display table
st.markdown("### Infinitive Forms of λύω (with Reliable Tooltips)")
st.markdown(table_html, unsafe_allow_html=True)
