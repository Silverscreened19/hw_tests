from main import geo_logs_func, geo_logs, unique_ids, ids, stats, max_vol_channel
import unittest
from unittest import TestCase
from ya import YaDisk, token_ya
from unittest import TestCase


class TestGeoLogsFunc(TestCase):
    def test_geo_list(self):
        res = geo_logs_func(geo_logs)
        self.assertIsInstance(res, list)
        self.assertIsNotNone(res)

    def test_len_list(self):
        res = geo_logs_func(geo_logs)
        self.assertEqual(len(res), 6)

    @unittest.expectedFailure
    def test_geo_list_equal(self):
        res = geo_logs_func(geo_logs)
        self.assertListEqual(res, geo_logs.copy)

    def test_russia_in_geo(self):
        res = geo_logs_func(geo_logs)
        for visit in res:
            self.assertIn('Россия', list(visit.values())[0][1])

    def test_geo_params_india(self):
        res = geo_logs_func(geo_logs)
        for visit in res:
            self.assertNotIn('Индия', list(visit.values())[0][1])

    def test_geo_params_portugal(self):
        res = geo_logs_func(geo_logs)
        for visit in res:
            self.assertNotIn('Португалия', list(visit.values())[0][1])

    def test_geo_params_france(self):
        res = geo_logs_func(geo_logs)
        for visit in res:
            self.assertNotIn('Франция', list(visit.values())[0][1])


class TestUniqueIds(TestCase):
    def test_len(self):
        res = unique_ids(ids)
        self.assertEqual(len(res), 6)

    def test_set_type(self):
        res = unique_ids(ids)
        self.assertIsInstance(res, list)
        self.assertIsNotNone(res)

    def test_ids_unique(self):
        res = unique_ids(ids)
        self.assertListEqual(res, list(set(res)))


class TestChannel(TestCase):
    def test_key(self):
        res = max_vol_channel(ids)
        self.assertIn(res, stats.keys())

    def test_type(self):
        res = max_vol_channel(ids)
        self.assertIsInstance(res, str)
        self.assertNotIsInstance(res, int)

    def test_name_ya(self):
        res = max_vol_channel(ids)
        self.assertEqual(res, 'yandex')

    def test_name_fb(self):
        res = max_vol_channel(ids)
        self.assertNotEqual(res, 'facebook')

    def test_name_vk(self):
        res = max_vol_channel(ids)
        self.assertNotEqual(res, 'vk')

    def test_name_goo(self):
        res = max_vol_channel(ids)
        self.assertNotEqual(res, 'google')

    def test_name_em(self):
        res = max_vol_channel(ids)
        self.assertNotEqual(res, 'email')

    def test_name_ok(self):
        res = max_vol_channel(ids)
        self.assertNotEqual(res, 'ok')


class TestYandex(TestCase):

    def test_response(self):
        yadisk = YaDisk(token_ya)
        res = yadisk.create_folder()
        self.assertEqual(res, 201)
        self.assertNotEqual(res, 400)
        self.assertNotEqual(res, 401)
        self.assertNotEqual(res, 403)
        self.assertNotEqual(res, 404)
        self.assertNotEqual(res, 406)
        self.assertNotEqual(res, 409)
        self.assertNotEqual(res, 413)
        self.assertNotEqual(res, 423)
        self.assertNotEqual(res, 429)
        self.assertNotEqual(res, 503)
        self.assertNotEqual(res, 507)
