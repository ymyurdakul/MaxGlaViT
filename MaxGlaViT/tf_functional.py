from tensorflow.nn import *
from tensorflow.math import *

from tensorflow import (
    abs,
    cast,
    clip_by_value,
    complex,
    concat,
    convert_to_tensor,
    expand_dims,
    gather,
    gather_nd,
    linspace,
    map_fn,
    matmul,
    norm,
    pad,
    print,
    range,
    repeat,
    reshape,
    shape,
    sign,
    split,
    squeeze,
    stack,
    tensor_scatter_nd_update,
    tile,
    transpose,
    unstack,
    where,
    zeros,
)
from tensorflow.image import resize, extract_patches, non_max_suppression_with_scores
from tensorflow.signal import irfft2d, rfft2d


def assign(parameter, data):
    parameter.assign(data)
