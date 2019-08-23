import unittest
import model.test_model as test_model
import model.test_image as test_image

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_model))
suite.addTests(loader.loadTestsFromModule(test_image))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)