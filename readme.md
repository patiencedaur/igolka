### Darky & Patience's Board Games Database ###

This project lists boardgames that we have in our home, including number of players, mechanics, themes, playing time, etc.
Part of the data is received via BoardGameGeek API and part is parsed from the webpage as it is not available through the client API.

I am planning to add integration with our account on boardgamegeek.com so we could submit number of plays and rate games.

#### scraper ####
Gets and parses the html document with collection, retrieving game names and urls.

#### parser ####
Opens each game page, getting info like number of players, mechanics, etc.
