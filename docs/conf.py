"""Sphinx configuration."""
project = "Datapy"
author = "TradingPy"
copyright = "2022, TradingPy"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
