import googleapiclient.discovery

def get_channel_videos():
    # Prompts the user for the API key and the channel ID
    api_key = input("Enter your API Key: ")
    channel_id = input("Enter the YouTube Channel ID: ")

    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

    def fetch_videos(channel_id):
        # Get the uploads playlist id
        res = youtube.channels().list(id=channel_id, part='contentDetails').execute()
        playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        
        videos = []
        next_page_token = None

        while True:
            res = youtube.playlistItems().list(playlistId=playlist_id, 
                                               part='snippet', 
                                               maxResults=50,
                                               pageToken=next_page_token).execute()
            videos += res['items']
            next_page_token = res.get('nextPageToken')
            
            if next_page_token is None:
                break

        return videos

    # Fetch videos from the specified channel
    videos = fetch_videos(channel_id)
    for video in videos:
        print(video['snippet']['title'])

# Call the function to start the process
if __name__ == "__main__":
    get_channel_videos()
