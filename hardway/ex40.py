class Song(object):
    def __init__(self, lyrics: list):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                   "I do not want to get sued"])

happy_bday.sing_me_a_song()