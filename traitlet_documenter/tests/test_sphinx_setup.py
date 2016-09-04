import unittest

import mock

from traitlet_documenter import setup
from traitlet_documenter.class_traitlet_documenter import (
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
