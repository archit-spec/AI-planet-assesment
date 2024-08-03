Sure, let's format the logs in a cleaner way with proper sections and a table for easy readability.

---

# Training Logs

## Errors and Solutions

### Error: CUDA Kernel Errors
- **Description**: CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
- **Solution**: Follow the solution provided [here](https://stackoverflow.com/a/76565262/14687545).

### Custom Trainer Override
- **Reason**: Had to override the trainer class to account for custom loss (because changed the model token embedding dimension) (Claude response).

## Training Results

| Batch Size (Train, Eval) | Scaling Factor | Result     | Notes                                                                       |
|--------------------------|----------------|------------|-----------------------------------------------------------------------------|
| 4, 4                     | 4              | OOM        | Occurs on 2 T4 Kaggle TPUs with rope scaling set to 4 (1024 to 8k).          |
| 1, 1                     | 4              | OOM        | Out of memory even with the smallest batch size.                            |
| -                        | 2              | Doesn't OOM| Works fine with scaling factor set to 2.                                     |

---
