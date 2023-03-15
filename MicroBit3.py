from microbit import *
import log


while True:
    temp=temperature()
    sound=microphone.sound_level()
    light=display.read_light_level()
    if pin_logo.is_touched():    
        log.add({
          'Temperature': temperature(),
          'Sound': microphone.sound_level(),
          'Light': display.read_light_level()
        })

        display.scroll("Data logged!")
        display.show(Image('00000:''09090:''00000:''90009:''09990'))

     
