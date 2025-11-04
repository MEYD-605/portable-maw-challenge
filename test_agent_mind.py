import os
import sys
from src.no1homelab.core.agent_mind import AgentMind

# Ensure environment variables are loaded for this script
# In a real scenario, direnv would handle this, but for testing, we can simulate.
# For this test, we assume the .env file has been manually sourced or variables are set.

print("--- Starting AgentMind GLM 4.6 Test ---")
print("--- Debugging Info ---")
print(f"Python executable: {sys.executable}")
print(f"sys.path: {sys.path}")
print(f"VIRTUAL_ENV: {os.environ.get('VIRTUAL_ENV')}")
print("----------------------")

# Instantiate AgentMind
agent_mind = AgentMind()

# Test prompt
user_prompt = "Hello, who are you?"

print(f"Sending prompt: \"{user_prompt}\" to AgentMind...")

# Call the understand_intent method
response = agent_mind.understand_intent(user_prompt)

print("--- AgentMind Response ---")
print(response)
print("--- Test Finished ---")

