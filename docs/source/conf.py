import sys
import pathlib


sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))

# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Tools Collection'
copyright = '2023 Dominik Fuchs'
author = 'Dominik Fuchs'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',

    'autoapi.extension',
    'sphinxcontrib.openapi',
]

autoapi_type = 'python'
autoapi_dirs = ['../../Tools', '../../Server', '../../GUI']


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
