from dataclasses import dataclass
from typing import List, Any
@dataclass
class AgentAction:
    tool: str
    query: str
@dataclass
class ActionFinish:
    llm_query: str

class Tool:
    def __init__(self,name,description):
        self.name = name
        self.description = description
    def execute(self,query):
        raise NotImplementedError("Subclasses must implement this method")
@dataclass
class IntermediateStep:
    list_step: List[Any]
    result: []

class Agent:
    def __int__(self,tools,llm,max_iterations:int):
        self.tools = tools
        self.llm = llm
        self.max_iterations = max_iterations
    def run(self,initial_prompt):
        current_state = initial_prompt
        current_step = None
        iteration = 0
        while True:
            current_step = self.generate_next_step()
            if isinstance(current_step.list_step[-1],ActionFinish):
                return current_step.result
            iteration +=1
            if iteration == self.max_iterations:
                return "I'm sorry. I don't know about your question"

    def generate_next_step(self,history):
        raise NotImplementedError("Subclasses must implement this method")