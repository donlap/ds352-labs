import joblib
import pandas as pd
import streamlit as st 

EDU_DICT = {'Preschool': 1,
            '1st-4th': 2,
            '5th-6th': 3,
            '7th-8th': 4,
            '9th': 5,
            '10th': 6,
            '11th': 7,
            '12th': 8,
            'HS-grad': 9, 
            'Some-college': 10,
            'Assoc-voc': 11,
            'Assoc-acdm': 12,
            'Bachelors': 13,
            'Masters': 14,
            'Prof-school': 15,
            'Doctorate': 16
            }

model = joblib.load('model.joblib')
unique_values = joblib.load('unique_values.joblib')
    
unique_class =  unique_values["workclass"]
unique_education =  unique_values["education"]
unique_marital_status =  unique_values["marital.status"]
unique_relationship =  unique_values["relationship"]
unique_occupation =  unique_values["occupation"]
unique_sex =  unique_values["sex"]
unique_race = unique_values["race"]
unique_country =  unique_values["native.country"]

def main():
    st.title("Adult Income Analysis")

    with st.form("questionaire"):
        age = st.slider("Age", min_value=10, max_value=100)
        workclass = st.selectbox("Workclass", unique_class)
        education = st.selectbox("Education", unique_education)
        Marital_Status = st.selectbox("Marital Status", unique_marital_status)
        occupation = st.selectbox("Occupation", unique_occupation)
        relationship = st.selectbox("Relationship", unique_relationship)
        race = st.selectbox("Race", unique_race)
        sex = st.selectbox("Sex", unique_sex)
        hours_per_week = st.slider("Hours per week", min_value=1, max_value=100)
        native_country = st.selectbox("Country", unique_country)

        clicked = st.form_submit_button("Predict income")
        if clicked:
            result=model.predict(pd.DataFrame({"age": [age],
                                               "workclass": [workclass],
                                               "education": [EDU_DICT[education]],
                                               "marital.status": [Marital_Status],
                                               "occupation": [occupation],
                                               "relationship": [relationship],
                                               "race": [race],
                                               "sex": [sex],
                                               "hours.per.week": [hours_per_week],
                                               "native.country": [native_country]}))
            result = '>50K' if result[0] == 1 else '<=50K'
            st.success('The predicted income is {}'.format(result))

if __name__=='__main__':
    main()
