import streamlit as st

import os
import requests

st.header("iDirect")
st.write('Upload your audio asking for directions')


#BASE_URL=os.environ.get('FRONTEND_BASE_URL')



# Attach audio file
with st.form("my-form", clear_on_submit=True):
        audio_file = st.file_uploader("Choose an audio file", type=["mp3"])
        button_attribute = st.form_submit_button("Upload :arrow_up:")

if audio_file is not None:
    st.write("Selected Audio File :small_red_triangle_down:") 
    st.audio(audio_file, format='audio/mp3')

else:
    st.warning("Please select Audio file")

# if button_attribute and st.session_state.select:
#     # audio_file = st.session_state['audio_file']
#     # st.session_state['audio_file'] = None
#     print(audio_file.name)
#     if st.session_state.select:
#         # print("goin into loop")
#         url = f'http://{BASE_URL}:8000/gpt/upload-audio'
#         headers = {'accept': 'application/json'}
#         files = {'file': (audio_file.name, audio_file.read(), 'audio/mpeg')}
#         result = requests.post(url, headers= headers, files= files )
        
#         output = result.json()
#         print("-----------------------------")

#         print(result.status_code)
#         print(output)
#         # print(output['success'])
#         if result.status_code == 200 and audio_file is not None:
#             st.success("Audio Uploaded!")
#             st.session_state.select = True
#         elif result.status_code == 400 and audio_file is not None:
#             st.warning(output['message'])

st.write("\n")
st.write("\n")

result_file_list = requests.get(f'http://{BASE_URL}:8000/gpt/processed-audio-files').json()

list_of_dict = result_file_list['files_with_question']
file_names = []
# Loop through the list of dictionaries
for item in list_of_dict:
# Access the value under the key 'file_names'
    file_name = item['file_name']
# Add the file_name to our list
    file_names.append(file_name)

selected_audio_option = st.selectbox('Select the required file for Link',)

st.write('You selected:', selected_audio_option)
st.write("\n")
# st.write("\n")

st.write("Translated text ")
st.write('The translated text for your audio file is here')


