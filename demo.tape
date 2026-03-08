# drinkfyi — Python Beverage Hub Demo
Output demo.gif

Set FontSize 20
Set Width 1000
Set Height 580
Set Shell "zsh"
Set Theme "Catppuccin Mocha"
Set TypingSpeed 30ms
Set Padding 24

Type "uv run --with drinkfyi python3"
Enter
Sleep 2s

Type "from drinkfyi import available_clients, get_client"
Enter
Sleep 1s

Type "available_clients()"
Enter
Sleep 1.5s

Type "# Cross-beverage search"
Enter
Sleep 0.5s

Type "c = get_client('cocktail')"
Enter
Sleep 1s

Type "c.search('negroni')"
Enter
Sleep 2.5s

Type "exit()"
Enter
Sleep 1s
