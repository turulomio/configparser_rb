from importlib.resources import files
from gettext import translation

try:
    t=translation('configparser_rb', files("configparser_rb") / 'locale')
    _=t.gettext
except:
    _=str