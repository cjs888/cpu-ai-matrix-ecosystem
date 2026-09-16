from message import StandardMessage
from micro_module import BaseMicroModule


class DataComputeModule(BaseMicroModule):
    """
    General‑purpose numerical & structural computing demo module.
    Can be extended to simulation, engineering calculation, parameter generation and other scenarios.
    """
    def __init__(self):
        super().__init__(module_id="data_compute")

    def load(self) -> None:
        self.loaded = True
        print(f"[{self.module_id}] module loaded into memory.")

    def process(self, msg: StandardMessage) -> StandardMessage:
        input_data = msg.payload.get("input_data", {})
        output = {
            "computed_value": input_data.get("raw_length", 0) * 2,
            "derived_tags": input_data.get("keyword_tags", [])
        }
        resp = StandardMessage.build(
            from_id=self.module_id,
            target_id="scheduler",
            payload=output,
            task_id=msg.header.task_id
        )
        return resp
