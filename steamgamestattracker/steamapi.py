import requests
import json

class SteamAPI():
    def __init__(self, apikey):
        self.apikey = apikey
        self.r = requests.Session()

    def get(self, path, version, params={}):
        params['format'] = 'json'
        url = "https://api.steampowered.com/%s/%s/" % (path, version)
        r = self.r.get(url, params=params)
        return r.json()

    def GetSupportedAPIList(self):
        '''Get all APIs'''
        path = "ISteamWebAPIUtil/GetSupportedAPIList"
        version = "v0001"
        params = {}
        return self.get(path, version, params)

    # GetNewsForApp (v0002)
    def GetNewsForApp(self, appid, count=1, maxlength=300):
        '''GetNewsForApp returns the latest of a game specified by its appID.'''
        path = "ISteamNews/GetNewsForApp"
        version = "v0002"
        params = {
            "appid": appid,
            "count": count,
            "maxlength": maxlength
        }
        return self.get(path, version, params)

    # GetGlobalAchievementPercentagesForApp (v0002)
    def GetGlobalAchievementPercentagesForApp(self, gameid):
        '''Returns on global achievements overview of a specific game in percentages.'''
        path = "ISteamUserStats/GetGlobalAchievementPercentagesForApp"
        version = "v0002"
        params = {
            "gameid": gameid
        }
        return self.get(path, version, params)

    # GetGlobalStatsForGame (v0001)
    def GetGlobalStatsForGame(self, appid, name=[], count=1):
        """
        Note: name is a list of achievement names
        """
        path = 'ISteamUserStats/GetGlobalStatsForGame'
        version = 'v0001'
        params = {
            'appid': appid,
            'count': count
        }
        i = 0
        for n in name:
            params["name[%s]" % i] = n
            i += 1
        print(params)
        return self.get(path, version, params)

    # GetPlayerSummaries (v0002)
    def GetPlayerSummaries(self, steamids):
        '''Returns basic profile information for a list of 64-bit Steam IDs.'''
        path = "ISteamUser/GetPlayerSummaries"
        version = "v0002"
        params = {
            "key": self.apikey,
            "steamids": steamids
        }
        return self.get(path, version, params)

    # GetFriendList (v0001)
    def GetFriendList(self, steamid, relationship='friend'):
        '''Returns the friend list of any Steam user, provided their Steam Community profile visibility is set to "Public".'''
        path = "ISteamUser/GetFriendList"
        version = "v0001"
        params = {
            "key": self.apikey,
            "steamid": steamid,
            "relationship": relationship
        }
        return self.get(path, version, params)

    # GetPlayerAchievements (v0001)
    def GetPlayerAchievements(self, appid, steamid, l="en"):
        '''Returns a list of achievements for this user by app id'''
        path = "ISteamUserStats/GetPlayerAchievements"
        version = "v0001"
        params = {
            "key": self.apikey,
            "steamid": steamid,
            "appid": appid,
            "l": l
        }
        return self.get(path, version, params)

    # GetUserStatsForGame (v0002)
    def GetUserStatsForGame(self, appid, steamid, l="en"):
        '''Returns a list of achievements for this user by app id'''
        path = "ISteamUserStats/GetUserStatsForGame"
        version = "v0002"
        params = {
            "key": self.apikey,
            "steamid": steamid,
            "appid": appid,
            "l": l
        }
        return self.get(path, version, params)

    # GetOwnedGames (v0001)
    def GetOwnedGames(self, steamid, include_appinfo=False, include_played_free_games=False, appids_filter=[]):
        '''
        GetOwnedGames returns a list of games a player owns along with some 
        playtime information, if the profile is publicly visible. Private, 
        friends-only, and other privacy settings are not supported unless you 
        are asking for your own personal details (ie the WebAPI key you are 
        using is linked to the steamid you are requesting).
        '''
        path = "IPlayerService/GetOwnedGames"
        version = "v0001"
        params = {
            "key": self.apikey,
            "steamid": steamid,
            "include_appinfo": include_appinfo,
            "include_played_free_games": include_played_free_games,
            "appids_filter": appids_filter,
        }
        return self.get(path, version, params)

    # GetRecentlyPlayedGames (v0001)
    def GetRecentlyPlayedGames(self, steamid, count=200):
        '''
        GetRecentlyPlayedGames returns a list of games a player has played in 
        the last two weeks, if the profile is publicly visible. Private, 
        friends-only, and other privacy settings are not supported unless you 
        are asking for your own personal details (ie the WebAPI key you are 
        using is linked to the steamid you are requesting).
        '''
        path = "IPlayerService/GetRecentlyPlayedGames"
        version = "v0001"
        params = {
            "key": self.apikey,
            "steamid": steamid,
            "count": count
        }
        return self.get(path, version, params)
    
    # IsPlayingSharedGame (v0001)
    def IsPlayingSharedGame(self, steamid, appid_playing):
        '''
        IsPlayingSharedGame returns the original owner's SteamID if a borrowing 
        account is currently playing this game. If the game is not borrowed or 
        the borrower currently doesn't play this game, the result is always 0.
        '''
        path = "IPlayerService/IsPlayingSharedGame"
        version = "v0001"
        params = {
            "key": self.apikey,
            "steamid": steamid,
            "appid_playing": appid_playing
        }
        return self.get(path, version, params)

    # GetSchemaForGame (v2)
    def GetSchemaForGame(self, appid):
        '''
        GetSchemaForGame returns gamename, gameversion and availablegamestats
        (achievements and stats).
        '''
        path = "ISteamUserStats/GetSchemaForGame"
        version = "v2"
        params = {
            "key": self.apikey,
            "appid": appid,
        }
        return self.get(path, version, params)

    # GetPlayerBans (v1)
    def GetPlayerBans(self, steamids):
        '''
        GetPlayerBans returns Community, VAC, and Economy ban statuses for 
        given players.
        '''
        path = "ISteamUser/GetPlayerBans"
        version = "v1"
        params = {
            "key": self.apikey,
            "steamids": steamids,
        }
        return self.get(path, version, params)