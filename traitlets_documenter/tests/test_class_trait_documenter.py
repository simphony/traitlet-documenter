from __future__ import unicode_literals
import unittest

import mock

from traitlets_documenter.class_traitlets_documenter import (
    ClassTraitletDocumenter)


class TestClassTraitletDocumenter(unittest.TestCase):

    def test_import_object_with_error(self):
        # given
        documenter = ClassTraitletDocumenter(mock.Mock(), 'test')
        documenter.modname = 'invalid456767'
        documenter.objpath = ['Dummy', 'trait_1']

        # when
        result = documenter.import_object()

        # then
        self.assertFalse(result)
        documenter.env.note_reread.assert_called()

if __name__ == '__main__':
    unittest.main()
