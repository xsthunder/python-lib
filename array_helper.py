def flatten_array(array):
    def f(ac, arr):
        if(isinstance(arr, list)):
            ac.extend(arr)
        return ac
    return reduce(f ,array, [] )
