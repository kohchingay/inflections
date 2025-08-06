import streamlit as st
import pandas as pd

# Inject custom CSS for wider columns and smaller headings
st.markdown("""
    <style>
        .block-container {
            padding-left: 10rem;
            padding-right: 10rem;
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        table {
            width: 100%;
        }
        th, td {
            padding: 0.5rem 1rem;
            text-align: center;
            white-space: nowrap;
        }
        h1, h2, h3, h4 {
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Conjugation of λύω")
st.write("Full indicative inflections of λύω organized by tense and voice.")

# Helper functions
def show_two(title1, data1, title2, data2):
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(f"### {title1}")
        st.table(pd.DataFrame(data1, columns=["Person", "Singular", "Plural"]))
    with col2:
        st.markdown(f"### {title2}")
        st.table(pd.DataFrame(data2, columns=["Person", "Singular", "Plural"]))

def show_three(title1, data1, title2, data2, title3, data3):
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.markdown(f"### {title1}")
        st.table(pd.DataFrame(data1, columns=["Person", "Singular", "Plural"]))
    with col2:
        st.markdown(f"### {title2}")
        st.table(pd.DataFrame(data2, columns=["Person", "Singular", "Plural"]))
    with col3:
        st.markdown(f"### {title3}")
        st.table(pd.DataFrame(data3, columns=["Person", "Singular", "Plural"]))

# Present Indicative
present_active = [["1st", "λύω", "λύομεν"], ["2nd", "λύεις", "λύετε"], ["3rd", "λύει", "λύουσι(ν)"]]
present_mp = [["1st", "λύομαι", "λυόμεθα"], ["2nd", "λύῃ", "λύεσθε"], ["3rd", "λύεται", "λύονται"]]
show_two("Pres. Act. Ind.", present_active, "Pres. Mid./Pass. Ind.", present_mp)

# Imperfect Indicative
imperfect_active = [["1st", "ἔλυον", "ἐλύομεν"], ["2nd", "ἔλυες", "ἐλύετε"], ["3rd", "ἔλυε(ν)", "ἔλυον"]]
imperfect_mp = [["1st", "ἐλυόμην", "ἐλυόμεθα"], ["2nd", "ἐλύου", "ἐλύεσθε"], ["3rd", "ἐλύετο", "ἐλύοντο"]]
show_two("Imp. Act. Ind.", imperfect_active, "Imp. Mid./Pass. Ind.", imperfect_mp)

# Future Indicative
future_active = [["1st", "λύσω", "λύσομεν"], ["2nd", "λύσεις", "λύσετε"], ["3rd", "λύσει", "λύσουσι(ν)"]]
future_middle = [["1st", "λύσομαι", "λυσόμεθα"], ["2nd", "λύσῃ", "λύσεσθε"], ["3rd", "λύσεται", "λύσονται"]]
future_passive = [["1st", "λυθήσομαι", "λυθησόμεθα"], ["2nd", "λυθήσῃ", "λυθήσεσθε"], ["3rd", "λυθήσεται", "λυθήσονται"]]
show_three("Fut. Act. Ind.", future_active, "Fut. Mid. Ind.", future_middle, "Fut. Pass. Ind.", future_passive)

# 1st Aorist Indicative
aorist1_active = [["1st", "ἔλυσα", "ἐλύσαμεν"], ["2nd", "ἔλυσας", "ἐλύσατε"], ["3rd", "ἔλυσε(ν)", "ἔλυσαν"]]
aorist1_middle = [["1st", "ἐλυσάμην", "ἐλυσάμεθα"], ["2nd", "ἐλύσω", "ἐλύσασθε"], ["3rd", "ἐλύσατο", "ἐλύσαντο"]]
aorist1_passive = [["1st", "ἐλύθην", "ἐλύθημεν"], ["2nd", "ἐλύθης", "ἐλύθητε"], ["3rd", "ἐλύθη", "ἐλύθησαν"]]
show_three("1Aor. Act. Ind.", aorist1_active, "1Aor. Mid. Ind.", aorist1_middle, "1Aor. Pass. Ind.", aorist1_passive)

# 2nd Aorist Indicative
aorist2_active = [["1st", "ἔλαβον", "ἐλάβομεν"], ["2nd", "ἔλαβες", "ἐλάβετε"], ["3rd", "ἔλαβε(ν)", "ἔλαβον"]]
aorist2_middle = [["1st", "ἐλαβόμην", "ἐλαβόμεθα"], ["2nd", "ἐλάβου", "ἐλάβεσθε"], ["3rd", "ἐλάβετο", "ἐλάβοντο"]]
aorist2_passive = [["1st", "ἐλήμφθην", "ἐλήμφθημεν"], ["2nd", "ἐλήμφθης", "ἐλήμφθητε"], ["3rd", "ἐλήμφθη", "ἐλήμφθησαν"]]
show_three("2Aor. Act. Ind.", aorist2_active, "2Aor. Mid. Ind.", aorist2_middle, "2Aor. Pass. Ind.", aorist2_passive)

# Perfect Indicative
perfect_active = [["1st", "λέλυκα", "λελύκαμεν"], ["2nd", "λέλυκας", "λελύκατε"], ["3rd", "λέλυκε(ν)", "λελύκασι(ν)"]]
perfect_middle = [["1st", "λέλυμαι", "λελύμεθα"], ["2nd", "λέλυσαι", "λέλυσθε"], ["3rd", "λέλυται", "λέλυνται"]]
perfect_passive = perfect_middle
show_three("Perf. Act. Ind.", perfect_active, "Perf. Mid. Ind.", perfect_middle, "Perf. Pass. Ind.", perfect_passive)

# Pluperfect Indicative
pluperfect_active = [["1st", "ἐλελύκη", "ἐλελύκεμεν"], ["2nd", "ἐλελύκης", "ἐλελύκετε"], ["3rd", "ἐλελύκει", "ἐλελύκεσαν"]]
pluperfect_middle = [["1st", "ἐλελύμην", "ἐλελύμεθα"], ["2nd", "ἐλέλυσο", "ἐλέλυσθε"], ["3rd", "ἐλέλυτο", "ἐλέλυντο"]]
pluperfect_passive = pluperfect_middle
show_three("Plupf. Act. Ind.", pluperfect_active, "Plupf. Mid. Ind.", pluperfect_middle, "Plupf. Pass. Ind.", pluperfect_passive)
