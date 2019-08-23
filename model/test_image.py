import unittest
import PIL
from PIL import Image
import numpy as np
from numpy.testing import assert_array_equal
import io
import os
from model.image import decode_image

class TestImage(unittest.TestCase):
    def test_decode_image(self):
        publicPath = '{}/'.format(os.getcwd())
        img = Image.open(publicPath + 'model/fixtures/euro.jpg')

        imgByteArr = io.BytesIO()
        img.save(imgByteArr, format=img.format)
        imgByteArr = imgByteArr.getvalue()

        expected = np.array(img)
        result = np.array(decode_image(imgByteArr))

        assert_array_equal(expected, result)

