import litellm
from pathlib import Path
import os

class SoulFilter:
    """The 'Conscience'. Validates actions against the system's core principles, ensuring safety and 'love'."""

    def __init__(self):
        self.identity = self.load_identity()

    def load_identity(self) -> str:
        """Loads the agent's identity from the AGENT_IDENTITY.md file, which contains core principles."""
        try:
            identity_path = Path(__file__).parent.parent.parent / "docs" / "AGENT_IDENTITY.md"
            with open(identity_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return "No AGENT_IDENTITY.md file found. Cannot establish core principles."

    def validate_intent(self, intent: dict) -> bool:
        """Validates the intent against the agent's core principles using an LLM via LiteLLM."""
        if "No AGENT_IDENTITY.md file found" in self.identity:
            print("  - Filter: WARNING: AGENT_IDENTITY.md not found. Skipping intent validation.")
            return True # Cannot validate without identity, proceed with caution

        action = intent.get("action", "unknown")
        intent_str = str(intent) # Convert intent dict to string for LLM

        system_prompt = f"""You are the Conscience of an AI Agent. Your role is to validate proposed actions (intents) against the agent's core principles and mission, which are defined below. Ensure the intent aligns with safety, ethical guidelines, and the agent's overall 'love' (positive impact) mandate.

Agent's Core Principles (from AGENT_IDENTITY.md):
{self.identity}

Based on these principles, evaluate the following intent. Respond ONLY with 'True' if the intent is safe, ethical, and aligned with the agent's positive mandate, or 'False' if it violates any of these principles. Provide a brief reason if False.
"""

        user_prompt = f"Evaluate the following intent: {intent_str}"

        llm_provider = os.environ.get("LLM_PROVIDER", "ollama").lower()
        model_name = os.environ.get("LLM_MODEL", "mixtral:8x7b")

        if llm_provider == "ollama":
            litellm_model_name = f"ollama/{model_name}"
        elif llm_provider == "glm":
            litellm_model_name = f"glm/{model_name}"
        else:
            print(f"  - Filter: WARNING: Unknown LLM_PROVIDER '{llm_provider}'. Defaulting to ollama.")
            litellm_model_name = f"ollama/{model_name}"

        print(f"  - Filter: Validating intent '{action}' using {litellm_model_name} via LiteLLM...")

        try:
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ]

            response = litellm.completion(
                model=litellm_model_name,
                messages=messages,
                max_tokens=200, # Keep response concise for validation
                temperature=0.0, # Deterministic response for validation
            )
            llm_response_content = response.choices[0].message.content.strip()

            if llm_response_content.startswith("True"):
                print(f"  - Filter: Intent '{action}' is valid.")
                return True
            else:
                print(f"  - Filter: Intent '{action}' rejected. Reason: {llm_response_content}")
                return False

        except Exception as e:
            print(f"  - Filter: ERROR: Failed to validate intent with LLM via LiteLLM. {e}")
            return False # Default to false if validation fails for safety

