from configparser_rb import __version__
from os import system

def release():
    print("""Nueva versión:
  * Cambiar la version en pyproject.toml
  * Cambiar la versión y la fecha en __init__.py
  * Ejecutar otra vez poe release
  * git checkout -b configparser_rb-{0}
  * poe translate
  * linguist
  * poe translate
  * poe test
  * poe jupyter
  * git commit -a -m 'configparser_rb-{0}'
  * git push
  * Hacer un pull request con los cambios a main
  * Hacer un nuevo tag en GitHub
  * git checkout main
  * git pull
  * poetry build
  * poetry publish
  * Crea un nuevo ebuild de configparser_rb en Gentoo con la nueva versión
  * Subelo al repositorio myportage

""".format(__version__))
    
def coverage():
    system("coverage run  -m pytest && coverage report && coverage html")


def translate():
    #es
    system("xgettext -L Python --no-wrap --no-location --from-code='UTF-8' -o configparser_rb/locale/configparser_rb.pot configparser_rb/*.py")
    system("msgmerge -N --no-wrap -U configparser_rb/locale/es.po configparser_rb/locale/configparser_rb.pot")
    system("msgfmt -cv -o configparser_rb/locale/es/LC_MESSAGES/configparser_rb.mo configparser_rb/locale/es.po")
    
    
