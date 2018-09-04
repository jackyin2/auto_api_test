#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: test_login.py
@time: 17-4-19 上午10:41
"""
import unittest, requests
from lib.log import LOG
from lib.tools import failrun
from lib.config_operate import ConfigOperate
from parameterized import parameterized, param


class TestSignUp(unittest.TestCase):
    '''报名接口测试'''

    def setUp(self):
        self.url = ConfigOperate('UrlConf').get_config('bj_tuanche', 'url')
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Content-Type":"application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }

    @parameterized.expand(
        [
            param("phone_null",
                  data_params={'name': 'linlang9', 'cityId': 10, 'carStyleId': 32633, 'brandId': 67, 'groupbyType': 1,
                               'groupbyNum': 2001}),
            param(
                "name_null",
                data_params={'phone': '15633669988', 'cityId': 10, 'carStyleId': 32633, 'brandId': 67, 'groupbyType': 1,
                             'groupbyNum': 2001}),
            param("city_null",
                  data_params={'name': 'linlang9', 'phone': '15633669988', 'carStyleId': 32633, 'brandId': 67,
                               'groupbyType': 1,
                               'groupbyNum': 2001})
        ]
    )
    def test_sign_params_null(self, _, data_params):
        '''验证报名各字段参数为空'''
        uri = '/bentley/api/applyForTcjAsyn/'
        response = requests.post(self.url + uri, data=data_params, headers=self.headers)
        LOG.info('请求{0},参数{1},状态{2},\n 响应数据{3}'.format(uri, data_params, response, response.text))
        self.assertEqual(response.status_code, 200, '断言响应结果为200')
        self.assertEqual(response.json()['code'], 100001, '断言结果为100001')
        self.assertEqual(response.json()['msg'], '参数异常', '断言参数异常')

    def test_sign(self):
        '''验证正常参数报名'''
        uri = '/bentley/api/applyForTcjAsyn/'
        data_params = {'name': 'linlang66', 'phone': '15633996699','cityId': 10, 'carStyleId': 32,
                       'brandId': 67, 'groupbyType': 1,'groupbyNum': 2001}
        response = requests.post(self.url + uri, data=data_params, headers=self.headers)
        LOG.info('请求{0},参数{1},状态{2},\n 响应数据{3}'.format(uri, data_params, response, response.text))
        self.assertEqual(response.status_code, 200, '断言响应结果为200')
        self.assertEqual(response.json()['code'], 100000, '断言结果为100000')

    def tearDown(self):
        pass

if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestSignUp("test_sign"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
