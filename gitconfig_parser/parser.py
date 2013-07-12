""":mod:`gitconfig_parser.parser` -- Parser implementation
"""

from pyparsing import (
    OneOrMore, restOfLine, Group, ZeroOrMore,
    CharsNotIn, Suppress, Word, alphanums, Literal, pythonStyleComment)


def build_parser():
    key = Word(alphanums).setResultsName('key')
    value = restOfLine.setParseAction(
        lambda string, location, tokens: tokens[0].strip()
    ).setResultsName('value')
    property_ = Group(key + Suppress(Literal('=')) + value)
    properties = Group(OneOrMore(property_)).setResultsName('properties')
    section_name = (Suppress('[') + OneOrMore(CharsNotIn(']')) +
                    Suppress(']')).setResultsName('section')
    section = Group(section_name + properties)
    ini_file = ZeroOrMore(section).setResultsName('sections')
    ini_file.ignore(pythonStyleComment)
    return ini_file


def parse_file(file_):
    parser = build_parser()
    return parser.parseWithTabs().parseFile(file_, parseAll=True)
