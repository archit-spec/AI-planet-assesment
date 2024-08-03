# DAY 1
Here is the query rewritten with links and all the context lengths:

## Project TODO:
1. Extend context length good contendors:
   - [TinyLLaMA 1B](https://huggingface.co/yahma/tiny-llama-1b) (4096 ctx length)
   - [OpenELM 1B](https://arxiv.org/pdf/2404.14619.pdf) (1024 ctx length)
   - [Danube 1B](https://github.com/danube-ai/danube) (8192 ctx length)
   
2. Generate a chain-of-thought (CoT) dataset leveraging the high context window

The key points are:

- TinyLLaMA 1B, OpenELM 1B, Danube 1B, Mistral-7B, GPT-3.5-Turbo, Mamba, and Recurrent Memory Transformers (RMT) are good candidates for extending context length
- OpenELM 1B has a maximum context length of 1024 tokens, while Danube 1B supports up to 8192 tokens
- Mistral-7B and GPT-3.5-Turbo have context lengths of 32K and 16K tokens respectively
- Generating a chain-of-thought dataset can leverage the high context window capabilities of these models

Huge inspiration comes from this blog [kaiokendev rope impl](https://kaiokendev.github.io/til) 
Now coming increasing ctx len im gonna be using this application of 



# Actually scrap those top models off, they alr have rotatry pos encoding enabled by default we will do it for gpt-2



https://x.com/KarelDoostrlnck/status/1724991014207930696 from this source 
we will build our dataset
https://colab.research.google.com/drive/1CpsOiLiLYKeGrhmq579_FmtGsD5uZ3Qe#scrollTo=kqXyOOZZashX

RN using LIMA to train 

## After 5 try's on full finetuning and oom'ing im gonna try qlora


>got finetuned but incoherrent maybe i should try llama instead of gpt2

# Day 2
https://github.com/kaiokendev/cutoff-len-is-context-len/blob/main/util/dope_llama_monkey_patch.py

https://github.com/kaiokendev/cutoff-len-is-context-len
extending gpt2 ctx len via rope scaling
training run -> https://wandb.ai/dumbal/huggingface/runs/omafkp4r?nw=nwuserdumbal
this supposedly failed for obvious reasons probably
ok wow i should try this with the 8b param https://x.com/_xjdr/status/1819401339568640257


# day 3 

 ## clear steps:
   - apply monkey patch for rope embeddings
   - add eos token as pad token (gpt2 tokenizer doesnt have it by default) + increase lm_head size by one because vocab increased by 1 
   - format and tokenize long alpaca for training
   - pass model + data to trainer
   - train?


   alt method:
   - monkey patch and and change config and upload the model to hf (override pretrainedconfig class in config.py)
   - directly download and train with trainer api 
