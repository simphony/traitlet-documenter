from traitlets import Float, HasTraits, Int

module_trait = Float


def dummy_function():
    pass


class Dummy(HasTraits):

    trait_1 = Float

    not_trait = 2

    trait_2 = Float  # second comment


class Dummy1(HasTraits):

    trait_1 = Int

    not_trait = 2
