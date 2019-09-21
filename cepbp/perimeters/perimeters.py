import numpy as np
from cepbp.common.pick_dimension import PickDimension


class Perimeters(PickDimension):
    """
    Class, encpsulating all calculations related to perimeters
    """

    def __init__(self, dimension='perimeter'):
        PickDimension.__init__(self)

    @staticmethod
    def rectangle_perimeter(measurements):
        """
        Calculate the perimeter of a rectangle

        Parameters
        ----------
        measurements: tuple of n float elements

        Returns
        -------
        float
        """
        return (measurements[0] + measurements[1]) * 2.0

    @staticmethod
    def circle_perimeter(measurements):
        """
        Calculate the perimeter of a circle

        Parameters
        ----------
        measurements: tuple of n float elements

        Returns
        -------
        float
        """
        return (2.0 * np.pi * measurements[0])

    def perimeter_value(self, measurements, shape):
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
        return self.dimension_calculation(measurements, shape, 'perimeter')
