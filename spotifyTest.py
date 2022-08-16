#!/usr/bin/env python
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID="487176ae060fa8e78a39f41230489782ddeea49a"
CLIENT_ID="ae31cd85f0494ee19274ed1595efedf6"
CLIENT_SECRET="1c527945e4524a7ba030182a2cb07cf4"

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri="http://localhost:8080",
                                                scope="user-read-playback-state,user-modify-playback-state"))


# Transfer playback to the Raspberry Pi if music is playing on a different device
sp.transfer_playback(device_id=DEVICE_ID, force_play=False)

# Play the spotify track at URI with ID 45vW6Apg3QwawKzBi03rgD (you can swap this for a diff song ID below)
sp.start_playback(device_id="", context_uri='spotify:album:3cf4iSSKd8ffTncbtKljXw?si=Z3eeI0TjRgi-p0V00aD9dg')
