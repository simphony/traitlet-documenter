import unittest

import mock

from traitlets_documenter import setup
from traitlets_documenter.class_traitlets_documenter import (
    ClassTraitletDocumenter)


class TestSphinxSetup(unittest.TestCase):

    def test_setup(self):
        app = mock.Mock()
        setup(app)
        expected = app.add_autodocumenter.call_args_list
        calls = [
            mock.call(ClassTraitletDocumenter)]
        self.assertEqual(expected, calls)

if __name__ == '__main__':
    unittest.main()
