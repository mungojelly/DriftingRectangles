import pytest
import driftingrectangles

def test_drifting_zero_stays_still():
    rectangle_that_should_stay_still = {
        "x": 0,
        "y": 0,
        "x_drift": 0,
        "y_drift": 0
        }
    drifted_nowhere = driftingrectangles.drift_rectangles({
        "rectangles": [rectangle_that_should_stay_still]
        })
    assert drifted_nowhere["rectangles"][0] == rectangle_that_should_stay_still
