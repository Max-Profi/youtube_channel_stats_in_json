from statistics import YouTubeStats

API_KEY = 'AIzaSyAf5XnX2imU3KqPaRqBJukhm3LkHmsSn0k'

channel_id ='UCLZIN4aTXYm92c1ENyN8KmA'


if __name__ == "__main__":
    channel_stats = YouTubeStats(API_KEY, channel_id, 'Amway921')

    channel_stats.get_channel_stats()

    channel_stats.stats_to_json_file()
