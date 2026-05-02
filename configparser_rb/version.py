from datetime import datetime
from importlib.resources import files
from gettext import translation

__version__="1.1.0"
__versiondatetime__= datetime(2026, 5, 2, 19, 7)
__versiondate__=__versiondatetime__.date()


try:
    t=translation('configparser_rb', files("configparser_rb") / 'locale')
    _=t.gettext
except:
    _=str