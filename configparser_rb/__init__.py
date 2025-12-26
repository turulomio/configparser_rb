from datetime import datetime
from importlib.resources import files
from gettext import translation

__version__="1.0.0"
__versiondatetime__= datetime(2025, 12, 26, 20, 41)
__versiondate__=__versiondatetime__.date()


try:
    t=translation('configparser_rb', files("configparser_rb") / 'locale')
    _=t.gettext
except:
    _=str