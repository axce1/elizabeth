# -*- coding: utf-8 -*-

import re

import pytest

from mimesis import Generic

from .test_providers import _patterns as p


class TestGeneric(object):
    def test_str(self, generic):
        assert re.match(p.STR_REGEX, str(generic))

    def test_base_personal(self, generic):
        result = generic.personal.username()
        assert result is not None

    def test_base_text(self, generic):
        result = generic.text.words()
        assert result is not None

    def test_base_payment(self, generic):
        result = generic.payment.bitcoin_address()
        assert result is not None

    def test_base_address(self, generic):
        result = generic.address.address()
        assert result is not None

    def test_base_food(self, generic):
        result = generic.food.fruit()
        assert result is not None

    def test_base_science(self, generic):
        result = generic.science.scientific_article()
        assert result is not None

    def test_base_business(self, generic):
        result = generic.business.copyright()
        assert result is not None

    def test_base_unit_system(self, generic):
        result = generic.unit_system.unit()
        assert result is not None

    def test_base_code(self, generic):
        result = generic.code.isbn()
        assert result is not None

    def test_bad_argument(self, generic):
        with pytest.raises(AttributeError):
            _ = generic.bad_argument  # noqa

    def test_add_providers(self, generic):
        class Provider1(object):
            @staticmethod
            def one():
                return 1

        class Provider2(object):
            class Meta:
                name = 'custom_provider'

            @staticmethod
            def two():
                return 2

        class Provider3(object):
            @staticmethod
            def three():
                return 3

        generic.add_providers(Provider1, Provider2, Provider3)
        assert generic.provider1.one() == 1
        assert generic.custom_provider.two() == 2
        assert generic.provider3.three() == 3

        with pytest.raises(TypeError):
            generic.add_providers(True)

        class UnnamedProvider(object):
            @staticmethod
            def nothing():
                return None

        generic.add_provider(UnnamedProvider)
        assert generic.unnamedprovider.nothing() is None


class TestSeededGeneric(object):
    TIMES = 5

    @pytest.fixture
    def _generics(self, seed):
        return Generic(seed=seed), Generic(seed=seed)

    def test_generic_address(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.address.street_number() == g2.address.street_number()
            assert g1.address.street_name() == g2.address.street_name()

    def test_generic_business(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.business.company() == g2.business.company()
            assert g1.business.copyright() == g2.business.copyright()

    def test_generic_clothing_sizes(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.clothing_sizes.international_size() == \
                g2.clothing_sizes.international_size()
            assert g1.clothing_sizes.european_size() == \
                g2.clothing_sizes.european_size()

    def test_generic_code(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.code.locale_code() == g2.code.locale_code()
            assert g1.code.issn() == g2.code.issn()

    def test_generic_cryptographic(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.cryptographic.uuid() == g2.cryptographic.uuid()
            assert g1.cryptographic.hash() == g2.cryptographic.hash()

    def test_generic_datetime(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.datetime.week_date() == g2.datetime.week_date()
            assert g1.datetime.day_of_week() == g2.datetime.day_of_week()

    def test_generic_development(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.development.container() == g2.development.container()
            assert g1.development.version_control_system() == \
                g2.development.version_control_system()

    def test_generic_file(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.file.size() == g2.file.size()
            assert g1.file.file_name() == g2.file.file_name()

    def test_generic_food(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.food.dish() == g2.food.dish()
            assert g1.food.spices() == g2.food.spices()

    def test_generic_games(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.games.gaming_platform() == g2.games.gaming_platform()
            assert g1.games.score() == g2.games.score()

    def test_generic_hardware(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.hardware.screen_size() == g2.hardware.screen_size()
            assert g1.hardware.cpu() == g2.hardware.cpu()

    def test_generic_internet(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.internet.content_type() == g2.internet.content_type()
            assert g1.internet.http_status_message() == \
                g2.internet.http_status_message()

    def test_generic_numbers(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.numbers.integers() == g2.numbers.integers()
            assert g1.numbers.digit() == g2.numbers.digit()

    def test_generic_path(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.path.root() == g2.path.root()
            assert g1.path.home() == g2.path.home()

    def test_generic_payment(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.payment.cid() == g2.payment.cid()
            assert g1.payment.paypal() == g2.payment.paypal()

    def test_generic_personal(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.personal.age() == g2.personal.age()
            assert g1.personal.name() == g2.personal.name()

    def test_generic_science(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.science.chemical_element() == \
                g2.science.chemical_element()
            assert g1.science.math_formula() == g2.science.math_formula()

    def test_generic_structured(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.structured.css() == g2.structured.css()
            assert g1.structured.html() == g2.structured.html()

    def test_generic_text(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.text.swear_word() == g2.text.swear_word()
            assert g1.text.color() == g2.text.color()

    def test_generic_transport(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.transport.truck() == g2.transport.truck()
            assert g1.transport.airplane() == g2.transport.airplane()

    def test_generic_unit_system(self, _generics):
        g1, g2 = _generics
        for _ in range(self.TIMES):
            assert g1.unit_system.unit() == g2.unit_system.unit()
            assert g1.unit_system.prefix() == g2.unit_system.prefix()
