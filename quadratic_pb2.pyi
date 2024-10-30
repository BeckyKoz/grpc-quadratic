from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QuadraticRequest(_message.Message):
    __slots__ = ("coeffa", "coeffb", "coeffc")
    COEFFA_FIELD_NUMBER: _ClassVar[int]
    COEFFB_FIELD_NUMBER: _ClassVar[int]
    COEFFC_FIELD_NUMBER: _ClassVar[int]
    coeffa: float
    coeffb: float
    coeffc: float
    def __init__(self, coeffa: _Optional[float] = ..., coeffb: _Optional[float] = ..., coeffc: _Optional[float] = ...) -> None: ...

class QuadraticReply(_message.Message):
    __slots__ = ("solution",)
    SOLUTION_FIELD_NUMBER: _ClassVar[int]
    solution: str
    def __init__(self, solution: _Optional[str] = ...) -> None: ...
