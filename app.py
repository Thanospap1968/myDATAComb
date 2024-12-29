import streamlit as st
import main


    
df = main.read_map("map.xlsx")
typoi = df["ΤΥΠΟΣ"].sort_values().unique()

st.title("myDATA Συνδυασμοί Παραστατικών")
st.write("Prolink Data ΕΠΕ")

st.selectbox(
    "Επιλογή τύπου Ε3",
    typoi,
    index=None,
    placeholder="Επιλέξτε τύπο Ε3",
    key="typoi_box"

)

if st.session_state.typoi_box != None:
    st.dataframe(
        data=df[df['ΤΥΠΟΣ'] == st.session_state.typoi_box],
        hide_index=True,
        column_order=("ΠΑΡΑΣΤΑΤΙΚΟ", "ΚΑΤΗΓΟΡΙΑ"),
        column_config={
            "ΠΑΡΑΣΤΑΤΙΚΟ": st.column_config.Column(
                width="large"
            ),
            "ΚΑΤΗΓΟΡΙΑ": st.column_config.Column(
                width="large"
            ),
        }
    )



