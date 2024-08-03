
---

# DAY 1

## Project TODO
1. Extend context length with good contenders:
   - [TinyLLaMA 1B](https://huggingface.co/yahma/tiny-llama-1b) (4096 ctx length)
   - [OpenELM 1B](https://arxiv.org/pdf/2404.14619.pdf) (1024 ctx length)
   - [Danube 1B](https://github.com/danube-ai/danube) (8192 ctx length)

2. Generate a chain-of-thought (CoT) dataset leveraging the high context window.

### Key Points:
- **TinyLLaMA 1B**, **OpenELM 1B**, **Danube 1B**, **Mistral-7B**, **GPT-3.5-Turbo**, **Mamba**, and **Recurrent Memory Transformers (RMT)** are good candidates for extending context length.
- **OpenELM 1B** has a maximum context length of 1024 tokens, while **Danube 1B** supports up to 8192 tokens.
- **Mistral-7B** and **GPT-3.5-Turbo** have context lengths of 32K and 16K tokens respectively.
- Generating a chain-of-thought dataset can leverage the high context window capabilities of these models.

Huge inspiration comes from this blog: [kaiokendev rope implementation](https://kaiokendev.github.io/til).

### Note:
- Actually, scrap those top models off, they already have rotary position encoding enabled by default. We will do it for GPT-2.
- [Source](https://x.com/KarelDoostrlnck/status/1724991014207930696): We'll build our dataset from this.
- [Colab Notebook](https://colab.research.google.com/drive/1CpsOiLiLYKeGrhmq579_FmtGsD5uZ3Qe#scrollTo=kqXyOOZZashX): Current work.

### Current Training:
- Using LIMA to train.
- After 5 tries on full fine-tuning and OOM'ing, I'm going to try QLoRA.

> Got fine-tuned but incoherent, maybe I should try LLaMA instead of GPT-2.

# DAY 2

### References:
- [Monkey Patch Script](https://github.com/kaiokendev/cutoff-len-is-context-len/blob/main/util/dope_llama_monkey_patch.py)
- [GitHub Repository](https://github.com/kaiokendev/cutoff-len-is-context-len)
- Extending GPT-2 context length via rope scaling:
  - [Training Run](https://wandb.ai/dumbal/huggingface/runs/omafkp4r?nw=nwuserdumbal): This supposedly failed for obvious reasons.
  - Should try with the 8B parameter: [Source](https://x.com/_xjdr/status/1819401339568640257).

# DAY 3

## Clear Steps:
1. Apply monkey patch for rope embeddings.
2. Add EOS token as pad token (GPT-2 tokenizer doesn't have it by default) and increase lm_head size by one because the vocab increased by 1.
3. Format and tokenize long Alpaca for training.
4. Pass model and data to the trainer.
5. Train?

### Alternative Method:
1. Monkey patch and change config and upload the model to Hugging Face (override PretrainedConfig class in config.py).
2. Directly download and train with Trainer API.

---
