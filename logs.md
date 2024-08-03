error CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
this should be solved by doing: https://stackoverflow.com/a/76565262/14687545
>had to override trainer class to account for custom loss (because changed the model tokem embeddin dim) (claude response)
>4,4 (train,eval) batch size oom's on 2 t4 kaggle tpu's with rope scaling set to 4 (1024 to 8k)
>1,1(train,eval) also ooms
>scaling factor set to 2, Doesnt oom
