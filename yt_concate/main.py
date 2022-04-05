import urllib.request
import json
from yt_concate.settings import API_KEY

print(API_KEY)

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def get_all_video_in_channel(channel_id):
    # api_key = 'AIzaSyAUZ7tdcFuwo_B78-qWZxeEk1PJoq7wFN4'  # 我的api_key

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'  # 讓我們使用API的網址，術語叫做endpoint

    first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                        channel_id)

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except KeyError:
            break
    return video_links

# video_list = get_all_video_in_channel(CHANNEL_ID)
# print(len(video_list))
