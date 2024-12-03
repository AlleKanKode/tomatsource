import requests
import datetime

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return []

def main(base_url, start_datetime, iterations, max_results):
    current_datetime = start_datetime
    tracks_list = []

    for _ in range(iterations):
        formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
        url = f"{base_url}/{formatted_datetime}/{max_results}"
        data = fetch_data(url)

        for track in data:
            track_info = {
                "artist": track["nowPlayingArtist"],
                "track": track["nowPlayingTrack"]
            }
            tracks_list.append(track_info)

        if data:
            last_play_time_str = data[-1]["nowPlayingTime"]
            current_datetime = datetime.datetime.strptime(last_play_time_str, '%Y-%m-%d %H:%M:%S')
        else:
            break

    return tracks_list

if __name__ == "__main__":
    base_url = "https://listenapi.planetradio.co.uk/api9.2/events/tar"
    #start_datetime = datetime.datetime.strptime('2024-11-13 22:49:00', '%Y-%m-%d %H:%M:%S')
    start_datetime = datetime.datetime.now()
    iterations = 5  # Antal iterationer
    max_results = 100  # Antal resultater pr. anmodning

    tracks = main(base_url, start_datetime, iterations, max_results)
    for track in tracks:
        print(f"Artist: {track['artist']}, Track: {track['track']}")