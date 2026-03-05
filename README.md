# drinkfyi

Unified beverage knowledge hub — cocktails, wine, beer, whiskey, tea, coffee, and sake in one package. Part of the [FYIPedia](https://fyipedia.com) ecosystem.

## Install

```bash
pip install drinkfyi[all]            # Everything (7 beverage packages + CLI)
pip install drinkfyi[cocktail]       # Cocktail engine only
pip install drinkfyi[wine,beer]      # Wine + beer clients
pip install drinkfyi[cli]            # CLI only (no beverage packages)
```

### Available extras

| Extra | Package | Site |
|-------|---------|------|
| `cocktail` | [cocktailfyi](https://pypi.org/project/cocktailfyi/) | [cocktailfyi.com](https://cocktailfyi.com) |
| `wine` | [vinofyi](https://pypi.org/project/vinofyi/) | [vinofyi.com](https://vinofyi.com) |
| `beer` | [beerfyi](https://pypi.org/project/beerfyi/) | [beerfyi.com](https://beerfyi.com) |
| `whiskey` | [whiskeyfyi](https://pypi.org/project/whiskeyfyi/) | [whiskeyfyi.com](https://whiskeyfyi.com) |
| `tea` | [teafyi](https://pypi.org/project/teafyi/) | [teafyi.com](https://teafyi.com) |
| `coffee` | [brewfyi](https://pypi.org/project/brewfyi/) | [brewfyi.com](https://brewfyi.com) |
| `sake` | [nihonshufyi](https://pypi.org/project/nihonshufyi/) | [nihonshufyi.com](https://nihonshufyi.com) |

## Quick Start

```python
from drinkfyi import available_clients, get_client

# See what's installed
print(available_clients())  # ['cocktail', 'wine', 'beer', ...]

# Get a client by type
client = get_client("cocktail")
results = client.search("margarita")
client.close()

# Or use individual packages directly
from cocktailfyi import parse_measure_ml
ml = parse_measure_ml("1 1/2 oz")  # 45.0
```

## CLI

```bash
drinkfyi list                          # List installed packages
drinkfyi search cocktail margarita     # Search via specific client
drinkfyi search wine "pinot noir"      # Search wines
drinkfyi search beer ipa               # Search beers
```

## Links

- [FYIPedia](https://fyipedia.com) — Open-source developer tools ecosystem
- [GitHub](https://github.com/fyipedia/drinkfyi)
- [PyPI](https://pypi.org/project/drinkfyi/)
