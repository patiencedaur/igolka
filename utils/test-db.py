from db_utils import GetGames, DatabaseInit

def test1():
    d = DatabaseInit()
    d.create_db()
    d.fill_db()
    d.print_db()
    print()

def test2():
    g = GetGames()
    g.get_by_title('Azul')

def test3():
    g = GetGames()
    query = {'player_num': '2', 'coco': 'Competitive'}
    g.search_db(query)

def test4():
    DatabaseInit().drop_sync()

if __name__ == "__main__":

    print("You can perform the following database tests:")
    print("(1) Initialize + fill + print database")
    print("(2) Get game by title (defaults to Azul)")
    print("(3) Search by player_num = 2 and coco = 'Competitive'")
    print("(4) Drop and sync")

    prompt = input("Enter number of test to perform: ")

    test_name = "test" + prompt

    try:
        eval(test_name + "()")
    except:
        print("Invalid test id.")
