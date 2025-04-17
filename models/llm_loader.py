# models/llm_loader.py
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

class LLMEngine:
    def __init__(self, model_name: str, device: str = None):
        self.model_name = model_name
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = None
        self.model = None
        self.generator = None

    def load(self):
        print(f"🔧 Loading LLM: {self.model_name} on {self.device}")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            device_map="auto" if self.device == "cuda" else None,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
        )
        self.generator = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device=0 if self.device == "cuda" else -1
        )

    def generate(self, prompt: str, max_new_tokens: int = 256) -> str:
        if not self.generator:
            raise ValueError("❌ LLM not loaded. Call load() first.")
        outputs = self.generator(prompt, max_new_tokens=max_new_tokens, do_sample=True)
        return outputs[0]["generated_text"]