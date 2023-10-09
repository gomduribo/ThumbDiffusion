from googleapiclient.discovery import build
from requests import get  # to make GET request

def download(url, file_name):
    with open(file_name, "wb") as file:   # open in binary mode
        response = get(url)               # get request
        file.write(response.content)      # write to file



# Replace with your own API key
# API_KEY = "AIzaSyALGaWS2fifI8pRHIUA9HLwG_0ukcTryQQ"
API_KEY = "AIzaSyD3cif5mEMSA6YUZviii-QfjsiOraek_4I"

# Create a YouTube API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Call the API to search for videos
search_response = youtube.search().list(
    q="침착맨",
    type='video',
    part='=id,snippet',
    location='37, 127',
    locationRadius='100km',
    # 한국 동영상 한정
    order = 'viewCount',
    # 조회수 순으로 다운
    maxResults=5
).execute()
count = 0
# Print the titles of the search results
for search_result in search_response.get('items', []):
    count+=1
    print(search_result['id']['videoId'])
    # print(search_result['snippet']['thumbnails'])
    if __name__ == '__main__':

        url = "https://img.youtube.com/vi/"+search_result['id']['videoId']+"/maxresdefault.jpg"
        # youtube thumbnail url을 가져옴
        download(url,str(count)+".jpg")
        # 다운로드 경로 설정 필요
    