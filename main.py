import speech_recognition as sr
import os
from os import path
import winsound


if __name__ == '__main__':
    # Read the folder name
    with os.scandir('Input/') as entries:
        for entry in entries:
            print(entry.name)
            # see if transcripts_of_"foldername".txt exists, if so return.
            # create a transcripts_of_"foldername".txt
            f = open(("Input/transcripts_of_" + entry.name + ".txt"), "a")
            # Loop through writing /"foldername"/"filename".wav|"transcription" to transcripts_of_"foldername".txt
            basepath = 'Input/' + entry.name
            for entry2 in os.listdir(basepath):
                if os.path.isfile(os.path.join(basepath, entry2)):
                    # print(entry2)
                    AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), basepath + "/" + entry2)

                    # use the audio file as the audio source
                    r = sr.Recognizer()
                    try:
                        with sr.AudioFile(AUDIO_FILE) as source:
                            audio = r.record(source)  # read the entire audio file

                        # recognize speech using Google Speech Recognition
                        try:
                            # for testing purposes, we're just using the default API key
                            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                            # instead of `r.recognize_google(audio)`
                            transcription = "/" + entry.name + "/" + entry2 + "|" + r.recognize_google(audio)
                            print(transcription)
                            f = open(("Input/transcripts_of_" + entry.name + ".txt"), "a")
                            f.write(transcription)
                            f.write("\n")
                            f.close()
                        except sr.UnknownValueError:
                            print("Google Speech Recognition could not understand audio")
                            f = open(("Input/transcripts_of_" + entry.name + ".txt"), "a")
                            f.write("\n")
                            f.close()
                        except sr.RequestError as e:
                            print("Could not request results from Google Speech Recognition service; {0}".format(e))
                    except Exception as e:
                        print("Audio Format Error")
                        f = open(("Input/transcripts_of_" + entry.name + ".txt"), "a")
                        f.write("\n")
                        f.close()
    print('\a')
    winsound.Beep(1000, 200)
    winsound.Beep(1500, 200)
    winsound.Beep(2000, 200)


