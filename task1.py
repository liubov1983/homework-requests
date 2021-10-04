import requests

hero_list = ['Hulk', 'Captain America', 'Thanos']
heros = {}

def get_intelligence(hero_name):
    
    for hero in hero_name:
        url = 'https://superheroapi.com/api/2619421814940190/search/' + hero
        response = requests.get(url=url)
        resp = response.json()
        for result in resp['results']:
            if result['name'] == hero:
                heros[hero] = int(result['powerstats']['intelligence'])
    

def compare_intelligence(heros):
    max_count = 0
    for item in heros.values():
        if item > max_count:
            max_count = item

    for key, value in heros.items():
        if value == max_count:
            print(f'Самый умный - {key}')


def main(hero_list, heros):
    get_intelligence(hero_list)
    compare_intelligence(heros)

if __name__ == '__main__':
    main(hero_list, heros)