import requests
import json

if __name__ == "__main__":
    print('You should run youtube.api file')

class YouTubeStats:
    def __init__(self, api_key, channel_id, channel_title):
        self.api_key = api_key
        self.channel_title = channel_title
        self.channel_id = channel_id
        self.channel_stats = None


    def get_channel_stats(self):
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            data = data['items'][0]['statistics']
            self.channel_stats = {**{"channel_title": f"{self.channel_title}"}, **data}
        else:
            self.channel_stats = None
            print('Response error status code:', response.status_code)
        return self.channel_stats


    def stats_to_json_file(self):
        if self.channel_stats is None:
            return 'There is no stats'
        file_name = f"{self.channel_title}.json"
        with open(file_name, 'w') as f:
            json.dump(self.channel_stats, f)
            f.write("\n\n")
        print('JSON file with channel stats is created')
