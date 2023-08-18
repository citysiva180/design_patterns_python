# Target interface
class MediaPlayer:
    def play(self, audio_type, file_name):
        pass

# Adaptee
class AdvancedMediaPlayer:
    def play_vlc(self, file_name):
        pass
    
    def play_mp4(self, file_name):
        pass

# Adapter
class MediaAdapter(MediaPlayer):
    
    def __init__(self, audio_type):
    
        if audio_type == "vlc":
            self.advanced_player = AdvancedMediaPlayerVlc()
        elif audio_type == "mp4":
            self.advanced_player = AdvancedMediaPlayerMp4()
    
    def play(self, audio_type, file_name):
    
        if audio_type == "vlc":
            self.advanced_player.play_vlc(file_name)
        elif audio_type == "mp4":
            self.advanced_player.play_mp4(file_name)

# Concrete Adaptee
class AdvancedMediaPlayerVlc(AdvancedMediaPlayer):
    def play_vlc(self, file_name):
        print("Playing VLC file:", file_name)

class AdvancedMediaPlayerMp4(AdvancedMediaPlayer):
    def play_mp4(self, file_name):
        print("Playing MP4 file:", file_name)

# Concrete Target
class AudioPlayer(MediaPlayer):
    def play(self, audio_type, file_name):
        if audio_type == "mp3":
            print("Playing MP3 file:", file_name)
        elif audio_type in ("vlc", "mp4"):
            media_adapter = MediaAdapter(audio_type)
            media_adapter.play(audio_type, file_name)
        else:
            print("Invalid audio type:", audio_type)

# Client code
if __name__ == "__main__":
    player = AudioPlayer()

    player.play("mp3", "song.mp3")
    player.play("vlc", "movie.vlc")
    player.play("mp4", "video.mp4")
    player.play("avi", "video.avi")
