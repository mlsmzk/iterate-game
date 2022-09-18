# iterate-game
Small CLI Game for Iterate

# Instructions

To draw a card, players run the file in the following format:

`python3 iterate_game.py [card_type] [card_arguments]`

Where card_type indicates the kind of card that you want to draw (Experience, School, etc.) and card_arguments gives the randomizer extra information (Experience Level, School Level, etc.).

Below is an example:
`python3 iterate_game.py school ms`

`Output
name : Pineapple
reqs : None
unlocks : hs and lvl2
pref : None`

This example asks for the draw of a middle school card.

### School Cards
School cards have 4 levels: "es", "ms", "hs", and "c". See the example above for usage.