from __future__ import print_function
from context import cepbp
from cepbp.perimeters.perimeters import Perimeters
from cepbp.common.custom_error_handler import CustomError
from cepbp.dimension_calculator import DimensionCalculator
import numpy as np


class TestDimensionCalculator:

    def test_shapes_dimensions_good_inputs(self):
        dc = DimensionCalculator(1, submitted_by='tester')
        for shape in ['rectangle', 'circle']:
            for dimension in ['perimeter', 'area']:
                assert isinstance(dc.output_dimension_value((1, 1), shape, dimension), float)

    def test_shapes_dimensions_bad_inputs(self):
        dc = DimensionCalculator(1, submitted_by='tester')
        assert (dc.output_dimension_value((1, 1), 'rectangles', 'perimeter') is None)
        assert (dc.output_dimension_value((1, 1), 'rectangle', 'perimeters') is None)
        assert (dc.output_dimension_value((1, 1), 'rectangles', 'perimeters') is None)

    def test_measurements_inputs(self):
        dc = DimensionCalculator()
        assert (dc.output_dimension_value((-1, 1), 'rectangle', 'perimeter') is None)
        assert (dc.output_dimension_value((1, -1), 'rectangle', 'perimeter') is None)
        assert (dc.output_dimension_value((-1, -1), 'rectangle', 'perimeter') is None)
        assert (dc.output_dimension_value((np.inf, 1), 'rectangle', 'perimeter') is None)
        assert (dc.output_dimension_value((1, -np.inf), 'rectangle', 'perimeter') is None)
        assert (dc.output_dimension_value((1, 'test'), 'rectangle', 'perimeter') is None)
        assert (dc.output_dimension_value((1), 'rectangle', 'perimeter') is None)
        assert (dc.output_dimension_value((), 'rectangle', 'perimeter') is None)
