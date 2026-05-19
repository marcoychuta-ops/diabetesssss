import streamlit as st
import pandas as pd
import pickle

# Cargar modelo
modelo = pickle.load(open('modelos/modelo.pkl', 'rb'))

st.title("Predicción de Diabetes")

st.write("Ingrese los datos del paciente")

glucose = st.number_input("Glucose")
bloodpressure = st.number_input("Blood Pressure")
skinthickness = st.number_input("Skin Thickness")
insulin = st.number_input("Insulin")
bmi = st.number_input("BMI")
age = st.number_input("Age")

# Crear dataframe
datos = pd.DataFrame({
    'Glucose': [glucose],
    'BloodPressure': [bloodpressure],
    'SkinThickness': [skinthickness],
    'Insulin': [insulin],
    'BMI': [bmi],
    'Age': [age]
})

# Botón
if st.button("Predecir"):

    prediccion = modelo.predict(datos)

    if prediccion[0] == 1:
        st.error("El paciente tiene riesgo de diabetes")
    else:
        st.success("El paciente NO tiene riesgo de diabetes")

st.write("---")
st.write("Nombre: TU NOMBRE")
st.write("Código ISIL: TU CÓDIGO")

st.markdown("[Ver Colab](PEGAR_AQUI_LINK_COLAB)")
