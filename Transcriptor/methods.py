import os
import torch
import whisper
import subprocess


def has_audio(path) :                # function to check whether the file contains an audio...
    try:
        result = subprocess.run(
            ["ffprobe", "-i", path, "-show_streams", "-select_streams", "a", "-loglevel", "error"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )                  #to fetch the details of the file...
        return bool(result.stdout)
    except Exception:        #to catch exception if its not a media file...
        return False


def av_filter(files, path) :                 #to filter out audio video files only from others...
    av = []
    for file in files :
        file = path + ("\\" if os.name == "nt" else "/") + file
        print(file)
        if has_audio(file) :
            av.append(file)
    return av                       #return audio video files only...


def transcribe(path) :                  # function to search for the file and transcribe it...
    print("Loading Model...")
    device = "cuda" if torch.cuda.is_available() else "cpu"    #search for an nvidia GPU...
    model = whisper.load_model("base").to(device)        # loading a whisper model...
    os.system("cls" if os.name == "nt" else "clear")
    
    for subdir, dirs, files in os.walk(path) :          #iterating through the directory and sub directories...
        print(f"\n\nProcessing Directory: {subdir}")
        files = av_filter(files, subdir)
    
        if files != [] :            #check if audio video files exists...
            for file in files :           #iterating through audio video files...
                print(f"Transcribing {file}\n")
                result = model.transcribe(file)           #transcribing the audio with whisper package...
                fname = os.path.splitext(file)[0]         #getting the file name of the audio or video...
                with open(f"{fname}.txt", 'w') as f:
                    f.write(result["text"])               #writing transcription to the .txt file...
                print(f"Transcribed and written to {fname}.txt\n")
        else :
            print("No Audio or Video files to process!!!")
        