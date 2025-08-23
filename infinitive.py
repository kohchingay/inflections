import streamlit as st

st.title("Infinitive Mood of λύω")

# st.markdown("<h1 style='color:#1f77b4;'>Infinitive Mood of λύω</h1>", unsafe_allow_html=True)

# = CSS styling with custom tooltip =
st.markdown("""
    <style>
        .note-blue {
            color: #66ccff;  /* Or any color you prefer */
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .block-container {
            max-width: unset;
            padding-left: 4rem;
            padding-right: 4rem;
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
            bottom: 200%; /* Position above */
            left: 50%;
            transform: translateX(-50%);
            opacity: 0;
            transition: opacity 0.3s;
            font-size: 0.8rem;
        }

        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        .note-gold { color: #ffcc00; font-weight: bold; }
        .note-blue { color: #66ccff; font-weight: bold; } 
        }
    </style>
""", unsafe_allow_html=True)

# = HTML table with CSS tooltips =
table_html = """
<table>
    <tr>
        <th></th>
        <th><span class='note-blue'>Active</span></th>
        <th><span class='note-blue'>Middle</span></th>
        <th><span class='note-blue'>Passive</span></th>
    </tr>
    <tr>
        <td><span class='note-blue'>Present</span></td>
        <td><span class="tooltip">λύειν<span class="tooltiptext">Present Active Infinitive</span></span></td>
        <td colspan="2"><span class="tooltip">λύεσθαι<span class="tooltiptext">Present Middle & Passive Infinitive</span></span></td>
    </tr>
    <tr>
        <td><span class='note-blue'>Aorist</span></td>
        <td><span class="tooltip">λῦσαι<span class="tooltiptext">Aorist Active Infinitive<br><span class='note-gold'>Also Aor.Mid.Imp. 2nd sing.</span></span></span></td>
        <td><span class="tooltip">λύσασθαι<span class="tooltiptext">Aorist Middle Infinitive</span></span></td>
        <td><span class="tooltip">λυθῆναι<span class="tooltiptext">Aorist Passive Infinitive</span></span></td>
    </tr>
    <tr>
        <td><span class='note-blue'>Perfect</span></td>
        <td><span class="tooltip">λελυκέναι<span class="tooltiptext">Perfect Active Infinitive</span></span></td>
        <td colspan="2"><span class="tooltip">λελύσθαι<span class="tooltiptext">Perfect Middle & Passive Infinitive</span></span></td>
    </tr>
</table>
"""

# Display table
# st.markdown('<div style="text-align: center;"><h3>Infinitive Forms of λύω</h3></div>', unsafe_allow_html=True)
st.markdown(table_html, unsafe_allow_html=True)
