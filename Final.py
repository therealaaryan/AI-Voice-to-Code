from tkinter import *
import speech_recognition as sr

root = Tk()
root.geometry("800x500")
root.title("Speech to Text")

def start_listening():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            text = text.lower()
            if "curly bracket" in text:
                text = text.replace("curly bracket","\n{}")
            elif "open circular bracket" in text:
                text = text.replace("open circular bracket","(")
            elif "close the circular bracket" in text:
                text = text.replace("close the circular bracket",")")
            elif "semicolon" in text:
                text = text.replace("semicolon",";")
            elif "colon" in text:
                text = text.replace("colon",":")
            elif "plus" in text:
                text = text.replace("plus", "+")
            elif "minus" in text:
                text = text.replace("minus", "-")
            elif "multiply" in text or "times" in text:
                text = text.replace("multiply", "*").replace("times", "*")
            elif "divide" in text:
                text = text.replace("divide", "/")
            elif "function" in text:
                text = text.replace("function", "def")
            elif "coma" in text:
                text = text.replace("coma", ",")
            elif "equal" in text:
                text = text.replace("equal", "=")
            elif "ad" in text:
                text = text.replace("ad", "add")
            elif "enter" in text:
                text = text.replace("enter", "\n")
            elif 'and' in text:
                fileEdit()

            return text

        except:
            return None


def get_text():
     text = start_listening()

     if text:
         myLabel2.config(text=text, fg="green")
         get_text()
     else:
         myLabel2.config(text="Couldn't recognize your speech!", fg="red")

def fileEdit():
    file = open('finalCode.txt', 'a')
    text = myLabel2['text']
    file.write(text + " ")
    file.close()

myLabel1 = Label(root, text="Press the button to start speaking", font=('Times', 20))
myLabel1.pack(pady=20)

myButton = Button(root, text="Start", command=get_text, font=('Times', 20))
myButton.pack(pady=20)

myLabel2 = Label(root, text="", font=('Times', 20))
myLabel2.pack(pady=20)
myButton2 = Button(root, text="Print", command=fileEdit, font=('Times', 20))
myButton2.pack(pady=20)

root.mainloop()
