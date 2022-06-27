class Spotify:
    def __init__(self, song_list):
        self.song_list = song_list
        print("Welcome to Spotify!")

    def playing_number(self, index):
        self.index = index
        if index <= len(self.song_list):

            result = f"Playing {self.index} number song for you\nSong name: {self.song_list[index - 1]}"


        else:
            result = f"{self.index} number song not found. Your playlist has {len(self.song_list)} songs only."

        return result

    def add_to_playlist(self, song):
        self.song_list.append(song)


user1 = Spotify(["See You Again", "Uptown Funk", "Hello"])
print("=========================")
print(user1.playing_number(4))
user1.add_to_playlist("Dusk Till Dawn")
print(user1.playing_number(3))
print(user1.playing_number(4))
