import os
# before keras imported
def choose_gpu(number):
  os.environ["CUDA_VISIBLE_DEVICES"]=str(number)
