import googleapiclient.discovery
import json

def get_channel_videos():
    # Prompt the user for the API key and the channel ID
    api_key = input("Enter your API Key: ")
    channel_id = input("Enter the YouTube Channel ID: ")

    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

    def fetch_channel_title(channel_id):
        # Fetch the channel's title
        res = youtube.channels().list(id=channel_id, part='snippet').execute()
        return res['items'][0]['snippet']['title']

    def fetch_video_details(video_id):
        # Fetch video details including view count
        res = youtube.videos().list(id=video_id, part='statistics').execute()
        return res['items'][0]['statistics']

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
            for item in res['items']:
                # Copy the item dict excluding the 'thumbnails' from 'snippet'
                video_info = item['snippet'].copy()
                video_info.pop('thumbnails', None)  # Remove thumbnails if exists
                video_id = video_info['resourceId']['videoId']
                video_details = fetch_video_details(video_id)
                
                # Create a new dict for the video excluding thumbnails
                new_item = {
                    'snippet': video_info,
                    'statistics': video_details
                }
                videos.append(new_item)
                
            next_page_token = res.get('nextPageToken')
            
            if next_page_token is None:
                break

        return videos

    channel_title = fetch_channel_title(channel_id)
    videos = fetch_videos(channel_id)
    
    # Format the filename to remove characters not suitable for filenames
    safe_channel_title = "".join([c for c in channel_title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
    filename = f"{safe_channel_title}_videos.json"
    
    # Save the videos and their view counts to a JSON file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(videos, f, ensure_ascii=False, indent=4)

    print(f"Video list with view counts saved to {filename}")

# Call the function to start the process
if __name__ == "__main__":
    get_channel_videos()
