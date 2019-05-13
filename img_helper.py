def split_img_vertical(img, spliter_x):
    """
    @params img: img loaded by keras.preprocessing.image.load_img
    @params splitter_x: where to split
    @return (left_part_of_img, right_part_of_img)
    """
    shape = img.size
    imgl = img.crop(box=(*(0,0),*(spliter_x, shape[1]) ))
    imgr = img.crop(box=(*(spliter_x, 0),*shape ) )
    return imgl, imgr
