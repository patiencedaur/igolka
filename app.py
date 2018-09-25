from flask import Flask, render_template, request, redirect
from utils.db_utils import GetGames

app = Flask(__name__)
app.config['TESTING'] = True

#Start page
@app.route("/")
def index():
    return render_template("index.html")

#Search results page
@app.route("/gamekeeper")
def gamekeeper():
    return render_template("gamekeeper.html")

#Actual search engine
@app.route("/search", methods=["POST"])
def search():

    try:
        query = {}
        # Forming a query to the database
        if len(request.form.get("title")) != 0:
            query["title"] = request.form.get("title")
        query["player_num"] = request.form.get("playerNum"))
        query["playing_minutes"] = request.form.get("playingMinutes")
        query["coco"] = request.form.get("coco")

        if not query:
            print("Looks like the query is empty... Try again")
            return redirect("/")

        #here comes the code that searches in the db...

        return redirect("/gamekeeper")

    except:
        return render_template("error.html")

    finally:
        print(query)



# Helps to check if a number was entered (or field is empty)
# def is_number(s):
#     if not s:
#         return True
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except (TypeError, ValueError):
#         pass
#     return False
