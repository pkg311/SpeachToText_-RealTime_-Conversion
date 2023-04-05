import speech_recognition as sr

# Create a recognizer object and adjust the energy threshold to reduce noise
r = sr.Recognizer()
r.energy_threshold = 4000

# Start listening for audio input from the microphone in real-time
with sr.Microphone() as source:
    print("Listening...")
    a=1
    # Continuously listen for audio input and convert it to text
    while a==1:
        try:
            audio = r.listen(source, phrase_time_limit=5) # Increase or decrease phrase time limit based on the length of audio you want to recognize
            text = r.recognize_google(audio)
            print("You said:", text)
            if 'bye Jarvis' in text:
                a=0
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        if a==0:
            break
