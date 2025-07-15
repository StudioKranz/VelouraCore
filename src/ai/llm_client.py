# llm_client.py
"""
Client for OpenAI and local LLMs.
"""

class LLMClient:
    def __init__(self, openai_api_key=None, local_model_path=None):
        self.openai_api_key = openai_api_key
        self.local_model_path = local_model_path

    def chat_completion(self, prompt):
        """
        Placeholder for OpenAI chat completion.
        """
        # TODO: Integrate with OpenAI API
        pass

    def run_local_model(self, prompt):
        """
        Placeholder for local model inference.
        """
        # TODO: Integrate with local model
        pass
