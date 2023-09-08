# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Pathfinder Project Україна'
copyright = '2023, Deniz Köse'
author = 'Deniz Köse'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_immaterial"
]

templates_path = ['_templates']
exclude_patterns = []

language = 'uk'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_favicon = '_static/favicon.png'
html_theme = "sphinx_immaterial"
html_static_path = ['_static']
html_title = f'{project}'
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
        "edit": "material/file-edit-outline",
    },
    "repo_url": "https://github.com/DenizKose/pfproject",
    "repo_name": "pfproject",
    "edit_uri": "blob/main/docs",
    "globaltoc_collapse": True,
    "features": [
        "navigation.expand",
        # "navigation.tabs",
        # "toc.integrate",
        "navigation.sections",
        # "navigation.instant",
        # "header.autohide",
        "navigation.top",
        # "navigation.tracking",
        # "search.highlight",
        "search.share",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "announce.dismiss",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "light-green",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "deep-orange",
            "accent": "lime",
            "toggle": {
                "icon": "material/lightbulb",
                "name": "Switch to light mode",
            },
        },
    ],
    "toc_title_is_page_title": True,
    # BEGIN: social icons
    "social": [
        {
            "icon": "fontawesome/brands/github",
            "link": "https://github.com/DenizKose/pfproject",
            "name": "Source on github.com",
        },
        {
            "icon": "fontawesome/brands/wikipedia-w",
            "link": "https://golarion.fandom.com/uk/wiki/Вікі_Golarion",
        },
    ],
    # END: social icons
}