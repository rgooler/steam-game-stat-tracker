
#!/usr/bin/env python
# encoding: utf-8
from steamgamestattracker.steamapi import SteamAPI
import json
import sys


def main():
    steam = SteamAPI(apikey="B3E1C11C73B61B18C4A340CB1B464115")
    # jippen = "76561197993843660"
    # games = steam.GetOwnedGames(jippen)
    # game = games['response']['games'][0]['appid']
    # todo: for loop this
    # schema = steam.GetSchemaForGame(218620)
    # print(json.dumps(schema, sort_keys=True, indent=2))

    print(json.dumps(steam.GetSchemaForGame(218620), sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
