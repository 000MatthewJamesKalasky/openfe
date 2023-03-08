from gufe import AlchemicalNetwork


class _abstract_transformer():
    """
        This class type is thought to be the part that transforms identified edges/transformations for chemical systems of an FE-campaign to an Alchemical
        Network.

        This can be very simple like simple transform where one protocol is directly mapped onto one transformation, but it could also be complex,
        where one transformation gets a protocols assigned from a set of protocols, depending on certain metrics.
    """

    def __call__(self, *args, **kwargs) -> AlchemicalNetwork:
        raise NotImplementedError()