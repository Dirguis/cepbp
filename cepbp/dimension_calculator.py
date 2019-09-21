from __future__ import print_function
from cepbp.common.input_testing import TestInputs
from cepbp.common.logs import Logs
from cepbp.common.custom_error_handler import CustomError
from cepbp.areas import Areas
from cepbp.perimeters import Perimeters
import configparser
import logging
import sys
import numpy as np


class ShapeName(object):

    def __init__(self):
        pass

    def print_shape(self, shape):
        print("The shape is a %s" % self.shape)


class DimensionCalculator(ShapeName, Perimeters, Areas, TestInputs):
    """
    General class to calculate the area of various shapes. Only the rectangles and circles are supported for perimeters and areas.

    Parameters
    ----------
    *args: integer
      Only the first element in args is used and corresponds to the user's group ID
    **kwargs: dictionary
      Only the key 'submitted_by' is used and corresponds to the user's name

    Example
    ----------
    from cepbp.dimension_calculator import DimensionCalculator
    dc = DimensionCalculator(1, submitted_by='Damien Forthomme')
    dc.output_dimension_value((3, 4), 'rectangle', 'areas')
    >>> Request submitted by Damien Forthomme
    >>> Request submitted by group 1
    >>> rectangle area: 12.000

    """
    def __init__(self, *args, **kwargs):
        TestInputs.__init__(self)
        self.group_nb = ''
        if args:
            self.group_nb = str(args[0])
        self.submitted_by = str(kwargs.get('submitted_by', ''))

        self.logger = Logs()
        self.logger.get_logger(name='logs_shape_dimension')

    def output_dimension_value(self, measurements, shape, dimension):
        """
        General function to handle all the steps to calcuate the dimension for a shape and measurement set.
        The result of the calculations are printed and logged.
        The inputs are checked for basic errors.

        Parameters
        ----------
        measurements: tuple of integers
          Tuple object containing the measurement of the object of interest
        shape: string
          'rectangle' for example
        dimension: string
          'perimeter' for example
        """

        if self.submitted_by:
            self.logger.print_and_log('Request submitted by %s' % self.submitted_by)
        if self.group_nb:
            self.logger.print_and_log('Request submitted by group %s' % self.group_nb)
        if (isinstance(measurements, float) | isinstance(measurements, int)):
            measurements = [measurements]

        try:
            errors = self.run_input_tests(shape, dimension, measurements)
            if errors:
                msg = '\n'.join(errors)
                raise CustomError(msg, (measurements, shape, dimension))
        except CustomError as e:
            self.logger.print_and_log('Error: {}\nData: \n{}'.format(e.msg, e.data), 'error')
            return None

        if dimension == 'perimeter':
            dimension_value = self.perimeter_value(measurements, shape)
        if dimension == 'area':
            dimension_value = self.area_value(measurements, shape)

        try:
            if np.isinf(dimension_value):
                msg = 'The dimension value is infinite. Please check inputs'
                raise CustomError(msg, (measurements, shape, dimension))
        except Exception as e:
            self.logger.print_and_log('Error: {}\nData: \n{}'.format(e.msg, e.data), 'error')
            return None

        self.logger.print_and_log('%s %s: %0.3f' % (shape, dimension, dimension_value))
        return dimension_value
