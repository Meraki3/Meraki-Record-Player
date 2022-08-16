#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID="487176ae060fa8e78a39f41230489782ddeea49a"
CLIENT_ID="ae31cd85f0494ee19274ed1595efedf6"
CLIENT_SECRET="1c527945e4524a7ba030182a2cb07cf4"

while True:
    try:
        reader=SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))
        
        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("Waiting for record scan...")
            id= reader.read()[0]
            print("Card Value is:",id)
            sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
            
            # DONT include the quotation marks around the card's ID value, just paste the number
            if (id==417539860128):
                #playing bad bunny
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:3RQQmkQEvNCY4prGKE6oc5')
                sleep(2)
            
            elif (id==350532052540):
                
                # playing Burna Boy
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6kgDkAupBVRSqbJPUaTJwQ')
                sleep(2)
                         
            elif (id==1036787164774):
                
                # playing Sam Smith
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:3XftSbguntyRTBQaGItmfK')
                sleep(2)
                
            elif (id==555733984784):
                
                # playing Kungs
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:66KCBRiOFSs9bki2A15WlB')
                sleep(2)
                
            elif (id==763771791003):
                
                # playing Charles Aznavour
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:3Nq8RecQlxWA7TVPjZsGuv')
                sleep(2)
                
            elif (id==967681615448):
                
                # playing Fairouz
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:7MrdWIvdobTf6MqVD3yILM')
                sleep(2)
            # continue adding as many "elifs" for songs/albums that you want to play

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()
