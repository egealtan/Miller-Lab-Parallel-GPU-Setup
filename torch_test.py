# %%

import matplotlib.pyplot as plt
plt.plot([1,2,3],[2,3,5])
plt.show()


# %%

file1 = open("/workspaces/pytorch_setup_test/data_folder/data.txt","a")
file1.write("This line has been added in the devcontainer!")

file2 = open("/workspaces/pytorch_setup_test/data_folder/data2.txt","a")
file2.write("This file and the line line have been added in the devcontainer!")

file1.close()
file2.close()

aa = 3



# import torch
# import numpy as np
# print(torch.__version__)
# print('Hello World!')
# print(f'Cuda version?:{torch.version.cuda}')
# print(f'Cudnn version?:{torch.backends.cudnn.version()}')
# print(f'Cuda available?: {torch.cuda.is_available()}')
# print(f'Current device?: {torch.cuda.current_device()}')
# print(f'Device count?: {torch.cuda.torch.cuda.device_count()}')
# print(f'Device name?: {torch.cuda.get_device_name(0)}')

# aa = 3
# import tensorflow as tf
# print(tf.__version__)




# %%
