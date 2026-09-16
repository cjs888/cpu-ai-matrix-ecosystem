from abc import ABC, abstractmethod
from typing import Optional
from message import StandardMessage


class BaseMicroModule(ABC):
    """
    Abstract base class for all micro‑modules inside AI matrix.
    Prototype only, not official standard.
    Every professional module shall inherit this base class in this demo.
    """
    def __init__(self, module_id: str):
        self.module_id: str = module_id
        self.loaded: bool = False

    @abstractmethod
    def load(self) -> None:
        """Load model, weights, initialize resources."""
        pass

    @abstractmethod
    def process(self, msg: StandardMessage) -> StandardMessage:
        """Receive standard message, execute business logic, return result message."""
        pass

    def unload(self) -> None:
        """Release memory, unload all occupied resources."""
        self.loaded = False
        print(f"[Module {self.module_id}] resource unloaded.")

    def is_loaded(self) -> bool:
        return self.loaded
