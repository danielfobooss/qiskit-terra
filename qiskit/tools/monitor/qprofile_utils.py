# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Profiler decorator
"""
import sys
import logging

logger = logging.getLogger(__name__)

def qprofile(func):
    def wrapper(*original_args, **original_kwargs):
        qobj = func(*original_args, **original_kwargs)
        if logging.root.level >= logging.DEBUG:
            logger.debug("<<Profiling Info>> qobj is {} bytes".format(
                sys.getsizeof(qobj)))
        return qobj
    return wrapper
