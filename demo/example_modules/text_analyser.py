from message import StandardMessage
from micro_module import BaseMicroModule


class TextAnalyserModule(BaseMicroModule):
    """
    General‑purpose text analysis demo module.
    Can be replaced by semantic extraction, metadata parsing, multi‑modal parsing in real‑world practice.
    """
    def __init__(self):
        super().__init__(module_id="text_analyser")

    def load(self) -> None:
        self.loaded = True
        print(f"[{self.module_id}] module loaded into memory.")

    def process(self, msg: StandardMessage) -> StandardMessage:
        content = msg.payload.get("content", "")
        analysed_data = {
            "raw_length": len(content),
            "keyword_tags": ["demo", "sample", "matrix"]
        }
        resp = StandardMessage.build(
            from_id=self.module_id,
            target_id="scheduler",
            payload=analysed_data,
            task_id=msg.header.task_id
        )
        return resp
