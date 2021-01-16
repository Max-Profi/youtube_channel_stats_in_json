from statistics import YouTubeStats

API_KEY = 'set your youtube data api here'

channel_id ='channel id'

channel_title = 'channel title'


if __name__ == "__main__":
    channel_stats = YouTubeStats(API_KEY, channel_id, channel_title)

    channel_stats.get_channel_stats()

    channel_stats.stats_to_json_file()
