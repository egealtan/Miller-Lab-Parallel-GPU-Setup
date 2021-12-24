# %%
from netrep.metrics import LinearMetric

# Rotationally invariant metric (fully regularized).
proc_metric = LinearMetric(alpha=1.0, center_columns=True)

# Linearly invariant metric (no regularization).
cca_metric = LinearMetric(alpha=0.0, center_columns=True)

# %%
# Given
# -----
# X : ndarray, (num_samples x num_neurons), activations from first network.
#
# Y : ndarray, (num_samples x num_neurons), activations from second network.
#
# metric : an instance of LinearMetric(...)

# Fit alignment transformations.
import numpy as np
X = np.arange(50).reshape(10,5)

Y = np.random.normal(0,5000,50)
Y = Y.reshape(10,5)

print(f"X.shape: {X.shape}")
print(f"Y.shape: {Y.shape}")

cca_metric.fit(X, Y)

# Evaluate distance between X and Y, using alignments fit above.
dist = cca_metric.score(X, Y)

print(f"Distance between X and Y is: {dist}")

cca_metric.fit(X, X)

# Evaluate distance between X and Y, using alignments fit above.
dist = cca_metric.score(X, X)

print(f"Distance between X and X is: {dist}")
# %%

# %%

# %%

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

# %%

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




# %%
