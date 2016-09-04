from traitlets import Float, Int, List

constant = 1

if False:

    trait_2 = List(Float)

if True:

    #: inside definition
    trait_2 = List(Int)

    #: another definition
    trait_3 = List(Float)
