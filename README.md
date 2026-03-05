# drinkfyi

[![PyPI](https://img.shields.io/pypi/v/drinkfyi)](https://pypi.org/project/drinkfyi/)
[![Python](https://img.shields.io/pypi/pyversions/drinkfyi)](https://pypi.org/project/drinkfyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Unified beverage knowledge hub for Python. Access cocktails, wine, beer, whiskey, tea, coffee, and sake through a single package. DrinkFYI aggregates 7 specialized beverage APIs into one unified interface -- search across 636 cocktail recipes, 777 grape varieties, 112 beer styles, 80 whiskey expressions, 60 tea varieties, 72 coffee varieties, and 80 sake expressions. Part of the [FYIPedia](https://fyipedia.com) developer tools ecosystem.

> **Explore beverages** -- [CocktailFYI](https://cocktailfyi.com) | [VinoFYI](https://vinofyi.com) | [BeerFYI](https://beerfyi.com) | [BrewFYI](https://brewfyi.com) | [WhiskeyFYI](https://whiskeyfyi.com) | [TeaFYI](https://teafyi.com) | [NihonshuFYI](https://nihonshufyi.com)

<p align="center">
  <img src="demo.gif" alt="drinkfyi demo -- unified beverage search across 7 sites" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Available Packages](#available-packages)
- [Quick Start](#quick-start)
- [What You'll Find Across the Beverage FYI Family](#what-youll-find-across-the-beverage-fyi-family)
  - [Cocktails (CocktailFYI)](#cocktails-cocktailfyi)
  - [Wine (VinoFYI)](#wine-vinofyi)
  - [Beer (BeerFYI)](#beer-beerfyi)
  - [Coffee (BrewFYI)](#coffee-brewfyi)
  - [Whiskey (WhiskeyFYI)](#whiskey-whiskeyfyi)
  - [Tea (TeaFYI)](#tea-teafyi)
  - [Sake (NihonshuFYI)](#sake-nihonshufyi)
- [Command-Line Interface](#command-line-interface)
- [API Endpoints](#api-endpoints)
- [Using Individual Packages](#using-individual-packages)
- [Learn More About Beverages](#learn-more-about-beverages)
- [Beverage FYI Family](#beverage-fyi-family)
- [FYIPedia Developer Tools](#fyipedia-developer-tools)
- [License](#license)

## Install

```bash
pip install drinkfyi[all]            # Everything (7 beverage packages + CLI)
pip install drinkfyi[cocktail]       # Cocktail engine only
pip install drinkfyi[wine,beer]      # Wine + beer clients
pip install drinkfyi[cli]            # CLI only (no beverage packages)
```

## Available Packages

Install only the beverage categories you need:

| Extra | Package | Site | Data |
|-------|---------|------|------|
| `cocktail` | [cocktailfyi](https://pypi.org/project/cocktailfyi/) | [cocktailfyi.com](https://cocktailfyi.com) | 636 recipes, 15 families, ABV/calorie engine |
| `wine` | [vinofyi](https://pypi.org/project/vinofyi/) | [vinofyi.com](https://vinofyi.com) | 777 grapes, regions, wineries, 741K records |
| `beer` | [beerfyi](https://pypi.org/project/beerfyi/) | [beerfyi.com](https://beerfyi.com) | 112 styles, 82 hops, 41 malts, 29 yeast |
| `coffee` | [brewfyi](https://pypi.org/project/brewfyi/) | [brewfyi.com](https://brewfyi.com) | 72 varieties, 20 origins, 21 brew methods |
| `whiskey` | [whiskeyfyi](https://pypi.org/project/whiskeyfyi/) | [whiskeyfyi.com](https://whiskeyfyi.com) | 80 expressions, 13 regions, 7 countries |
| `tea` | [teafyi](https://pypi.org/project/teafyi/) | [teafyi.com](https://teafyi.com) | 60 varieties, 15 teaware, 7 categories |
| `sake` | [nihonshufyi](https://pypi.org/project/nihonshufyi/) | [nihonshufyi.com](https://nihonshufyi.com) | 80 sake, 10 rice varieties, 50 breweries |

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

## What You'll Find Across the Beverage FYI Family

The Beverage FYI Family spans 7 specialized sites covering the world's major drink categories. Each site provides structured data through a consistent API pattern -- free, no authentication required, JSON with CORS enabled.

### Cocktails (CocktailFYI)

CocktailFYI covers 636 cocktail recipes across 15 families (Sour, Daisy, Fizz, Collins, Highball, Old-Fashioned, Martini, Manhattan, Negroni, Flip, Julep, Toddy, Punch, Tiki, Shooter). Each recipe includes precise measurements, calculated ABV, estimated calories, flavor profiles, required glassware, and garnish specifications. The cocktailfyi package includes a local computation engine for ABV and calorie calculations without API calls.

Learn more: [Browse 636 Cocktail Recipes](https://cocktailfyi.com/cocktail/) · [Cocktail Ingredient Guide](https://cocktailfyi.com/ingredient/)

### Wine (VinoFYI)

VinoFYI catalogs wines across 6 types (Red, White, Rose, Sparkling, Fortified, Dessert) with 777 grape varieties, wine regions organized by appellation system, wineries, and 230 expert guides. The database contains 741K records covering terroir characteristics, food pairings, and vintage information.

Learn more: [Wine Types Guide](https://vinofyi.com/type/) · [Browse 777 Grape Varieties](https://vinofyi.com/grape/)

### Beer (BeerFYI)

BeerFYI follows the BJCP (Beer Judge Certification Program) style guidelines with 112 beer styles, 82 hop varieties with alpha acid profiles, 41 malts with SRM color values, and 29 yeast strains. Each style includes defined parameters for IBU, SRM, ABV, OG/FG ranges, and recommended ingredients.

Learn more: [Browse 112 Beer Styles](https://beerfyi.com/style/) · [Hop Variety Profiles](https://beerfyi.com/hop/)

### Coffee (BrewFYI)

BrewFYI covers 72 coffee varieties with genetic lineage (Arabica, Robusta, and hybrids), 20 origin countries with altitude and harvest data, and 21 brew methods with optimal extraction parameters. Guides cover processing methods (washed, natural, honey, anaerobic), roast profiling, and SCA cupping protocols.

Learn more: [Coffee Varieties Database](https://brewfyi.com/variety/) · [21 Brew Methods](https://brewfyi.com/method/)

### Whiskey (WhiskeyFYI)

WhiskeyFYI spans 80 whiskey expressions across 7 countries (Scotland, USA, Ireland, Japan, Canada, India, Taiwan) and 13 regions. Each expression includes type classification, cask information, age statement, ABV, and detailed tasting notes. The database covers legal definitions for Scotch, Bourbon, Tennessee, Rye, and Japanese whisky.

Learn more: [Browse Whiskey Types](https://whiskeyfyi.com/type/) · [Explore 13 Whiskey Regions](https://whiskeyfyi.com/region/)

### Tea (TeaFYI)

TeaFYI covers 60 tea varieties organized by oxidation level across 7 categories (Green, White, Yellow, Oolong, Black, Pu-erh, Herbal), 15 origin countries, and 15 teaware items. Each tea includes processing method, caffeine content, optimal brewing parameters (temperature, steep time, leaf ratio), and flavor descriptors.

Learn more: [Browse Tea Categories](https://teafyi.com/category/) · [Teaware Guide](https://teafyi.com/teaware/)

### Sake (NihonshuFYI)

NihonshuFYI catalogs 80 sake expressions with the tokutei meishoshu (special designation) classification system, 10 sake-specific rice varieties with shinpaku characteristics, and 50 breweries across Japan. Each sake includes grade, polishing ratio (seimaibuai), SMV (nihonshu-do), acidity, and tasting notes.

Learn more: [Sake Grade System](https://nihonshufyi.com/grade/) · [Brewery Profiles](https://nihonshufyi.com/brewery/)

## Command-Line Interface

```bash
# List installed beverage packages
drinkfyi list

# Search via specific client
drinkfyi search cocktail margarita
drinkfyi search wine "pinot noir"
drinkfyi search beer ipa
drinkfyi search coffee espresso
drinkfyi search whiskey bourbon
drinkfyi search tea matcha
drinkfyi search sake "junmai daiginjo"
```

## API Endpoints

Each beverage site exposes a consistent set of 10 API endpoints. All are free, require no authentication, and return JSON with CORS enabled.

| Site | Base URL | Endpoints |
|------|----------|-----------|
| CocktailFYI | `https://cocktailfyi.com/api/v1/` | cocktails, ingredients, families, glossary, search, compare, random, guides |
| VinoFYI | `https://vinofyi.com/api/v1/` | wines, grapes, regions, wineries, glossary, search, compare, random, guides |
| BeerFYI | `https://beerfyi.com/api/v1/` | styles, hops, malts, yeast, glossary, search, compare, random, guides |
| BrewFYI | `https://brewfyi.com/api/v1/` | varieties, origins, methods, glossary, search, compare, random, guides |
| WhiskeyFYI | `https://whiskeyfyi.com/api/v1/` | whiskeys, distilleries, regions, glossary, search, compare, random, guides |
| TeaFYI | `https://teafyi.com/api/v1/` | teas, origins, teaware, glossary, search, compare, random, guides |
| NihonshuFYI | `https://nihonshufyi.com/api/v1/` | sake, rice, breweries, glossary, search, compare, random, guides |

All sites also serve an OpenAPI 3.1.0 specification at `/api/v1/openapi.json`.

### Example

```bash
# Search across cocktails
curl -s "https://cocktailfyi.com/api/v1/search/?q=margarita"

# Get a specific beer style
curl -s "https://beerfyi.com/api/v1/styles/new-england-ipa/"

# Compare two wines
curl -s "https://vinofyi.com/api/v1/compare/pinot-noir/cabernet-sauvignon/"
```

## Using Individual Packages

Each beverage package can be used independently:

```python
# Cocktails -- includes local computation engine
from cocktailfyi import parse_measure_ml, compute_abv
ml = parse_measure_ml("2 oz")  # 60.0

# Wine
from vinofyi.api import VinoFYI
with VinoFYI() as api:
    grapes = api.search("pinot noir")

# Beer
from beerfyi.api import BeerFYI
with BeerFYI() as api:
    styles = api.search("ipa")

# Coffee
from brewfyi.api import BrewFYI
with BrewFYI() as api:
    varieties = api.search("gesha")

# Whiskey
from whiskeyfyi.api import WhiskeyFYI
with WhiskeyFYI() as api:
    whiskeys = api.search("islay")

# Tea
from teafyi.api import TeaFYI
with TeaFYI() as api:
    teas = api.search("oolong")

# Sake
from nihonshufyi.api import NihonshuFYI
with NihonshuFYI() as api:
    sake = api.search("daiginjo")
```

## Learn More About Beverages

- **Cocktails**: [Recipes](https://cocktailfyi.com/cocktails/) | [Ingredients](https://cocktailfyi.com/ingredients/) | [Guides](https://cocktailfyi.com/guides/)
- **Wine**: [Wines](https://vinofyi.com/wines/) | [Grapes](https://vinofyi.com/grapes/) | [Regions](https://vinofyi.com/regions/) | [Guides](https://vinofyi.com/guides/)
- **Beer**: [Styles](https://beerfyi.com/styles/) | [Hops](https://beerfyi.com/hops/) | [Malts](https://beerfyi.com/malts/) | [Guides](https://beerfyi.com/guides/)
- **Coffee**: [Varieties](https://brewfyi.com/varieties/) | [Origins](https://brewfyi.com/origins/) | [Methods](https://brewfyi.com/methods/) | [Guides](https://brewfyi.com/guides/)
- **Whiskey**: [Whiskeys](https://whiskeyfyi.com/whiskeys/) | [Distilleries](https://whiskeyfyi.com/distilleries/) | [Guides](https://whiskeyfyi.com/guides/)
- **Tea**: [Teas](https://teafyi.com/teas/) | [Teaware](https://teafyi.com/teaware/) | [Guides](https://teafyi.com/guides/)
- **Sake**: [Sake](https://nihonshufyi.com/sake/) | [Rice](https://nihonshufyi.com/rice/) | [Breweries](https://nihonshufyi.com/breweries/) | [Guides](https://nihonshufyi.com/guides/)

## Beverage FYI Family

| Site | Domain | Focus |
|------|--------|-------|
| CocktailFYI | [cocktailfyi.com](https://cocktailfyi.com) | 636 cocktail recipes, ABV, calories, flavor profiles |
| VinoFYI | [vinofyi.com](https://vinofyi.com) | Wines, grapes, regions, wineries, food pairings |
| BeerFYI | [beerfyi.com](https://beerfyi.com) | 112 beer styles, hops, malts, yeast, brewing guides |
| BrewFYI | [brewfyi.com](https://brewfyi.com) | 72 coffee varieties, roasting, 21 brew methods |
| WhiskeyFYI | [whiskeyfyi.com](https://whiskeyfyi.com) | 80 whiskey expressions, distilleries, regions |
| TeaFYI | [teafyi.com](https://teafyi.com) | 60 tea varieties, teaware, brewing guides |
| NihonshuFYI | [nihonshufyi.com](https://nihonshufyi.com) | 80 sake, rice varieties, 50 breweries |

## FYIPedia Developer Tools

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| colorfyi | [PyPI](https://pypi.org/project/colorfyi/) | [npm](https://www.npmjs.com/package/@fyipedia/colorfyi) | Color conversion, WCAG contrast, harmonies -- [colorfyi.com](https://colorfyi.com) |
| emojifyi | [PyPI](https://pypi.org/project/emojifyi/) | [npm](https://www.npmjs.com/package/emojifyi) | Emoji encoding & metadata for 3,953 emojis -- [emojifyi.com](https://emojifyi.com) |
| symbolfyi | [PyPI](https://pypi.org/project/symbolfyi/) | [npm](https://www.npmjs.com/package/symbolfyi) | Symbol encoding in 11 formats -- [symbolfyi.com](https://symbolfyi.com) |
| unicodefyi | [PyPI](https://pypi.org/project/unicodefyi/) | [npm](https://www.npmjs.com/package/unicodefyi) | Unicode lookup with 17 encodings -- [unicodefyi.com](https://unicodefyi.com) |
| fontfyi | [PyPI](https://pypi.org/project/fontfyi/) | [npm](https://www.npmjs.com/package/fontfyi) | Google Fonts metadata & CSS -- [fontfyi.com](https://fontfyi.com) |
| distancefyi | [PyPI](https://pypi.org/project/distancefyi/) | [npm](https://www.npmjs.com/package/distancefyi) | Haversine distance & travel times -- [distancefyi.com](https://distancefyi.com) |
| timefyi | [PyPI](https://pypi.org/project/timefyi/) | [npm](https://www.npmjs.com/package/timefyi) | Timezone ops & business hours -- [timefyi.com](https://timefyi.com) |
| namefyi | [PyPI](https://pypi.org/project/namefyi/) | [npm](https://www.npmjs.com/package/namefyi) | Korean romanization & Five Elements -- [namefyi.com](https://namefyi.com) |
| unitfyi | [PyPI](https://pypi.org/project/unitfyi/) | [npm](https://www.npmjs.com/package/unitfyi) | Unit conversion, 220 units -- [unitfyi.com](https://unitfyi.com) |
| holidayfyi | [PyPI](https://pypi.org/project/holidayfyi/) | [npm](https://www.npmjs.com/package/holidayfyi) | Holiday dates & Easter calculation -- [holidayfyi.com](https://holidayfyi.com) |
| cocktailfyi | [PyPI](https://pypi.org/project/cocktailfyi/) | -- | Cocktail ABV, calories, flavor -- [cocktailfyi.com](https://cocktailfyi.com) |
| vinofyi | [PyPI](https://pypi.org/project/vinofyi/) | -- | Wine API client -- grapes, regions, wineries -- [vinofyi.com](https://vinofyi.com) |
| beerfyi | [PyPI](https://pypi.org/project/beerfyi/) | -- | Beer styles, hops, malts API -- [beerfyi.com](https://beerfyi.com) |
| brewfyi | [PyPI](https://pypi.org/project/brewfyi/) | -- | Coffee varieties, brew methods API -- [brewfyi.com](https://brewfyi.com) |
| whiskeyfyi | [PyPI](https://pypi.org/project/whiskeyfyi/) | -- | Whiskey expressions, distilleries API -- [whiskeyfyi.com](https://whiskeyfyi.com) |
| teafyi | [PyPI](https://pypi.org/project/teafyi/) | -- | Tea varieties, teaware API -- [teafyi.com](https://teafyi.com) |
| nihonshufyi | [PyPI](https://pypi.org/project/nihonshufyi/) | -- | Sake grades, breweries API -- [nihonshufyi.com](https://nihonshufyi.com) |
| **drinkfyi** | [PyPI](https://pypi.org/project/drinkfyi/) | -- | **Unified beverage hub -- 7 sites -- [fyipedia.com](https://fyipedia.com)** |
| fyipedia | [PyPI](https://pypi.org/project/fyipedia/) | -- | Unified CLI: `fyi color info FF6B35` -- [fyipedia.com](https://fyipedia.com) |
| fyipedia-mcp | [PyPI](https://pypi.org/project/fyipedia-mcp/) | -- | Unified MCP hub for AI assistants -- [fyipedia.com](https://fyipedia.com) |

## License

MIT
