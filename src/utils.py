from pathlib import Path
import os

from langchain_openai import ChatOpenAI, OpenAI
import yaml
openai_key = "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"
def get_current_folder():
    return str(Path(__file__).parent)
def get_llm():
    os.environ["OPENAI_API_KEY"] = openai_key
    llm = ChatOpenAI(model="gpt-4o",temperature=0)
    return llm
def get_prompt(file_name):
    with open(get_current_folder()+f'/prompt_template/{file_name}.yaml',encoding="UTF-8") as f:
        prompt = yaml.safe_load(f)['prompt']
    return prompt

