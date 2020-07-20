"""
numerical_types.py:

A file that contains the definitions for all the integer types provided as part of F prime.  F prime supports integers
that map to stdint.h integer sizes, that is, 8-bit, 16-bit, 32-bit, and 64-bit signed and unsigned integers.

@author mstarch
"""
import re
import abc

from .type_base import ValueType
from .type_exceptions import DeserializeException, NotInitializedException, TypeMismatchException, TypeRangeException

BITS_RE = re.compile(r"[IUF](\d\d?)")

class NumericalType(ValueType, abc.ABC):
    """ Numerical types that can be serialized using struct and are of some power of 2 byte width """

    @classmethod
    def __get_bits(cls):
        """ Gets the integer bits of a given type """
        match = BITS_RE.match(cls)
        assert match, "Type {} does not follow format I#Type nor U#Type required of integer types".format(cls)
        return int(match.group(1))

    @classmethod
    def getSize(cls):
        """ Gets the size of the integer based on the size specified in the class name """
        return int(cls.__get_bits()/8)


class IntegerType(NumericalType, abc.ABC):
    """ Base class thar represents all integer common functions """

    def validate(self, val):
        """ Validates the given integer. """
        if not isinstance(val, int):
            raise TypeMismatchException(int, type(val))
        min_val = 0
        max_val = 1 << self.__get_integer_bits()
        if self.startswith("I"):
            min_val -= int(max_val/2)
            max_val -= int(max_val/2)
        if val < min_val or val >= max_val:
            raise TypeRangeException(val)


class FloatType(NumericalType, abc.ABC):
    """ Base class thar represents all float common functions """

    def validate(self, val):
        """ Validates the given integer. """
        if not isinstance(val, float):
            raise TypeMismatchException(float, type(val))


class I8Type(IntegerType):
    """ Single byte integer type. Represents C chars """

    @staticmethod
    def get_serialize_format():
        """ Allows serialization using struct """
        return "b"


class I16Type(IntegerType):
    """ Double byte integer type. Represents C shorts """
    @staticmethod
    def get_serialize_format():
        """ Allows serialization using struct """
        return ">h"

class I32Type(IntegerType):
    """ Four byte integer type. Represents C int32_t, """
    @staticmethod
    def get_serialize_format():
        """ Allows serialization using struct """
        return ">i"

class I64Type(IntegerType):
    """ Eight byte integer type. Represents C int64_t, """
    @staticmethod
    def get_serialize_format():
        """ Allows serialization using struct """
        return ">q"

class U8Type(IntegerType):
    """ Single byte integer type. Represents C chars """
    @staticmethod
    def get_serialize_format():
        """ Allows serialization using struct """
        return "B"

class U16Type(IntegerType):
    """ Double byte integer type. Represents C shorts """
    @staticmethod
    def get_serialize_format():
        """ Allows serialization using struct """
        return ">H"

class U32Type(IntegerType):
    """ Four byte integer type. Represents C unt32_t, """
    @staticmethod
    def get_serialize_format():
        """ Allows serialization using struct """
        return ">I"

class U64Type(IntegerType):
    """ Eight byte integer type. Represents C unt64_t, """
    @staticmethod
    def get_serialize_format():
        """ Allows serialization using struct """
        return ">Q"


class F32Type(FloatType):
    """ Eight byte integer type. Represents C unt64_t, """
    @staticmethod
    def get_serialize_format():
        """ Allows serialization using struct """
        return ">f"


class F64Type(IntegerType):
    """ Eight byte integer type. Represents C unt64_t, """
    @staticmethod
    def get_serialize_format():
        """ Allows serialization using struct """
        return ">d"
