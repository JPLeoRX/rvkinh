import threading
from injectable import injectable
from rvkinh_message_protocol import AttackOrchestration


ATTACK_ORCHESTRATION = AttackOrchestration({}, {})
ATTACK_ORCHESTRATION_LOCK = threading.Lock()


@injectable
class ServiceAttackOrchestration:
    def set(self, attack_orchestration: AttackOrchestration) -> bool:
        with ATTACK_ORCHESTRATION_LOCK:
            ATTACK_ORCHESTRATION.goal_akio_by_cluster_id = attack_orchestration.goal_akio_by_cluster_id
            ATTACK_ORCHESTRATION.goal_haru_by_cluster_id = attack_orchestration.goal_haru_by_cluster_id
        return True

    def get(self) -> AttackOrchestration:
        return ATTACK_ORCHESTRATION
