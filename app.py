from flask import Flask, render_template, request, redirect
from utils.db_utils import GetGames

app = Flask(__name__)
# app.config['TESTING'] = True

#Start page
@app.route("/")
def index():
    return render_template("index.html")

#Actual search engine
@app.route("/search", methods=["POST"])
def search():
    try:
        query = {}
        search_results = []
        # Forming a query to the database and a redirect address
        for req in request.form:
            if len(request.form.get(req)) != 0:
                query[req] = to_ascii(request.form.get(req))

        if not query:
            print("Looks like the query is empty... Try again")
            return redirect("/")

        search_results = GetGames().search_db(query)

        return render_template("gamekeeper.html", search_results=search_results)

    except:
        return render_template("error.html")

    # finally:
    #     print("Query: ")
    #     print(query)
    #     print("Search results: ")
    #     print(search_results)


def to_ascii(s):
    '''Convert string to ascii to search in the db.'''
    return s.encode('raw_unicode_escape')
