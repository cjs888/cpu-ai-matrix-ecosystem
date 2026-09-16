from message import StandardMessage
from scheduler import Scheduler


class SimulationClient:
    def __init__(self, scheduler: Scheduler):
        self.scheduler = scheduler

    def submit_task(self, user_input_text: str):
        request_msg = StandardMessage.build(
            from_id="client",
            target_id="scheduler",
            payload={"text": user_input_text}
        )
        result_msg = self.scheduler.route_and_run(request_msg)
        print("\n==== Client received final result ====")
        print(result_msg.payload)
        return result_msg
