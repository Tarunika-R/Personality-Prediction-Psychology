import streamlit as st
import time
import numpy as np
import pandas as pd
import joblib

model = joblib.load('model')

st.set_page_config(page_title = 'Predict Your Personality' , 
                   page_icon = ':eye:', 
                   layout = "centered", 
                   initial_sidebar_state = "auto")

st.title('Personality Prediction - Psychology')
st.header('Predict your personality on answering the following questions')
st.subheader('1 - Strongly Disagree')
st.subheader('2 - Disagree')
st.subheader('3 - Neutral')
st.subheader('4 - Agree')
st.subheader('5 - Strongly Agree')
st.session_state.horizontal = True
st.divider()

EXT2 = st.radio("I don't talk a lot", ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
EXT3 = st.radio('I feel comfortable around people', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
EXT5 = st.radio('I start conversations', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal) 
st.divider()
EXT6 = st.radio('I have little to say', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
EXT8 = st.radio("I don't like to draw attention to myself", ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
EXT9 = st.radio("I don't mind being the center of attention", ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()

EST1 = st.radio('I get stressed out easily', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
EST2 = st.radio('I am relaxed most of the time', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
EST4 = st.radio('I seldom feel blue', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
EST6 = st.radio('I get upset easily', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
EST7 = st.radio('I change my mood a lot', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
EST8 = st.radio('I have frequent mood swings', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()

AGR3 = st.radio('I insult people', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
AGR4 = st.radio('I sympathize with others feelings', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
AGR5 = st.radio('I am not interested in other peoples problems', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
AGR7 = st.radio('I am not really interested in others', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
AGR9 = st.radio('I feel others emotions', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
AGR10 = st.radio('I make people feel at ease', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()

CSN1 = st.radio('I am always prepared', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
CSN2 = st.radio('I leave my belongings around', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
CSN4 = st.radio('I make a mess of things', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
CSN5 = st.radio('I get chores done right away', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
CSN6 = st.radio('I often forget to put things back in their proper place', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
CSN9 = st.radio('I follow a schedule', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
            
OPN2 = st.radio('I have difficulty understanding abstract ideas', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
OPN3 = st.radio('I have a vivid imagination', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
OPN4 = st.radio('I am not interested in abstract ideas', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
OPN5 = st.radio('I have excellent ideas', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
OPN6 = st.radio('I do not have a good imagination', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)
st.divider()
OPN7 = st.radio('I am quick to understand things', ('1', '2', '3', '4', '5'), horizontal=st.session_state.horizontal)



def analyse ():
    row = np.array([EXT2, EXT3, EXT5, EXT6, EXT8, EXT9, EST1, EST2, EST4, EST6, EST7, EST8, AGR3, AGR4, AGR5, AGR7, AGR9, AGR10, CSN1, CSN2, CSN4, CSN5, CSN6, CSN9, OPN2, OPN3, OPN4, OPN5, OPN6, OPN7])
    x = pd.DataFrame([row])
    prediction = model.predict(x)[0]

    with st.spinner('Wait for it...'):
        time.sleep(5)
        
    if prediction == 0:
        st.success("Introverted and Reserved")
        st.caption('You are quiet')
        st.caption('You tend to be introspective') 
        st.caption('You enjoy spending time alone')
        st.caption('You gain eneragy through solitude and quiet')

    elif prediction == 1:
        st.success("Friendly and Outgoing")
        st.caption('You are extroverted')
        st.caption('You enjoy being around people') 
        st.caption('You are often talkative')
        st.caption('You are sociable')

    elif prediction == 2:
        st.success("Emotionally Stable")
        st.caption('You are calm, composed and stress-resistant')
        st.caption('You are a confident person') 
        st.caption('You cannot be easily provoked or disheartened by setbacks')
        st.caption('You withstand the whirlwind that life throws your way and still be productive and capable through it')

    elif prediction == 3:
        st.success("Sympathetic and Caring")
        st.caption('You show concern for others by understanding their situation')
        
    elif prediction == 4:
        st.success("Organized and Disciplined")
        st.caption('You have the baility to control yourself to make yourself thrive through things')
        st.caption('You are not dependent on anyone') 
        
st.divider()
st.button('Submit', on_click = analyse)

