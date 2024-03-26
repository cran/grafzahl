import torch

def py_detect_cuda():
    return(torch.cuda.is_available())
