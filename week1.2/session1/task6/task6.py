# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
music_database = { 
    "Taylor Swift": [
        "1989",
        "Red",
        "Folklore"
    ],
    "The Beatles": [
        "Abbey Road",
        "Let It Be",
        "Revolver"
    ],
    "Adele": [
        "19",
        "21"
        "30"
    ]
}

pprint(music_database)
artist = "The Beatles"
album_number=0

if artist in music_database and 0 <= album_number < len(music_database[artist]):
    album = music_database[artist][album_number]

    print("\nAlbum details")
    print("Artist:", artist)
    print("Album:", album)
else:
    print("Artist or albumn not found")

# (keys are artist names, values are lists of album names)

# Pretty-print the data structure

# Display details of one album recorded by a specific artist

