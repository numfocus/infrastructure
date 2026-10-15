# Copyright 2020-2026 NumFOCUS

from datetime import datetime

author = "NumFOCUS Infrastructure Committee"
project = "NumFOCUS Infrastructure Committee"
release = ""
copyright = f"{datetime.now().year}, {author}"  # NOQA: A001 DTZ005
html_theme = "pydata_sphinx_theme"


html_logo = "_static/NumFocus_LRG.png"
# Official NumFOCUS favicon: https://numfocus.org/favicon.ico
html_favicon = "_static/numfocus.ico"
templates_path = ["_templates"]
html_static_path = ["_static"]
html_css_files = ["style.css"]
html_sidebars = {"**": ["navigation.html"]}
html_theme_options = {
    "navbar_center": [],
    "footer_start": ["copyright"],
    "footer_end": [],
    "logo": {
        "text": "Infrastructure",
        "image_light": "_static/NumFocus_LRG.png",  # For light mode
        "image_dark": "_static/NumFocus_LRG.png",  # For dark mode
    },
}
