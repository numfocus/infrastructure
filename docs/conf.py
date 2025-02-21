from datetime import datetime

author = "NumFOCUS Infrastructure Committee"
project = "NumFOCUS Infrastructure Committee"
release = ""
copyright = f"{datetime.now().year}, {author}"  # NOQA: A001 DTZ005
html_theme = "pydata_sphinx_theme"


html_logo = "_static/NumFocus_LRG.png"
html_favicon = "_static/NumFocus_LRG.png"
html_theme_options = {
    "logo": {
        "text": "Infrastructure",
        "image_light": "_static/NumFocus_LRG.png",  # For light mode
        "image_dark": "_static/NumFocus_LRG.png",  # For dark mode
    },
}
