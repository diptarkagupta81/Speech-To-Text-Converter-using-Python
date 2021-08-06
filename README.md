# Speech-To-Text-Converter-using-Python
Using the Speech Recognition library available in Python, we take the input speech via mic and then convert it to the text file
To list out the mic available use:
sr.Microphone.list_microphone_names()

and then decide which mic you want to use and select it by providing the index value
eg: mic=sr.Microphone(device_index=1)
