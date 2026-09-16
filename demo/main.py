from scheduler import Scheduler
from client import SimulationClient
from example_modules.text_analyser import TextAnalyserModule
from example_modules.data_compute import DataComputeModule


def main():
    scheduler = Scheduler()
    scheduler.register_module(TextAnalyserModule())
    scheduler.register_module(DataComputeModule())

    client = SimulationClient(scheduler)
    sample_input = "General‑purpose CPU AI matrix ecosystem for all mankind, open global co‑construction."
    client.submit_task(sample_input)


if __name__ == "__main__":
    main()
