from functools import reduce
def flatten_array(array):
    """
    @params array, dim >=2
    @return new array, dim = dim - 1
    """
    def f(ac, arr):
        if(isinstance(arr, list)):
            ac.extend(arr)
        return ac
    return reduce(f ,array, [] )
