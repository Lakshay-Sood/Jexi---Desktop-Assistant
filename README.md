# Jexi - Desktop Voice Assistant
A desktop automation project with voice assistant support.

For a complete report on Jexi, follow this document: https://docs.google.com/document/d/16mDcuC6_itjg1_lE3AypzI8F12A_Ymi717PFZwu2nKU/edit?usp=sharing

### Brief Steps involved in the working of Jexi are:
1. Set energy threshold values to determine when to start/stop recording
2. Record audio from an audio source (usually system's microphone)
3. Send this audio clip to the Google Speech Recognition API which return a text
4. Verify if this text corresponds to any pre-defined executable command
5. If yes, execute the corresponding command. Else, do nothing.
6. Repeat steps 2-6.

### Requirements & Setup
1) You need to have python 3 installed on your system.
2) Clone/Download this repository to your local machine.
3) Download the required packages by running the "  pip install -r requirements.txt  " command in the terminal at the location where you clone/download this repository.
4) Voila! You are done.

### Bringing Jexi to life
1) Simply run the python script "main.py" in the terminal.
2) You are ready to use it now!
3) Optional: Check the dictionary (hashmap) at the beginning of the file to get to know the commands that Jexi currently supports.
4) Optional: For Video demo, check out this drive folder: https://drive.google.com/drive/folders/1ZT2Sg4BZ8A212ORlAgedqnDRmzWH8npd?usp=sharing
