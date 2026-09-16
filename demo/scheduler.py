from typing import Dict, List
from message import StandardMessage
from micro_module import BaseMicroModule


class Scheduler:
    """
    Minimal prototype implementation of global scheduling core.
    NOT official standard, only for architecture demonstration.
    Rules:
        1. Modules cannot communicate directly, all traffic pass scheduler.
        2. Scheduler never contains domain business logic.
    """
    def __init__(self):
        self.module_registry: Dict[str, BaseMicroModule] = {}

    def register_module(self, module: BaseMicroModule) -> None:
        self.module_registry[module.module_id] = module
        print(f"[Scheduler] module registered: {module.module_id}")

    def split_task(self, user_payload: Dict) -> List[Dict]:
        """
        Demo version: simple rule‑based task split.
        In the future, community can replace this logic freely.
        """
        raw_text = user_payload.get("text", "")
        return [
            {"action": "analyse", "content": raw_text},
            {"action": "compute", "source_key": "analysed_result"}
        ]

    def route_and_run(self, root_msg: StandardMessage) -> StandardMessage:
        task_id = root_msg.header.task_id
        user_payload = root_msg.payload
        subtask_list = self.split_task(user_payload)

        cache: Dict[str, Dict] = {}
        final_payload: Dict = {}

        # Subtask 1: text analyser
        msg_analyse = StandardMessage.build(
            from_id="scheduler",
            target_id="text_analyser",
            payload=subtask_list[0],
            task_id=task_id
        )
        analyser = self.module_registry["text_analyser"]
        if not analyser.is_loaded():
            analyser.load()
        res_analyse = analyser.process(msg_analyse)
        cache["analysed_result"] = res_analyse.payload

        # Subtask 2: data compute
        subtask_2 = subtask_list[1]
        subtask_2["input_data"] = cache["analysed_result"]
        msg_compute = StandardMessage.build(
            from_id="scheduler",
            target_id="data_compute",
            payload=subtask_2,
            task_id=task_id
        )
        calculator = self.module_registry["data_compute"]
        if not calculator.is_loaded():
            calculator.load()
        res_compute = calculator.process(msg_compute)
        final_payload["final_result"] = res_compute.payload

        # Notify resource release
        for _, mod in self.module_registry.items():
            mod.unload()

        output_msg = StandardMessage.build(
            from_id="scheduler",
            target_id="client",
            payload=final_payload,
            task_id=task_id
        )
        return output_msg
