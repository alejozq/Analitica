import streamlit as st 
from PIL import Image
from streamlit_option_menu import option_menu

st.title("Credit Risk Score \n :red[By Analizadores de Realidades]")

st.markdown("""
            <style>
            .e1nzilvr1 {
                text-align: center;
            }
            
            .e1nzilvr5 p {
                text-align:center;
                font:bold;
                font-size:20px;
            }
            
            </style>
            """, unsafe_allow_html= True
    
)

with st.sidebar:
    selected = option_menu("BIENVENIDOS", ["Video Tutorial", 'Ingresa tus datos'], 
        icons=['film projector', 'clipboard'], menu_icon="house", default_index=1)
    selected

if selected=="Video Tutorial":
    st.video("https://www.youtube.com/watch?v=wohwc9MQt6A&pp=ygUNZXNjbGF2YSByZW1peA%3D%3D")

elif selected=="Ingresa tus datos" :
    edad=st.number_input("Ingresa tu edad",key=int,min_value=0)
    if edad==0:
        st.write(" ")
    elif edad<20:
        st.error('Todavía no te podemos prestar', icon="🚫")
    elif 20<=edad<=25:
        edad="20-25"
    elif 26<=edad<=35 :
        edad="26-35"
    elif 36<=edad<=45 :
        edad="36-45"
        
    elif 46<=edad<=55:
        edad="46-55"
    elif 56<=edad<=65:
        edad="56-65"
    ingreso_anual=st.number_input("¿Cuánto ganas al año?",min_value=0)
    if 0<ingreso_anual<25000:
        ingreso_anual="Bajo"
    elif 25000<=ingreso_anual<50000:
        ingreso_anual="Medio-Bajo"
    elif 50000<=ingreso_anual<75000:
        ingreso_anual="Medio-Alto"
    elif ingreso_anual>=75000:
        ingreso_anual="Alto"
    monto_credito=st.number_input("Ingresa el valor del crédito deseado",min_value=0)
    if 0<monto_credito<=5000:
        monto_credito="Pequeño"
    elif 5000<monto_credito<=10000:
        monto_credito="Mediano"
    elif 10000<monto_credito<=15000:
        monto_credito="Grande"
    elif monto_credito>15000:
        monto_credito="Muy Grande"
        
    interes_deseado=st.number_input("¿A qué tasa de interés deseas tomarlo?",key=float,min_value=0.0)
    tipo_vivienda=st.selectbox('¿En qué tipo de vivienda vives?',('Propia', 'Arrendada', 'Hipotecada'),placeholder="Escoge una opción")
    loan_grade=st.selectbox("¿Cuál es tu calificación crediticia?",("A","B","C","D","F"))
    anos_empleo=st.number_input("¿Cuántos años llevas en tu trabajo actual?",min_value=0)
    
    
    if tipo_vivienda=="Propia":
            tipo_vivienda="OWN"
    elif tipo_vivienda=="Arrendada":
            tipo_vivienda="RENT"
    def score(edad, home, income):
            score = 0
            
            if edad < 22:
                score = score + 100
            elif 22 <= edad < 26:
                score = score + 120
            elif 26 <= edad < 29:
                score = score + 185
            elif 29 <= edad < 32:
                score = score + 200
            elif 32 <= edad < 37:
                score = score + 210
            elif 37 <= edad < 42:
                score = score + 225
            else:
                score = score + 250
                
            if home == 'OWN':
                score = score + 225
            elif home == 'RENT':
                score = score + 110
            else:
                score = score + 0
                
            if income < 10000:
                score = score + 120
            elif 10000 <= income < 17000:
                score = score + 140
            elif 17000 <= income < 28000:
                score = score + 180
            elif 28000 <= income < 35000:
                score = score + 200
            elif 35000 <= income < 42000:
                score = score + 225
            elif 42000 <= income < 58000:
                score = score + 230
            else:
                score = score + 260
            
            return score
    score_final=score(edad,tipo_vivienda,ingreso_anual)
    if st.button("Calcular mi Score"):
        st.info(f"Tu Credit Scores es de: {score_final} ")