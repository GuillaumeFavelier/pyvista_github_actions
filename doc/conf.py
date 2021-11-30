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
import gc
import os
import time
import pyvista
import mne
from mne.utils import _assert_no_instances
from mne.viz import Brain
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


class Resetter(object):
    """Simple class to make the str(obj) static for Sphinx build env hash."""

    def __init__(self):
        self.t0 = time.time()

    def __repr__(self):
        return f'<{self.__class__.__name__}>'

    def __call__(self, gallery_conf, fname):
        import matplotlib.pyplot as plt
        try:
            from pyvista import Plotter  # noqa
        except ImportError:
            Plotter = None  # noqa
        try:
            from pyvistaqt import BackgroundPlotter  # noqa
        except ImportError:
            BackgroundPlotter = None  # noqa
        try:
            from vtk import vtkPolyData  # noqa
        except ImportError:
            vtkPolyData = None  # noqa
        from mne.viz.backends.renderer import backend
        _Renderer = backend._Renderer if backend is not None else None
        # in case users have interactive mode turned on in matplotlibrc,
        # turn it off here (otherwise the build can be very slow)
        plt.ioff()
        plt.rcParams['animation.embed_limit'] = 30.
        gc.collect()
        when = 'mne/conf.py:Resetter.__call__'
        _assert_no_instances(Brain, when)  # calls gc.collect()
        if Plotter is not None:
            _assert_no_instances(Plotter, when)
        if BackgroundPlotter is not None:
            _assert_no_instances(BackgroundPlotter, when)
        if vtkPolyData is not None:
            _assert_no_instances(vtkPolyData, when)
        _assert_no_instances(_Renderer, when)


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

scrapers = ('matplotlib',)
scrapers += (
    mne.gui._LocateScraper(),
    mne.viz._brain._BrainScraper(),
    'pyvista',
)
report_scraper = mne.report._ReportScraper()
scrapers += (report_scraper,)


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
    'reset_modules': ('matplotlib', Resetter()),
}
