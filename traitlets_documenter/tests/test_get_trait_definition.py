from __future__ import unicode_literals
import unittest

from traitlets_documenter.tests import test_file
from traitlets_documenter.tests.test_file import dummy_function
from traitlets_documenter.util import get_trait_definition, DefinitionError


class TestGetTraitDefinition(unittest.TestCase):

    def test_get_invalid_module_trait_definition(self):
        # given
        parent = test_file
        object_name = 'invalid_trait'

        # when/then
        self.assertRaises(
            DefinitionError,
            get_trait_definition,
            parent, object_name)

    def test_get_trait_definition_from_function(self):

        object_name = 'trait_1'

        # when/then
        self.assertRaises(
            DefinitionError,
            get_trait_definition,
            dummy_function, object_name)


if __name__ == '__main__':
    unittest.main()
