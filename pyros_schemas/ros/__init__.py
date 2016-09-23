from __future__ import absolute_import
from __future__ import print_function

from .decorators import wraps_cls  # useful for direct import even if not included in __all__
from .decorators import with_explicitly_matched_type
from .fields import (
    RosBool,
    RosInt8, RosInt16, RosInt32, RosInt64,
    RosUInt8, RosUInt16, RosUInt32, RosUInt64,
    RosFloat32, RosFloat64,
    RosString, RosTextString,
    RosOpt,
)

from .std_msgs_schemas import (
    RosMsgBool,
    RosMsgInt8, RosMsgInt16, RosMsgInt32, RosMsgInt64,
    RosMsgUInt8, RosMsgUInt16, RosMsgUInt32, RosMsgUInt64,
    RosMsgFloat32, RosMsgFloat64,
    RosMsgString,
)

# from .fields import (
#     RosTextString,
# )
#
# from .fields_extra import (
#     OptNested,
#     OptEmpty,
#     OptBool,
#     OptString,
# )
#
# __all__ = [
#     'with_explicitly_matched_type',
#     'with_explicitly_matched_optional_type',
#
#     'RosBool',
#     'RosInt8', 'RosInt16', 'RosInt32', 'RosInt64',
#     'RosUInt8', 'RosUInt16', 'RosUInt32', 'RosUInt64',
#     'RosFloat32', 'RosFloat64',
#     'RosString',
#
#     'RosTextString',
#     'OptNested',
#     'OptEmpty',
#     'OptString',
# ]