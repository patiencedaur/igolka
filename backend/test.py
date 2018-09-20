from db_utils import GetGames, DatabaseInit

# d = DatabaseInit()
# d.print_db()
g = GetGames()
g.get_by_title('Sagrada')
