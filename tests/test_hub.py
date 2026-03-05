"""Tests for drinkfyi hub package."""

from drinkfyi import BEVERAGE_PACKAGES, available_clients, get_client


class TestBeveragePackages:
    def test_all_seven_types(self) -> None:
        assert len(BEVERAGE_PACKAGES) == 7

    def test_expected_types(self) -> None:
        expected = {"cocktail", "wine", "beer", "whiskey", "tea", "coffee", "sake"}
        assert set(BEVERAGE_PACKAGES.keys()) == expected

    def test_each_entry_has_module_and_class(self) -> None:
        for bev_type, (module_name, class_name) in BEVERAGE_PACKAGES.items():
            assert "." in module_name, f"{bev_type} module should be dotted path"
            assert class_name[0].isupper(), f"{bev_type} class should be PascalCase"


class TestAvailableClients:
    def test_returns_list(self) -> None:
        result = available_clients()
        assert isinstance(result, list)

    def test_installed_packages_present(self) -> None:
        # All 7 should be installed in dev environment
        result = available_clients()
        assert "cocktail" in result
        assert "wine" in result
        assert "beer" in result


class TestGetClient:
    def test_get_cocktail_client(self) -> None:
        client = get_client("cocktail")
        assert client is not None
        assert hasattr(client, "search")
        assert hasattr(client, "close")
        client.close()

    def test_get_wine_client(self) -> None:
        client = get_client("wine")
        assert client is not None
        assert hasattr(client, "search")
        client.close()

    def test_unknown_type_raises(self) -> None:
        import pytest

        with pytest.raises(ValueError, match="Unknown beverage type"):
            get_client("juice")

    def test_version(self) -> None:
        from drinkfyi import __version__

        assert __version__ == "0.1.0"
