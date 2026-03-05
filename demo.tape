# drinkfyi — Interactive Python REPL Demo
Output demo.gif

Set FontSize 14
Set Width 920
Set Height 620
Set Shell "zsh"
Set Theme "Catppuccin Mocha"
Set TypingSpeed 30ms
Set Padding 20

# Install + REPL in one command (uv creates temp env)
Type "uv run --with drinkfyi python3"
Enter
Sleep 2.5s

# Import and check available clients
Type "from drinkfyi import available_clients, get_client"
Enter
Sleep 1.5s

Type "available_clients()"
Enter
Sleep 1.5s

# Cross-beverage search: cocktails
Type "c = get_client('cocktail')"
Enter
Sleep 1s

Type "c.search('negroni')"
Enter
Sleep 2.5s

# Cross-beverage search: wine
Type "w = get_client('wine')"
Enter
Sleep 1s

Type "w.search('merlot')"
Enter
Sleep 2.5s

Type "exit()"
Enter
Sleep 1s
