from ytmusicapi import YTMusic


ytmusic = YTMusic('headers_auth.json')
PLAYLIST_ID = ""
FILENAME = ""


with open(FILENAME) as f:
    for line in f:
        search_results = ytmusic.search(line[0:-1])
        try:
            id = search_results[0]['videoId']
            ytmusic.add_playlist_items(PLAYLIST_ID, [id])
        except KeyError as e:
            id = search_results[1]['videoId']
            ytmusic.add_playlist_items(PLAYLIST_ID, [id])
        finally:
            continue
