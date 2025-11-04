from pathlib import Path

class AgentMind:
    """The 'Ear' and 'Frontal Lobe'. Understands user intent."""

    def __init__(self):
        self.identity = self.load_identity()

    def load_identity(self) -> str:
        """Loads the agent's identity from the AGENT_IDENTITY.md file."""
        try:
            identity_path = Path(__file__).parent.parent.parent / "docs" / "AGENT_IDENTITY.md"
            with open(identity_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return "No identity file found."

    def understand_intent(self, prompt: str) -> str:
        """Uses the integrated LLM to understand the user's prompt."""
        import litellm
        import os

        llm_provider = os.environ.get("LLM_PROVIDER", "ollama").lower() # Default to ollama for local development
        model_name = os.environ.get("LLM_MODEL", "mixtral:8x7b") # Default model

        # LiteLLM expects model names in a specific format, e.g., "ollama/mixtral:8x7b" or "glm/glm-4.6"
        if llm_provider == "ollama":
            litellm_model_name = f"ollama/{model_name}"
        elif llm_provider == "glm":
            litellm_model_name = f"glm/{model_name}" # Assuming model_name is like "glm-4.6"
        else:
            print(f"  - WARNING: Unknown LLM_PROVIDER '{llm_provider}'. Defaulting to ollama.")
            litellm_model_name = f"ollama/{model_name}"

        print(f"  - Sending prompt to {litellm_model_name} via LiteLLM...")
        try:
            messages = [
                {"role": "system", "content": self.identity},
                {"role": "user", "content": prompt},
            ]
            
            response = litellm.completion(
                model=litellm_model_name,
                messages=messages,
                max_tokens=4096, # A reasonable default
                temperature=0.7, # Default temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"  - ERROR: Failed to communicate with LLM via LiteLLM. {e}")
            return f"Error: Failed to communicate with LLM via LiteLLM. {e}"

