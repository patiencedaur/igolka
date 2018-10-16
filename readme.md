# Igolka - Darky & Patience's Board Games Database

This is a project for personal use.

Igolka is a boardgames database and a search tool. It connects with our profile on [BoardGameGeek](http://BoardGameGeek.com) via [BoardGameGeek API](https://github.com/lcosmin/boardgamegeek) and uses the [BoardGameGeek JSON API Wrapper](http://bgg-json.azurewebsites.net/).

Igolka lists boardgames that we have in our home, including number of players, mechanics, playing time, etc.

## Notes to myself

Before running, install dependencies:
`pip install -r requirements.txt`

Then, run `python3 dropsync.py` to initialize the database. You're all set!

Run `python3 dropsync.py` every time we add new games to our BoardGameGeek collection.
