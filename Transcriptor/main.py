import methods
import os

if __name__ == "__main__" :
    
    while True :
        path = input("Enter Absolute Path: ")
        if path.lower() == "exit" :           #block to exit for the user...
            print("Exiting...")
            exit()
        if os.path.exists(path) :         #check if the given path exists...
            break
        print("Enter a valid path!!!")

    methods.transcribe(path)