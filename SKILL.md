---
name: drink-tools
description: Unified beverage hub -- access cocktails, wine, beer, whiskey, tea, coffee, and sake through a single package. Use when searching across multiple beverage categories or when the user's question spans multiple drink types.
license: MIT
metadata:
  author: fyipedia
  version: "0.1.1"
  homepage: "https://drinkfyi.com/"
---

# DrinkFYI -- Unified Beverage Tools for AI Agents

Unified beverage knowledge hub for Python. Access cocktails, wine, beer, whiskey, tea, coffee, and sake through a single package. DrinkFYI aggregates 7 specialized beverage APIs into one interface -- search across 636 cocktail recipes, 777 grape varieties, 112 beer styles, 80 whiskey expressions, 60 tea varieties, 72 coffee varieties, and 80 sake expressions.

**Install**: `pip install drinkfyi[all]` -- **Web**: [drinkfyi.com](https://drinkfyi.com/) -- **PyPI**: [drinkfyi](https://pypi.org/project/drinkfyi/)

## When to Use

- User asks a question that spans multiple beverage categories
- User needs to search across cocktails, wine, beer, coffee, whiskey, tea, and sake simultaneously
- User wants a unified interface to all Beverage FYI sites
- User asks a general beverage question without specifying a category

## Tools

### `available_clients() -> list[str]`

Return list of installed beverage package names.

```python
from drinkfyi import available_clients

print(available_clients())  # ['cocktail', 'wine', 'beer', 'whiskey', 'tea', 'coffee', 'sake']
```

### `get_client(beverage_type: str) -> Any`

Get an API client instance for a beverage type. Returns the corresponding API client (CocktailFYI, VinoFYI, BeerFYI, etc.).

```python
from drinkfyi import get_client

# Get a client by beverage type
client = get_client("cocktail")
results = client.search("margarita")
client.close()

# Available types: 'cocktail', 'wine', 'beer', 'whiskey', 'tea', 'coffee', 'sake'
```

### Direct Package Usage

Each beverage package can be used independently:

```python
# Cocktails -- includes local computation engine
from cocktailfyi import parse_measure_ml, estimate_abv
ml = parse_measure_ml("1 1/2 oz")  # 45.0

# Wine
from vinofyi.api import VinoFYI
with VinoFYI() as api:
    results = api.search("pinot noir")

# Beer
from beerfyi.api import BeerFYI
with BeerFYI() as api:
    results = api.search("ipa")

# Coffee
from brewfyi.api import BrewFYI
with BrewFYI() as api:
    results = api.search("espresso")

# Whiskey
from whiskeyfyi.api import WhiskeyFYI
with WhiskeyFYI() as api:
    results = api.search("bourbon")

# Tea
from teafyi.api import TeaFYI
with TeaFYI() as api:
    results = api.search("matcha")

# Sake
from nihonshufyi.api import NihonshuFYI
with NihonshuFYI() as api:
    results = api.search("junmai daiginjo")
```

### `BEVERAGE_PACKAGES`

Registry mapping beverage types to their package modules and client classes.

```python
from drinkfyi import BEVERAGE_PACKAGES

# {'cocktail': ('cocktailfyi.api', 'CocktailFYI'),
#  'wine': ('vinofyi.api', 'VinoFYI'),
#  'beer': ('beerfyi.api', 'BeerFYI'),
#  'whiskey': ('whiskeyfyi.api', 'WhiskeyFYI'),
#  'tea': ('teafyi.api', 'TeaFYI'),
#  'coffee': ('brewfyi.api', 'BrewFYI'),
#  'sake': ('nihonshufyi.api', 'NihonshuFYI')}
```

## REST API (No Auth Required)

Each beverage site exposes a consistent set of endpoints. All are free, no auth, JSON with CORS.

```bash
# Search across cocktails
curl "https://cocktailfyi.com/api/search/?q=margarita"

# Get a specific beer style
curl "https://beerfyi.com/api/v1/styles/new-england-ipa/"

# Compare two wines
curl "https://vinofyi.com/api/v1/compare/pinot-noir/cabernet-sauvignon/"

# Sake detail
curl "https://nihonshufyi.com/api/v1/sake/dassai-23/"

# Coffee variety
curl "https://brewfyi.com/api/v1/varieties/gesha/"

# Whiskey detail
curl "https://whiskeyfyi.com/api/v1/whiskeys/lagavulin-16/"

# Tea detail
curl "https://teafyi.com/api/v1/teas/matcha/"
```

## Available Packages

| Extra | Package | Site | Data |
|-------|---------|------|------|
| `cocktail` | [cocktailfyi](https://pypi.org/project/cocktailfyi/) | [cocktailfyi.com](https://cocktailfyi.com) | 636 recipes, 15 families, ABV/calorie engine |
| `wine` | [vinofyi](https://pypi.org/project/vinofyi/) | [vinofyi.com](https://vinofyi.com) | 777 grapes, regions, wineries, 741K records |
| `beer` | [beerfyi](https://pypi.org/project/beerfyi/) | [beerfyi.com](https://beerfyi.com) | 112 styles, 82 hops, 41 malts, 29 yeast |
| `coffee` | [brewfyi](https://pypi.org/project/brewfyi/) | [brewfyi.com](https://brewfyi.com) | 72 varieties, 20 origins, 21 brew methods |
| `whiskey` | [whiskeyfyi](https://pypi.org/project/whiskeyfyi/) | [whiskeyfyi.com](https://whiskeyfyi.com) | 80 expressions, 13 regions, 7 countries |
| `tea` | [teafyi](https://pypi.org/project/teafyi/) | [teafyi.com](https://teafyi.com) | 60 varieties, 15 teaware, 7 categories |
| `sake` | [nihonshufyi](https://pypi.org/project/nihonshufyi/) | [nihonshufyi.com](https://nihonshufyi.com) | 80 sake, 10 rice varieties, 50 breweries |

## Install Options

```bash
pip install drinkfyi[all]            # Everything (7 packages + CLI)
pip install drinkfyi[cocktail]       # Cocktail engine only
pip install drinkfyi[wine,beer]      # Wine + beer clients
pip install drinkfyi[cli]            # CLI only
```

## Beverage FYI Family

Part of the [FYIPedia](https://fyipedia.com) ecosystem: [CocktailFYI](https://cocktailfyi.com), [VinoFYI](https://vinofyi.com), [BeerFYI](https://beerfyi.com), [BrewFYI](https://brewfyi.com), [WhiskeyFYI](https://whiskeyfyi.com), [TeaFYI](https://teafyi.com), [NihonshuFYI](https://nihonshufyi.com).
