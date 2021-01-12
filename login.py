import requests

league_id = 400089
year = 2019
url = "https://fantasy.espn.com/apis/v3/games/ffl/draftDetail/" + str(league_id) + "?seasonId" + str(year)

r = requests.get(url, cookies={
    "swid": "{983D30EC-0732-45DA-B8E9-67A254362394}",
    "espn_s2": "AECMfn3Tnw8gf5yS1PRaX%2BHZZJJA4UBMiXhOc2ARgRyNAGBMaDJKo0s%2B1jC4lDdF4Vd5FfdEkNgQxXfFwQ3cTLRDD6KEc2AGTXTNEb3blXeCR9csPkE5ONvo8rw5N4w5BETQTMAy8J5WuF904%2FdAJVe6ZRMEyexwXes7fj%2BgppdB4I%2BYkxxxhW%2BdMmM7rwlrawIkRrm8Rraq22M171if46FO70Kfwsst3Rpzgt0yn99PCYmqTHy8hNYgS%2FHIIldYNevpynPqUWFSDtYwQL0AQeMi"
})


print(r.json())