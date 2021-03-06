# -*- coding: utf-8 -*-
import re

import pytest

from mimesis import Code
from mimesis.data import LOCALE_CODES
from mimesis.enums import EANFormat, ISBNFormat
from mimesis.exceptions import NonEnumerableError

from . import _patterns as p


class TestCode(object):
    @pytest.fixture
    def code(self):
        return Code()

    def test_str(self, code):
        assert re.match(p.STR_REGEX, str(code))

    @pytest.mark.parametrize(
        'fmt, length', [
            (EANFormat.EAN8, 8),
            (EANFormat.EAN13, 13),
        ],
    )
    def test_ean(self, code, fmt, length):
        result = code.ean(fmt=fmt)
        assert len(result) == length

    def test_ean_non_enum(self, code):
        with pytest.raises(NonEnumerableError):
            code.ean(fmt='nil')

    def test_imei(self, code):
        result = code.imei()
        assert len(result) <= 15

    def test_pin(self, code):
        result = code.pin()
        assert len(result) == 4

    def test_issn(self, code):
        result = code.issn()
        assert len(result) == 9

    def test_locale_code(self, code):
        result = code.locale_code()
        assert result in LOCALE_CODES

    @pytest.mark.parametrize(
        'fmt, length', [
            (ISBNFormat.ISBN10, 10),
            (ISBNFormat.ISBN13, 13),
        ],
    )
    def test_isbn(self, code, fmt, length):
        result = code.isbn(fmt=fmt)
        assert result is not None
        assert len(result) >= length

    def test_isbn_non_enum(self, code):
        with pytest.raises(NonEnumerableError):
            code.isbn(fmt='nil')


class TestSeededCode(object):
    TIMES = 5

    @pytest.fixture
    def _codes(self, seed):
        return Code(seed=seed), Code(seed=seed)

    def test_ean(self, _codes):
        c1, c2 = _codes
        for _ in range(self.TIMES):
            assert c1.ean() == c2.ean()
            assert c1.ean(fmt=EANFormat.EAN13) == c2.ean(fmt=EANFormat.EAN13)

    def test_imei(self, _codes):
        c1, c2 = _codes
        for _ in range(self.TIMES):
            assert c1.imei() == c2.imei()

    def test_pin(self, _codes):
        c1, c2 = _codes
        for _ in range(self.TIMES):
            assert c1.pin() == c2.pin()
            assert c1.pin(mask='#_#_#') == c2.pin(mask='#_#_#')

    def test_issn(self, _codes):
        c1, c2 = _codes
        for _ in range(self.TIMES):
            assert c1.issn() == c2.issn()
            assert c1.issn(mask='#_#_#') == c2.issn(mask='#_#_#')

    def test_locale_code(self, _codes):
        c1, c2 = _codes
        for _ in range(self.TIMES):
            assert c1.locale_code() == c2.locale_code()

    def test_isbn(self, _codes):
        c1, c2 = _codes
        for _ in range(self.TIMES):
            assert c1.isbn() == c2.isbn()
            assert c1.isbn(fmt=ISBNFormat.ISBN13) == \
                c2.isbn(fmt=ISBNFormat.ISBN13)
