import scrape_game as sc

'''
Tests the scrape_game module
'''

def test_get_game_info():
    print("Testing get_game_info with Sagrada:", end=' ')
    try:
        sc.get_game_info('https://boardgamegeek.com/boardgame/199561/sagrada')
    finally:
        print()

if __name__ == '__main__':
    test_get_game_info()
