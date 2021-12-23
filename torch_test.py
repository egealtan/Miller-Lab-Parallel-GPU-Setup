
import torch
import numpy as np
print(torch.__version__)
print('Hello World!')

print(f'Cuda version?:{torch.version.cuda}')
print(f'Cudnn version?:{torch.backends.cudnn.version()}')
print(f'Cuda available?: {torch.cuda.is_available()}')
print(f'Current device?: {torch.cuda.current_device()}')
print(f'Device count?: {torch.cuda.torch.cuda.device_count()}')
print(f'Device name?: {torch.cuda.get_device_name(0)}')