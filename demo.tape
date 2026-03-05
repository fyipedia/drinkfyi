# drinkfyi — Python Beverage Hub Library Demo
Output demo.gif

Set FontSize 14
Set Width 920
Set Height 620
Set Shell "zsh"
Set Theme "Catppuccin Mocha"
Set TypingSpeed 35ms
Set Padding 20

Type `python -c "from drinkfyi import available_clients; print('Installed:', available_clients())"`
Enter
Sleep 2s

Type `python -c "from drinkfyi import get_client; c = get_client('cocktail'); r = c.search('negroni'); print(r['query'], '→', len(r.get('results',[])), 'results')"`
Enter
Sleep 3s

Type `python -c "from drinkfyi import get_client; c = get_client('wine'); r = c.search('merlot'); print(r['query'], '→', len(r.get('results',[])), 'results')"`
Enter
Sleep 3s

Sleep 2s
