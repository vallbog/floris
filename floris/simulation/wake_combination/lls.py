# Copyright 2021 NREL

# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

import numpy as np
from attrs import define

from floris.simulation import BaseModel


@define
class LLS(BaseModel):
    """
    FLS uses local linear superposition to combine the base flow field
    with the velocitiy deficits.
    """

    def prepare_function(self) -> dict:
        pass

    def function(
        self,
        wake_field: np.ndarray,
        velocity_deficit_dim: np.ndarray,
        u_initial: np.ndarray,
        u_inflow: np.ndarray,
    ):
        velocity_deficit_dim_local = u_inflow - u_initial + velocity_deficit_dim
        return wake_field + velocity_deficit_dim_local
