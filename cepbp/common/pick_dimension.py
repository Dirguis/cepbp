class PickDimension(object):
    """
    Automatically pick the right method from the child class to execute in order to get the dimension that the user wants
    """

    def __init__(self):
        pass

    def dimension_calculation(self, measurements, shape, dimension):
        """
        Automatically pick the right method from the child class to execute in order to get the dimension that the user wants

        Parameters
        ----------
        measurements: tuple of integers
          Tuple object containing the measurement of the object of interest
        shape: string
          'rectangle' for example
        dimension: string
          'perimeter' for example

        Returns
        -------
        float
          The caclulated dimension
        """
        return getattr(self, '_'.join((shape, dimension)))(measurements)
