# -*- coding: utf-8 -*-

import unittest
from flaskext.api import ApiError, Client

class TestCase(unittest.TestCase):
    
    def setUp(self):
        self.api = Client('http://localhost:5000')
    
    def test_new_task(self):
        self.assertRaises(ApiError, self.api.tasks.new)
        result = self.api.tasks.new(title='bla')['result']
        self.assertEqual(result, {'title': 'bla', 'text': None})


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCase))
    return suite
        
if __name__ == '__main__':
    unittest.main()        
