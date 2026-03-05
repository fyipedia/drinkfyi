"""Command-line interface for drinkfyi — unified beverage hub.

Requires the ``cli`` extra: ``pip install drinkfyi[cli]``

Usage::

    drinkfyi list                    # List installed beverage packages
    drinkfyi search cocktail margarita   # Search via specific client
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    name="drinkfyi",
    help="Unified beverage knowledge hub — cocktails, wine, beer, whiskey, tea, coffee, sake.",
    no_args_is_help=True,
)
console = Console()


@app.command("list")
def list_clients() -> None:
    """List installed beverage packages and their status."""
    from drinkfyi import BEVERAGE_PACKAGES, available_clients

    installed = available_clients()

    table = Table(title="DrinkFYI — Installed Beverage Packages")
    table.add_column("Type", style="cyan", no_wrap=True)
    table.add_column("Package")
    table.add_column("Status")

    for bev_type, (module_name, _class_name) in BEVERAGE_PACKAGES.items():
        pkg = module_name.split(".")[0]
        status = "[green]installed[/green]" if bev_type in installed else "[dim]not installed[/dim]"
        table.add_row(bev_type, pkg, status)

    console.print(table)
    console.print(f"\n[dim]{len(installed)}/{len(BEVERAGE_PACKAGES)} packages installed[/dim]")


@app.command()
def search(
    beverage_type: str = typer.Argument(
        help="Beverage type (cocktail, wine, beer, whiskey, tea, coffee, sake)"
    ),
    query: str = typer.Argument(help="Search query"),
) -> None:
    """Search across a specific beverage knowledge base."""
    from drinkfyi import BEVERAGE_PACKAGES, get_client

    if beverage_type not in BEVERAGE_PACKAGES:
        console.print(
            f"[red]Unknown type:[/red] {beverage_type}. Choose from: {', '.join(BEVERAGE_PACKAGES)}"
        )
        raise typer.Exit(1)

    try:
        client = get_client(beverage_type)
    except ImportError:
        pkg = BEVERAGE_PACKAGES[beverage_type][0].split(".")[0]
        console.print(f"[red]Package not installed:[/red] pip install {pkg}")
        raise typer.Exit(1)  # noqa: B904

    try:
        result = client.search(query)
        console.print_json(data=result)
    finally:
        if hasattr(client, "close"):
            client.close()


if __name__ == "__main__":
    app()
