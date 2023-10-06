# Subsystem 1: Amplifier
class Amplifier:
    def on(self):
        print("Amplifier is on")

    def off(self):
        print("Amplifier is off")

# Subsystem 2: DVD Player


class DVDPlayer:
    def on(self):
        print("DVD Player is on")

    def off(self):
        print("DVD Player is off")

    def play(self):
        print("DVD Player is playing")

# Subsystem 3: Screen


class Screen:
    def up(self):
        print("Screen is up")

    def down(self):
        print("Screen is down")

# Subsystem 4: Home Theater Facade


class HomeTheaterFacade:
    def __init__(self, amplifier, dvd_player, screen):
        self.amplifier = amplifier
        self.dvd_player = dvd_player
        self.screen = screen

    def watch_movie(self):
        self.amplifier.on()
        self.dvd_player.on()
        self.screen.down()
        self.dvd_player.play()

    def end_movie(self):
        self.amplifier.off()
        self.dvd_player.off()
        self.screen.up()


# Client code
if __name__ == "__main__":
    amplifier = Amplifier()
    dvd_player = DVDPlayer()
    screen = Screen()

    theater_facade = HomeTheaterFacade(amplifier, dvd_player, screen)

    print("=== Watching a movie ===")
    theater_facade.watch_movie()

    print("\n=== Ending the movie ===")
    theater_facade.end_movie()
