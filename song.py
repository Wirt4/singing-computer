
import subprocess
def speak(word):
    print(word)
    word = '"'+word+'"'
    command = 'say '+word
    subprocess.call(command, shell=True)
def main():
    speak("If you're out on the road")
    speak("Feeling lonely, and so cold")
    speak("All you have to do is call my name")
    speak("And I'll be there on the next train")
    speak("Where you lead, I will follow")
    speak("Anywhere that you lead me to")
    speak("If you need, you need me to be with you")
    speak("I will follow where you lead")
main()
