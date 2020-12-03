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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = u'SymbiFlow examples'
authors = u'SymbiFlow'
copyright = authors + u', 2020'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_tabs.tabs',
    'sphinxcontrib.jinja',
]

import os
from collections import OrderedDict
from tuttest import get_snippets

jinja_contexts = {}
top_dir = os.path.join(os.path.dirname(__file__), '..')
full_name_lut = {
    'a35t': 'Arty 35T',
    'a100t': 'Arty 100T',
    'basys3': 'Basys 3',
    'eos_s3': 'EOS S3',
}

# top-level examples directories
families = ('xc7', 'eos-s3')
for family in families:
    jinja_contexts[family] = {}

    # register examples
    examples = os.scandir(os.path.join(top_dir, family))
    for example in examples:
        if example.is_dir():
            entry = jinja_contexts[family][example.name] = {}

            # get path to example's README
            example_readme_path = [top_dir, family, example, 'README.rst']
            example_readme = os.path.join(*example_readme_path)

            # skip if file does not exist
            if not os.path.isfile(example_readme):
                continue

            snippets = get_snippets(example_readme)

            for snippet in snippets:
                print(snippet)
                variant = (snippet.split('-')[1])
                entry[variant] = {
                    'is_build': variant in full_name_lut,
                    'name': full_name_lut.get(variant, variant),
                    'code': snippets[snippet].text.split('\n'),
                }


print(jinja_contexts)

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_show_sourcelink = True
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

html_theme = 'sphinx_material'
html_theme_options = {
    'nav_title': project,
    'color_primary': 'deep-purple',
    'color_accent': 'purple',
    'repo_name': "antmicro/symbiflow-examples",
    'repo_url': 'https://github.com/antmicro/symbiflow-examples',
    'globaltoc_depth': 2,
    'globaltoc_collapse': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
