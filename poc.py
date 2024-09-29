import keyboard
from Watcher import *
import winsound
import os
import pyttsx3
#from playsound import playsound
#from pydub import AudioSegment
#from pydub.playback import play

#musa awak grind:
entries = [ 
            {'Path': ".\Ressources\Class\Awak\Musa\EBuff.bmp", 'MustBePresent': False, 'Counter': 0, 'tts': "utilise ton iBuff", 'confidence_percentage': 0.85, 'ReminderFrequency': 2},
            {'Path': ".\Ressources\Common\Rage\Rage100.bmp", 'MustBePresent': False, 'Counter': 0, 'tts': "utilise ta rage", 'confidence_percentage': 0.97, 'ReminderFrequency': 2},
            ]

# {'Path': ".\Ressources\Common\Buff\HarmoKama.bmp", 'MustBePresent': True, 'Counter': 0, 'tts': "Harmony Kama absent", 'confidence_percentage': 0.85, 'ReminderFrequency': 10},

#Lahn succ grind in kama area with agris
entries = [ 
            {'Path': ".\Ressources\Class\Succ\Lahn\EBuff.bmp", 'MustBePresent': False, 'Counter': 0, 'tts': "utilise ton iBuff", 'confidence_percentage': 0.85, 'ReminderFrequency': 2},
            
            {'Path': ".\Ressources\Common\Rage\Rage100.bmp", 'MustBePresent': False, 'Counter': 0, 'tts': "utilise ta rage", 'confidence_percentage': 0.97, 'ReminderFrequency': 2},
            {'Path': ".\Ressources\Common\LootScroll2.bmp", 'MustBePresent': True, 'Counter': 0, 'tts': "Loot Scroll absent", 'confidence_percentage': 0.85, 'ReminderFrequency': 10},
            {'Path': ".\Ressources\Common\Agris.bmp", 'MustBePresent': True, 'Counter': 0, 'tts': "Agris désactivé", 'confidence_percentage': 0.85, 'ReminderFrequency': 10},
            {'Path': ".\Ressources\Common\Buff\PveMeal.bmp", 'MustBePresent': True, 'Counter': 0, 'tts': "PveMeal absent", 'confidence_percentage': 0.85, 'ReminderFrequency': 10},
            {'Path': ".\Ressources\Common\Buff\AttackChurchBuff.bmp", 'MustBePresent': True, 'Counter': 0, 'tts': "Attack Church absent", 'confidence_percentage': 0.85, 'ReminderFrequency': 10},
            {'Path': ".\Ressources\Common\Buff\DefenceChurchBuff.bmp", 'MustBePresent': True, 'Counter': 0, 'tts': "Defence Church absent", 'confidence_percentage': 0.85, 'ReminderFrequency': 10},
            {'Path': ".\Ressources\Common\Buff\VellBuff.bmp", 'MustBePresent': True, 'Counter': 0, 'tts': "Vell absent", 'confidence_percentage': 0.85, 'ReminderFrequency': 10},
            ]



#BDO must run on main screen (0,0) on left top and the resolution must be adapted:
screeny=1080
screenx=1920 #2560
region = (0,0,screenx,screeny)

#for motherboard beep:
alarmFrequency = 2500  # Set Frequency To 2500 Hertz
alarmDuration = 3000  # Set Duration To 1000 ms == 1 second

#for log purpose:
timeformat= "%H:%M:%S.%f: "

#for image recognition
myWatcher = Watcher(0.95)

#for tts:
engine = pyttsx3.init()
voice = engine.getProperty('voices')[0] # the french voice
engine.setProperty('voice', voice.id)

#for notification found
#os.system("ffplay.exe" + " ./notif.wav")
#playsound('./notif.wav')
#song = AudioSegment.from_wav('./notif.wav')
#play(song)

#main loop:
while keyboard.is_pressed('-') == False:
    
    time.sleep(2)
    PeriodicCheck = False
    
    for entry in entries:
        print(entry['Path'])
        #IsLocalized = myWatcher.GetPosItem(entry['Path'], region, True) #
        IsLocalized = myWatcher.GetPosItemWithpercentage(entry['Path'], region, entry['confidence_percentage'])
        print(IsLocalized)
        if entry['MustBePresent']:  
            #print('Mustbe present true')   
            if (IsLocalized == None):
                #print("Localized")
                entry['Counter'] = entry['Counter'] + 1
                if entry['Counter'] >= entry['ReminderFrequency']:
                    engine.say(entry['tts'])
                    engine.runAndWait() 
                    entry['Counter'] = 0
            else:
                entry['Counter'] = 0
        else:
            if (IsLocalized != None):
                entry['Counter'] = entry['Counter'] + 1
                if entry['Counter'] >= entry['ReminderFrequency']:
                    engine.say(entry['tts'])
                    engine.runAndWait()  
                    entry['Counter'] = 0
            else:
                entry['Counter'] = 0
              
              
    
"""   
    EBuffloc = myWatcher.GetPosItem(".\Ressources\Class\Succ\Lahn\EBuff.bmp", region, False) 
    if (EBuffloc != None):
        snow = datetime.now()
        #print(snow.strftime(timeformat) , "EBuff found!")
        #winsound.Beep(alarmFrequency, alarmDuration)
        engine.say("test")
        engine.runAndWait()
    
    
    EBuffloc = myWatcher.GetPosItem(".\Ressources\Common\Buff\HarmoKama.bmp", region, True) 
    if (EBuffloc == None):
        snow = datetime.now()
        #print(snow.strftime(timeformat) , "Harmony Kama absent")
        PeriodicCheck = True
        #winsound.Beep(alarmFrequency, alarmDuration)
        engine.say("Harmony Kama absent")
        engine.runAndWait()
        
    EBuffloc = myWatcher.GetPosItem(".\Ressources\Common\Buff\PveMeal.bmp", region, True) 
    if (EBuffloc == None):
        snow = datetime.now()
        #print(snow.strftime(timeformat) , "Harmony Kama absent")
        PeriodicCheck = True
        #winsound.Beep(alarmFrequency, alarmDuration)
        engine.say("Bouffe Pve absente!")
        engine.runAndWait()
        
        
    EBuffloc = myWatcher.GetPosItem(".\Ressources\Common\Rage\Rage100.bmp", region, True) 
    if (EBuffloc != None):
        snow = datetime.now()
        #print(snow.strftime(timeformat) , "Harmony Kama absent")
        PeriodicCheck = True
        #winsound.Beep(alarmFrequency, alarmDuration)
        engine.say("Utilise ton 100%")
        engine.runAndWait()
"""