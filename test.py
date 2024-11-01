from transformers import AutoTokenizer,AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("Qwen2-VL-7B-Instruct-GPTQ-Int4")

for name,param in model.named_parameters():
    print(name)
