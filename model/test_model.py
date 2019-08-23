import unittest
from model.predictor import pretty_print_prediction 

class TestPredictor(unittest.TestCase):
    def test_pretty_print_prediction(self):
        prediction = '1 Euro, Euro, Spain'
        expected = {
            "coin": '1 Euro',
            "currency": ' Euro',
            "country": ' Spain'
        }
        result = pretty_print_prediction(prediction)
        self.assertDictEqual(result, expected)

    