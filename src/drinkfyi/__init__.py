"""drinkfyi — Unified beverage knowledge hub.

Access cocktails, wine, beer, whiskey, tea, coffee, and sake
through a single package. Install only what you need::

    pip install drinkfyi[cocktail]        # Cocktail engine
    pip install drinkfyi[wine,beer]       # Wine + beer clients
    pip install drinkfyi[all]             # Everything

Usage::

    from drinkfyi import available_clients
    print(available_clients())  # ['cocktailfyi', 'vinofyi', ...]
"""

from __future__ import annotations

from typing import Any

__version__ = "0.1.0"

# Map of beverage type → (package_name, client_class_name)
BEVERAGE_PACKAGES: dict[str, tuple[str, str]] = {
    "cocktail": ("cocktailfyi.api", "CocktailFYI"),
    "wine": ("vinofyi.api", "VinoFYI"),
    "beer": ("beerfyi.api", "BeerFYI"),
    "whiskey": ("whiskeyfyi.api", "WhiskeyFYI"),
    "tea": ("teafyi.api", "TeaFYI"),
    "coffee": ("brewfyi.api", "BrewFYI"),
    "sake": ("nihonshufyi.api", "NihonshuFYI"),
}


def available_clients() -> list[str]:
    """Return list of installed beverage package names."""
    import importlib

    installed: list[str] = []
    for bev_type, (module_name, _) in BEVERAGE_PACKAGES.items():
        try:
            importlib.import_module(module_name.split(".")[0])
            installed.append(bev_type)
        except ImportError:
            pass
    return installed


def get_client(beverage_type: str) -> Any:
    """Get an API client instance for a beverage type.

    Args:
        beverage_type: One of 'cocktail', 'wine', 'beer', 'whiskey',
                       'tea', 'coffee', 'sake'.

    Returns:
        An API client instance (e.g. CocktailFYI, VinoFYI, etc.).

    Raises:
        ValueError: If beverage_type is not recognized.
        ImportError: If the required package is not installed.
    """
    import importlib

    if beverage_type not in BEVERAGE_PACKAGES:
        msg = f"Unknown beverage type: {beverage_type!r}. Choose from: {list(BEVERAGE_PACKAGES)}"
        raise ValueError(msg)

    module_name, class_name = BEVERAGE_PACKAGES[beverage_type]
    module = importlib.import_module(module_name)
    client_class = getattr(module, class_name)
    return client_class()


__all__ = [
    "BEVERAGE_PACKAGES",
    "available_clients",
    "get_client",
]
