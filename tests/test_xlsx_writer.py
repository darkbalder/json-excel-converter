from json_excel_converter import Converter
from json_excel_converter.xlsx import Writer
from json_excel_converter.xlsx.formats import UnderlinedHeaderFormat, ColumnBorderFormat, BoldHeaderFormat, \
    CenteredHeaderFormat, HeaderFormat
from json_excel_converter.linearize import Value


def test_writer():
    w = Writer('/tmp/test.xlsx', formats=(CenteredHeaderFormat, BoldHeaderFormat, UnderlinedHeaderFormat,))
    w.start()
    w.write_header([
        Value('a', 1),
        Value('b', 2, has_children=True),
        Value('c', 1)
    ])
    w.write_header([
        Value(None, 1),
        Value('b1', 1),
        Value('b2', 1),
        Value(None, 1)
    ])
    w.write_row([Value(1), Value(2), Value(3), Value(4)])
    w.write_row([Value('1'), Value('2'), Value('3'), Value('4')])
    w.finish()


def test_writer_2():
    w = Writer('/tmp/test2.xlsx',
               formats=(CenteredHeaderFormat, BoldHeaderFormat, UnderlinedHeaderFormat, ColumnBorderFormat,))
    w.start()
    w.write_header([
        Value('a', 1),
        Value('b', 2, has_children=True),
        Value('c', 1)
    ])
    w.write_header([
        Value(None, 1),
        Value('b1', 1),
        Value('b2', 1),
        Value(None, 1)
    ])
    w.write_row([Value(1), Value(2), Value(3), Value(4)])
    w.write_row([Value('1'), Value('2'), Value('3'), Value('4')])
    w.finish()


def test_red_header():
    data = [
        {'a': 'Hello'},
        {'a': 'World'}
    ]

    w = Writer('/tmp/test3.xlsx',
               formats=(CenteredHeaderFormat, BoldHeaderFormat, UnderlinedHeaderFormat,
                        HeaderFormat({
                            'font_color': 'red'
                        })))

    conv = Converter()
    conv.convert(data, w)