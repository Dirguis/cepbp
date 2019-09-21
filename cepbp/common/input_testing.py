class TestInputs(object):
    """
    General class to handle input testings
    Note that some static variables are defined here. They could/should come from a configuration file
    """

    def __init__(self):
        self.allowed_shapes = ['circle', 'rectangle']
        self.allowed_dimensions = ['perimeter', 'area']

    def shape_testing(self, shape):
        """
        Test the input shape. They should be in the allowed_shapes list

        Parameters
        ----------
        shape: string
          'rectangle' for example

        Returns
        -------
        string
        """
        if shape in self.allowed_shapes:
            return ''
        else:
            error_msg = 'Shape %s is not supported. Choose from %s' % (shape, self.allowed_shapes)
            return error_msg

    def dimension_testing(self, dimension):
        """
        Test the input dimension. They should be in the allowed_dimensions list

        Parameters
        ----------
        dimension: string
          'perimeter' for example

        Returns
        -------
        string
        """
        if dimension in self.allowed_dimensions:
            return ''
        else:
            error_msg = 'Dimension %s is not supported. Choose from %s' % (dimension, self.allowed_dimensions)
            return error_msg

    def measurement_testing(self, measurements):
        """
        Test the input measurements. All values must be strictly positive and float or int

        Parameters
        ----------
        measurements: tuple of n float elements

        Returns
        -------
        string
        """
        if (isinstance(measurements, list) | isinstance(measurements, tuple)):
            for measurement in measurements:
                if isinstance(measurement, str):
                    error_msg = 'Individual measurements cannot be strings'
                    return error_msg
                if measurement <= 0:
                    error_msg = 'All measurements must be positive: {}'.format(measurements)
                    return error_msg
                if not (isinstance(measurement, float) | isinstance(measurement, int)):
                    error_msg = 'All measurements must be floats or integers: {}'.format(measurements)
                    return error_msg
        else:
            error_msg = 'Measurements must be a list or tuple: {}'.format(measurements)
            return error_msg
        return ''

    def measurement_length_testing(self, shape, measurements):
        """
        Make sure there is enough data passed in "measurements" given a shape

        Parameters
        ----------
        shape: string
          'rectangle' for example
        measurements: tuple or list of ints or floats

        Returns
        -------
        string
        """
        if shape == 'circle':
            if len(measurements) == 0:
                error_msg = 'There should be at least 1 measurement for shape circle: {}'.format(measurements)
                return error_msg

        if shape == 'rectangle':
            if len(measurements) <= 1:
                error_msg = 'There should be at least 2 measurement for shape rectangle: {}'.format(measurements)
                return error_msg

    def run_input_tests(self, shape, dimension, measurements):
        """
        Compile all the potential input errors

        Parameters
        ----------
        shape: string
          'rectangle' for example
        dimension: string
          'perimeter' for example
        measurements: tuple
          tuple of n elements

        Returns
        -------
        list of strings
          list of the error messages if there are any
        """
        errors = [
            self.shape_testing(shape),
            self.dimension_testing(dimension),
            self.measurement_testing(measurements),
            self.measurement_length_testing(shape, measurements)
        ]
        return [error for error in errors if error]
