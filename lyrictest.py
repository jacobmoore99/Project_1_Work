import lyricsgenius
genius = lyricsgenius.Genius("XLFgo7rC1mmbKLLQKVnImOqwp7K0BccjrMtbbSBp1YWVIxELhWgjVBTG22r8VxM2")
artist = genius.search_artist("Lin-Manuel Miranda", max_songs=3, sort="title")
song = genius.search_song("Alexander Hamilton", artist.name)
print(song.lyrics)