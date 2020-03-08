import tweepy
from gtts import gTTS
from moviepy.editor import *

auth = tweepy.OAuthHandler('')
auth.set_access_token('',
                      '')
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
print("running")


class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        tweetid = status.id
        tweetnouser = status.text.replace("@CarlWheezerBot", "")
        username = '@' + status.user.screen_name

        user_tweet = gTTS(text=tweetnouser, lang='en', slow=False)

        # Saving the converted audio

        user_tweet.save("useraudio/text2speech.mp3")

        # importing the audio and getting the audio all mashed up
        text2speech = AudioFileClip("useraudio/text2speech.mp3")
        videoclip = VideoFileClip("original_video/original_cut.mp4")
        editedAudio = videoclip.audio

        # splicing the original audio with the text2speech
        compiledAudio = CompositeAudioClip([editedAudio.set_duration(3.8), text2speech.set_start(3.8)])
        videoclip.audio = compiledAudio

        # saving the completed video fie
        videoclip.write_videofile("user_video/edited.mp4", audio_codec='aac')

        upload_result = api.media_upload("user_video/edited.mp4")
        api.update_status(in_reply_to_status_id=tweetid, media_ids=[upload_result.media_id_string],
                          auto_populate_reply_metadata=True)

    def on_error(self, status_code):
        if status_code == 420:
            return False

    def on_exception(self, exception):
        print(exception)
        return


def retweet(id_string):
    api.retweet(id_string)
    return


stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=['@carlwheezerbot'])
