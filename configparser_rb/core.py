from configparser import ConfigParser
from decimal import Decimal
from os import path, makedirs
from configparser_rb import _
from configparser_rb.rotatedbase64 import string_to_rotatedbase64, rotatedbase64_to_string
from pydicts import casts

def string2list_of_strings(s, separator=", "):
    arr=[]
    if s!="":
        arrs=s.split(separator)
        for a in arrs:
            arr.append(a[1:-1])
    return arr

def string2list_of_integers(s, separator=", "):
    arr=[]
    if s!="":
        arrs=s.split(separator)
        for a in arrs:
            arr.append(int(a))
    return arr

def list2string(lista):
        """Covierte lista a string"""
        if  len(lista)==0:
            return ""
        if str(lista[0].__class__) in ["<class 'int'>", "<class 'float'>"]:
            resultado=""
            for l in lista:
                resultado=resultado+ str(l) + ", "
            return resultado[:-2]
        elif str(lista[0].__class__) in ["<class 'str'>",]:
            resultado=""
            for l in lista:
                resultado=resultado+ "'" + str(l) + "', "
            return resultado[:-2]

class ConfigParserRB:
    def __init__(self, filename):
        self.filename=filename
        self.config=ConfigParser()
        if path.exists(self.filename):
            self.config.read(self.filename)
        else:
            print("Creating a new configuration file: {}".format(self.filename))

    def cset(self, section, option, value):
        self.set(section,option, string_to_rotatedbase64(value))

    def cget(self, section, option, default=None):
        return rotatedbase64_to_string(self.get(section,option,default))

    def get(self, section, option, default=None):
        if self.config.has_option(section, option)==True:
            return self.config.get(section, option)
        else:
            self.set(section, option, default)
            return self.get(section, option)

    def getDecimal(self, section,option, default=None):
        try:
            value=self.get(section, option, default)
            return Decimal(value)
        except:
            print("I couldn't convert to Decimal {} ({})".format(value, value.__class__))

    def getFloat(self, section,option, default=None):
        try:
            value=self.get(section, option, default)
            return float(value)
        except:
            print("I couldn't convert to float {} ({})".format(value, value.__class__))

    def getInteger(self, section,option, default=None):
        try:
            value=self.get(section, option, default)
            return int(value)
        except:
            print("I couldn't convert to int {} ({})".format(value, value.__class__))

    def getBoolean(self, section,option, default=None):
        try:
            value=self.get(section, option, default)
            return casts.str2bool(value)
        except:
            print("I couldn't convert to boolean {} ({})".format(value, value.__class__))

    ## Example: self.value_datetime_naive("Version", "197001010000", "%Y%m%d%H%M")
    def getDatetimeNaive(self, section, option, default=None, format="%Y%m%d%H%M"):
        try:
            value=self.get(section, option, default)
            return casts.str2dtnaive(value, format)
        except:
            print("I couldn't convert to datetime naive {} ({})".format(value, value.__class__))

    def getList(self, section, option, default=[]):
        try:
            value=self.get(section, option, default)
            return string2list_of_strings(value)
        except:
            print("I couldn't convert to list of strings {} ({})".format(value, value.__class__))

    def getListOfIntegers(self, section, option, default=[]):
        try:
            value=self.get(section, option, default)
            return string2list_of_integers(value)
        except:
            print("I couldn't convert to list of integers {} ({})".format(value, value.__class__))

    def set(self, section, option, value):
        if isinstance(value, list):
            value=list2string(value)
        if section not in self.config:
            self.config.add_section(section)
            self.config[section]={}
        self.config.set(section, option, str(value))

    def save(self):
        dirname=path.dirname(self.filename)
        if dirname != "":
            makedirs(dirname, exist_ok=True)
        with open(self.filename, 'w') as f:
            self.config.write(f)



def set():
    from argparse import ArgumentParser

    parser=ArgumentParser()
    parser.description="Configura las keys en ficheros de ConfigParserRB"
    parser.add_argument("--file", required=True)
    parser.add_argument("--section", required=True)
    parser.add_argument("--key", required=True)
    parser.add_argument("--value", required=True)
    parser.add_argument("--secure", help="Encode setting", action="store_true", default=False)
    args=parser.parse_args()

    config=ConfigParserRB(args.file)
    if args.secure:
        config.cset(args.section, args.key, args.value)
    else:
        config.set(args.section, args.key, args.value)
    config.save()

def get():
    from argparse import ArgumentParser

    parser=ArgumentParser()
    parser.description="Configura las keys en ficheros de ConfigParserRB"
    parser.add_argument("--file", required=True)
    parser.add_argument("--section", required=True)
    parser.add_argument("--key", required=True)
    parser.add_argument("--secure", help="Encode setting", action="store_true", default=False)
    args=parser.parse_args()

    config=ConfigParserRB(args.file)
    if args.secure:
        print(config.cget(args.section, args.key))
    else:
        print(config.get(args.section, args.key))