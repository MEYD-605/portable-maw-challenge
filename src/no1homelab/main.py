import argparse
from .core.agent_mind import AgentMind
from .core.planner_tree import PlannerTree
from .core.soul_filter import SoulFilter

class Agent:
    """The main agent class for No. 1, orchestrating the core modules."""

    def __init__(self):
        print("🧠 Initializing cognitive modules...")
        self.mind = AgentMind()
        self.planner = PlannerTree()
        self.filter = SoulFilter()
        self.identity = self.mind.load_identity()
        print("✅ Agent No. 1 is online.")

    def execute_task(self, prompt: str):
        """Executes a task by flowing through the cognitive architecture."""
        print(f"\n[INPUT] Received prompt: '{prompt}'")

        # 1. Mind: Understand the user's intent
        intent_response = self.mind.understand_intent(prompt)
        print(f"\n[MIND] Raw Response:\n---\n{intent_response}\n---")

        # --- Temporarily bypassing Filter and Planner for direct brain test ---
        # # 2. Filter: Check if the intent is valid
        # if not self.filter.validate_intent(intent):
        #     print("[SOUL] Intent rejected by filter.")
        #     return
        # print("[SOUL] Intent validated.")

        # # 3. Planner: Create a plan based on the intent
        # plan = self.planner.create_plan(intent)
        # print(f"[PLANNER] Plan created with {len(plan)} steps.")

        # # 4. Execute the plan (Placeholder)
        # print("Executing plan...")
        # for i, step in enumerate(plan, 1):
        #     print(f"  Step {i}: {step}")
        print("\n✅ Direct brain test finished. Downstream modules (Filter, Planner) were bypassed.")

def cli():
    """Defines the command-line interface for the agent."""
    parser = argparse.ArgumentParser(description="No. 1 - The Genesis Agent. A J.A.R.V.I.S. prototype.")
    parser.add_argument("prompt", type=str, nargs='?', default=None, help="The main prompt or task for the agent.")

    args = parser.parse_args()
    agent = Agent()

    if args.prompt:
        agent.execute_task(args.prompt)
    else:
        print("\nNo prompt provided. Agent is online and awaiting instructions.")
        print("Example: no1-scaffold \"Create a simple Flask project structure.\"")

if __name__ == "__main__":
    cli()