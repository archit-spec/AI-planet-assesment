
---

### Extending GPT-2 Context Length via RoPE Scaling
  note: ive chose gpt2 as its the only small model i could find that i could finetune easiy without ooming which was old enough to not have rope preimplemented (qlora was making it harder and giving too many errors so dint wanna go into that as time constrians)

#### Training Runs
- [Training Run 1 on WandB](https://wandb.ai/dumbal/huggingface/runs/omafkp4r?nw=nwuserdumbal)
- [Training Run 2 on WandB (this one is new im not using this model yet)](https://wandb.ai/dumbal/huggingface/runs/pivwo4nb?nw=nwuserdumbal)

#### Demo
- Try the model here: [GPT-2 Long Demo](https://huggingface.co/spaces/archit11/gpt2long)
- Try giving an input of >1k or 2k tokens
![Demo](./image.png)

#### Evaluation
- Not as good as expected: [RoPE Test Evaluation](https://github.com/kaiokendev/cutoff-len-is-context-len/blob/main/rope_test.ipynb)
 but...good enough! given the compute constrians! :D  


### Approach
- Use the rotatory pos implementation by lucid rains [here](https://github.com/lucidrains/rotary-embedding-torch)
- change the model to use rope pos embeddings 
- save and upload to huggingface (to not oom), the model can be found [here](https://huggingface.co/archit11/gpt2-long-finetuned)
- load and train seperately on [long-alpaca12k](https://huggingface.co/datasets/Yukang/LongAlpaca-12k) 
- these steps can be seen in [notebook](./final.ipynb) and [notebook](./gpt2long-train.ipynb) 
- for logs and other findings or docs check [logs](./pretier_log.md) and [this](./pretier_documentation.md)
---

