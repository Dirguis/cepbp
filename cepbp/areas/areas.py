import numpy as np
from cepbp.common.pick_dimension import PickDimension


class Areas(PickDimension):
    """
    Class, encpsulating all calculations related to areas
    """

    def __init__(self, dimension='area'):
        PickDimension.__init__(self)

    @staticmethod
    def rectangle_area(measurements):
        """
        Calculate the area of a rectangle

        Parameters
        ----------
        measurements: tuple of n float elements

        Returns
        -------
        float
        """
        return measurements[0] * measurements[1] * 1.0

    @staticmethod
    def circle_area(measurements):
        """
        Calculate the area of a circle

        Parameters
        ----------
        measurements: tuple of n float elements

        Returns
        -------
        float
        """
        return np.pi * (measurements[0] ** 2)

    def area_value(self, measurements, shape):
        """
        Given inputs, return the right method to calculate the dimension for a selected shape and dimension

        Parameters
        ----------
        measurements: tuple of integers
          Tuple object containing the measurement of the object of interest
        shape: string
          'rectangle' for example

        Returns
        -------
        float
          The function makes a call to another function that will pick the correct method, execute it and return the result
        """
        return self.dimension_calculation(measurements, shape, 'area')
