import {GoalAkio} from "./goal-akio.model";
import {GoalHaru} from "./goal-haru.model";

export class AttackOrchestration {
  goal_akio_by_cluster_id: Record<string, GoalAkio>;
  goal_haru_by_cluster_id: Record<string, GoalHaru>;

  constructor(object: any) {
    this.goal_akio_by_cluster_id = object.goal_akio_by_cluster_id;
    this.goal_haru_by_cluster_id = object.goal_haru_by_cluster_id;
  }
}
