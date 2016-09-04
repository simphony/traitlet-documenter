from __future__ import unicode_literals
import unittest

from traitlets_documenter.tests import test_file, test_file2
from traitlets_documenter.tests.test_file import Dummy, dummy_function
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

    def test_get_simple_class_trait_definition(self):
        # given
        parent = Dummy
        object_name = 'trait_1'

        # when
        definition = get_trait_definition(parent, object_name)

        # then
        self.assertEqual(definition, 'Float')

    def test_get_trait_definition_from_function(self):

        object_name = 'trait_1'

        # when/then
        self.assertRaises(
            DefinitionError,
            get_trait_definition,
            dummy_function, object_name)

    def test_get_simple_class_trait_definition_with_comments(self):
        # given
        parent = Dummy
        object_name = 'trait_4'

        # when
        definition = get_trait_definition(parent, object_name)

        # then
        self.assertEqual(definition, 'Float')

    def test_get_trait_definition_inside_if_block(self):
        # given
        parent = test_file2
        object_name = 'trait_2'

        # when
        definition = get_trait_definition(parent, object_name)

        # then
        self.assertEqual(definition, "List(Int)")


if __name__ == '__main__':
    unittest.main()
