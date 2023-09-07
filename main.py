import streamlit as st
from transformers import pipeline
from hing_dict.dict import translation_dict

# Initialize the translation pipeline
translator = pipeline('translation', model="Helsinki-NLP/opus-mt-en-hi", tokenizer="Helsinki-NLP/opus-mt-en-hi")

# Function to translate English to Hindi
def englishToHindi(sentence):
    hindi_text = translator(sentence, src_lang="eng_Latn", tgt_lang="hin_Deva")[0]['translation_text']
    return hindi_text.strip()

# Function to translate Hindi to Hinglish
def hindiToHinglish(sentence, translation_dict):
    words = sentence.split(' ')
    eng_words = []

    for word in words:
        if word in translation_dict:
            eng_words.append(translation_dict[word])
        else:
            eng_words.append(word)

    return ' '.join(eng_words)

# Function to translate English to Hinglish
def englishToHinglish(sentence):
    hindi_text = englishToHindi(sentence)
    hinglish_text = hindiToHinglish(hindi_text, translation_dict)
    return hinglish_text

# Streamlit UI
st.title("English To Hinglish Translator")

# Input text field for English text
st.subheader("Enter text in English")
text = st.text_input('Enter text')

# Button to trigger translation
if st.button('Translate'):
    # Translate and display Hindi and Hinglish text
    hindi_text = englishToHindi(text)
    st.subheader("Hindi")
    st.write(hindi_text.strip())

    hinglish_text = englishToHinglish(text)
    st.subheader("Hinglish")
    st.write(hinglish_text)

# Additional Streamlit components
st.sidebar.header("Settings")  
beam_width = st.sidebar.slider("Translation Beam Width", min_value=1, max_value=10, value=4)
