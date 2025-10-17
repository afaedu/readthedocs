import os

project = 'My Static HTML Site'
html_title = "My Static HTML Site"
html_theme = 'alabaster'

html_static_path = ['_static']

html_additional_pages = {
    'index': 'index.html',
    'about': 'about.html',
}

source_suffix = []
master_doc = 'index'
exclude_patterns = []
