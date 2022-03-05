from typing import Dict
from pydantic import BaseModel
from simplestr import gen_str_repr_eq
from rvkinh_message_protocol.controller.goal_akio import GoalAkio
from rvkinh_message_protocol.controller.goal_haru import GoalHaru


@gen_str_repr_eq
class AttackOrchestration(BaseModel):
    goal_akio_by_cluster_id: Dict[str, GoalAkio]
    goal_haru_by_cluster_id: Dict[str, GoalHaru]

    def __init__(self, goal_akio_by_cluster_id: Dict[str, GoalAkio], goal_haru_by_cluster_id: Dict[str, GoalHaru]) -> None:
        super().__init__(goal_akio_by_cluster_id=goal_akio_by_cluster_id, goal_haru_by_cluster_id=goal_haru_by_cluster_id)
