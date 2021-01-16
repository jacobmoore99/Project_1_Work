import lyricsgenius as genius
geniusCreds = "XLFgo7rC1mmbKLLQKVnImOqwp7K0BccjrMtbbSBp1YWVIxELhWgjVBTG22r8VxM2"
artist_name = "Taylor Swift"
api = genius.Genius(geniusCreds)
artist = api.search_artist(artist_name, max_songs=20)

import os
os.getcwd()

artist.save_lyrics()