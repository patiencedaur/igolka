from db_utils import GetGames, DatabaseInit

# d = DatabaseInit()
# d.create_db()
# d.fill_db()
# d.print_db()
# print()

g = GetGames()
# g.get_by_title('Azul')

query = {"player_num": "3", "playing_minutes": "30", "coco": "Cooperative"}
g.search_db(query)
