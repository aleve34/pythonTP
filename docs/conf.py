# -- Project information -----------------------------------------------------

project = 'Sum Project'  # Name of your project
author = 'Nerine'     # Your name or team name
release = '1.0'          # Version of your project

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',  # Automatically generate documentation from docstrings
    'sphinx.ext.viewcode',  # Add links to the source code in the documentation
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'  # You can change this theme to any available theme
html_static_path = ['_static']
