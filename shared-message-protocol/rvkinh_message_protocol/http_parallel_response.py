from typing import Dict, Any, List
from simplestr import gen_str_repr_eq
from rvkinh_message_protocol.http_response import HttpResponse


@gen_str_repr_eq
class HttpParallelResponse:
    responses: List[HttpResponse]
    execution_time: float

    def __init__(self, responses: List[HttpResponse], execution_time: float):
        self.responses = responses
        self.execution_time = execution_time
