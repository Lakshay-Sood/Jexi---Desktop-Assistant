# Jexi - Desktop Voice Assistant
A desktop automation project with voice assistant support.

### This application is currently under development.

### Brief Steps involved are:
1. Set energy threshold values to determine when to start/stop recording
2. Record audio from an audio source (usually system's microphone)
3. Send this audio clip to the Google Speech Recognition API which return a text
4. Verify if this text corresponds to any pre-defined executable command
5. If yes, execute the corresponding command. Else, do nothing.
6. Repeat steps 2-6.
