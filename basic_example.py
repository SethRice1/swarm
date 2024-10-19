# basic_example.py

from swarm import Swarm, Agent
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Swarm client
client = Swarm()

def transfer_to_agent_b():
    return agent_b

# Define Agent B
agent_b = Agent(
    name="Agent B",
    instructions="Only speak in Haikus.",
)

# Define Agent A with a function to transfer to Agent B
agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful agent.",
    functions=[transfer_to_agent_b],
)

# Run the Swarm with Agent A
response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "I want to talk to agent B."}],
)

# Print the response from Agent B
print(response.messages[-1]["content"])
