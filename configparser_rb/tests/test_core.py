from configparser_rb.core import ConfigParserRB
from decimal import Decimal
from tempfile import TemporaryDirectory

def test_ConfigParserRB():
    with TemporaryDirectory() as tempdir:
        config=ConfigParserRB(f"{tempdir}/config.ini")
        config.set("Features", "string", "Hi")
        config.set("Features", "boolean", True)
        config.set("Features", "integer", 1)
        config.set("Features", "float", 1.1)
        config.set("Features", "list of strings", ["a", "b"])
        config.set("Features", "list of integers", [1, 2])
        config.set("Features", "decimal", "12.234")
        config.cset("Features", "cstring", "Hi")
        config.save()

        config=ConfigParserRB(f"{tempdir}/config.ini")
        assert config.cget("Features", "cstring") == "Hi"
        assert config.get("Features", "string") == "Hi"
        assert config.getBoolean("Features", "boolean") == True
        assert config.getInteger("Features", "integer") == 1
        assert config.getFloat("Features", "float") == 1.1
        assert config.getListOfIntegers("Features", "list of integers") == [1, 2]
        assert config.getList("Features", "list of strings") == ["a", "b"]
        assert config.getDecimal("Features", "decimal") == Decimal("12.234")