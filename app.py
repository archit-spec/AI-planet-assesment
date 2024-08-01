import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset
import torch

# Load the dataset
dataset = load_dataset("Yukang/LongAlpaca-12k", split='train[:10%]')

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")
model = AutoModelForCausalLM.from_pretrained("archit11/gpt2-long-finetuned")

# Add special tokens to the tokenizer
special_tokens = {
    'pad_token': '<pad>',
    'cls_token': '<s>',
    'sep_token': '</s>',
    'unk_token': '<unk>'
}
tokenizer.add_special_tokens(special_tokens)

# Resize token embeddings of the model
model.resize_token_embeddings(len(tokenizer))

# Verify the vocabulary sizes match
assert len(tokenizer) == model.config.vocab_size, "Tokenizer and model vocabulary sizes do not match."

# Define the inference function
def generate_text(instruction_index):
    text = dataset['instruction'][instruction_index]
    
    # Tokenize and prepare the input for the model
    tokenized_input = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        padding='max_length',
        truncation=True,
        max_length=5000,  # Adjust as needed
        return_tensors='pt'
    )

    input_ids = tokenized_input['input_ids']
    attention_mask = tokenized_input['attention_mask']

    # Generate text using the model
    model.eval()
    with torch.no_grad():
        outputs = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=50,  # Adjust as needed
            num_return_sequences=1
        )

    # Decode the generated text
    decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded_output

# Create the Gradio interface
interface = gr.Interface(
    fn=generate_text,
    inputs=gr.inputs.Slider(minimum=0, maximum=len(dataset)-1, step=1, label="Instruction Index"),
    outputs="text",
    title="GPT-2 Text Generation",
    description="Generate text based on the instruction at a specific index from the LongAlpaca-12k dataset."
)

# Launch the Gradio interface
interface.launch()

