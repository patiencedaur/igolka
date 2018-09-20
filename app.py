from flask import Flask, render_template, request, redirect

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
    title = request.form.get("name")
    player_num_min = request.form.get("playerMin")
    player_num_max = request.form.get("playerMax")
    playing_minutes = request.form.get("playingMinutes")
    coco = request.form.get("coco")

    #Console log
    print("Searching for game...")
    print("Title: " + title)
    print("Min Players: " + player_num_min)
    print("Max Players: " + player_num_max)
    print("Playing Time: " + playing_minutes)
    print("PVP or Coop: " + coco)

    #Check if player_num_min and player_num_max are numbers
    numberCondition = is_number(player_num_min) and \
                    is_number(player_num_max)
    if not numberCondition:
        return render_template("error.html")

    return redirect("/gamekeeper")

# Helps to check if a number was entered (or field is empty)
def is_number(s):
    if not s:
        return True
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False
