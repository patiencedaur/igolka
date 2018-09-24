from db_utils import GetGames, DatabaseInit

d = DatabaseInit()
d.create_db()
d.fill_db()
d.print_db()
print()

g = GetGames()
g.get_by_title('Azul')
