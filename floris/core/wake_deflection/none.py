
from typing import Any, Dict

import numpy as np
from attrs import define

from floris.core import (
    BaseModel,
    FlowField,
    Grid,
)


@define
class NoneVelocityDeflection(BaseModel):
    """
    The None deflection model is a placeholder code that simple ignores any
    deflection and returns an array of zeroes.
    """

    def prepare_function(
        self,
        grid: Grid,
        flow_field: FlowField,
    ) -> Dict[str, Any]:

        kwargs = {
            "freestream_velocity": flow_field.u_initial_sorted,
        }
        return kwargs

    def function(
        self,
        x_i: np.ndarray,
        y_i: np.ndarray,
        yaw_i: np.ndarray,
        turbulence_intensity_i: np.ndarray,
        ct_i: np.ndarray,
        rotor_diameter_i: float,
        *,
        freestream_velocity: np.ndarray,
    ):
        """Skip all deflection calculations and returns zeros array."""
        self.logger.info(
            "The wake deflection model is set to 'none'. Deflection modeling disabled."
        )
        if np.any(np.abs(yaw_i) > 0.001):
            raise ValueError(
                "The deflection model is disabled yet not all effective yaw angles are zero. " +
                "To resolve this error, please ensure secondary steering is disabled in your " +
                "input file and ensure no nonzero yaw angles are passed to the floris object."
            )

        return np.zeros_like(freestream_velocity)
