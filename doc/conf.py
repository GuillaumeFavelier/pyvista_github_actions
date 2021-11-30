# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import pyvista
import mne
pyvista.OFF_SCREEN = True
pyvista.BUILDING_GALLERY = True


# -- Project information -----------------------------------------------------

project = 'test'
copyright = '2021, test'
author = 'test'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

master_doc = 'index'
source_suffix = ['.rst', '.md']

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx_gallery.gen_gallery',
    'numpydoc',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'bootstrap'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'navbar_sidebarrel': False,
    'navbar_pagenav': False,
    'source_link_position': "",
    'navbar_links': [
        ("Examples", "auto_examples/index"),
    ],
    'bootswatch_theme': "flatly",
    'bootstrap_version': "3",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

scrapers = ('matplotlib', 'pyvista')
scrapers += mne.viz._brain._BrainScraper


examples_dirs = ['../examples']
gallery_dirs = ['auto_examples']
sphinx_gallery_conf = {
    'examples_dirs': examples_dirs,
    'gallery_dirs': gallery_dirs,
    'plot_gallery': 'True',
    'backreferences_dir': os.path.join('generated'),
    'abort_on_example_error': False,
    'image_scrapers': scrapers,
    'show_memory': True,
}
