from pathlib import Path
import os

from langchain_openai import ChatOpenAI, OpenAI
import yaml
openai_key = "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"
def get_current_folder():
    return str(Path(__file__).parent)
def get_llm():
    os.environ["OPENAI_API_KEY"] = openai_key
    llm = OpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)
    return llm
def get_prompt(file_name):
    with open(get_current_folder()+f'/prompt_template/{file_name}.yaml',encoding="UTF-8") as f:
        prompt = yaml.safe_load(f)['prompt']
    return prompt

