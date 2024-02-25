from gtts import gTTS
import os

def text_to_speech(text, lang='en', output_file='output.mp3'):
    tts = gTTS(text=text, lang=lang, slow=True)  # Set slow=True to slow down the speech
    tts.save(output_file)
    os.system("start " + output_file)  # Opens the generated audio file

if __name__ == "__main__":
    input_text = ("bro mi mits collge lo yedho event anta ga yem sangathi ppelli yeppudu bro")
    
    text_to_speech(input_text)
    
