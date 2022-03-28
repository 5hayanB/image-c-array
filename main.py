from cv2 import imread, resize, COLOR_BGR2GRAY, cvtColor
from sys import maxsize
from numpy import set_printoptions
from re import sub
set_printoptions(threshold=maxsize)

def c_arr_file(lst):
    for __ in lst:
        # Read image
        img_file = __[0]
        img_format = __[1]
        img = imread(f'pics/{img_file}.{img_format}')
        print(f"Original dimensions: {img.shape}")
        width = 300
        height = 300
        channels = 3
        dims = (width, height)
        
        # Resize image
        resized = resize(img, dims)
        print(f'Resized dimensions: {resized.shape}')
        
        # Convert to grayscale
        gray = cvtColor(resized, COLOR_BGR2GRAY)
        print(f'Grayscale dimensions: {gray.shape}')
        
        # Getting to c array
        c_arr = [hex(resized[i][j][k]) for i in range(width) for j in range(height) for k in range(channels)]
        for k in range(len(c_arr)):
            if len(c_arr[k]) == 3:
                lb = c_arr[k][-1]
                c_arr[k] = f'0x0{lb}'
        print(f'Length of c_arr: {len(c_arr)}')
        c_arr_str1 = f'#include "{img_file}.h"\n#include <cstdint>\n\nalignas(16) const uint8_t {img_file}_img[] = {c_arr};\nconst int {img_file}_img_len = {len(c_arr)};\n'
        c_arr_str2 = sub('\[', '{', c_arr_str1)
        c_arr_str3 = sub('\{', '[', c_arr_str2, count=1)
        c_arr_str4 = sub(']', '}', c_arr_str3)
        c_arr_str5 = sub('}', ']', c_arr_str4, count=1)
        c_arr_str = sub("'", "", c_arr_str5)

        # Getting header files
        arr_hdr = f'#include <cstdint>\n\nextern const uint8_t {img_file}_img[];\nextern const int {img_file}_img_len;'
        
        # Writing to c arrays
        with open(f'c_arrays/{img_file}.cc', 'w', encoding='UTF-8') as f:
            f.write(c_arr_str)
        
        # Writing to header files
        with open(f'c_arrays/{img_file}.h', 'w', encoding='UTF-8') as f:
            f.write(arr_hdr)
        
        # Test
        # with open('test.cc', 'w', encoding='UTF-8') as f:
        #     f.write(str(resized))

if __name__ == '__main__':
    img_list = [
        ['car1', 'jpeg'],
        ['car2', 'jpg'],
        ['car3', 'jpeg'],
        ['car4', 'jpeg'],
        ['car5', 'jpg'],
        ['hamza', 'jpeg'],
        ['no_person', 'jpg'],
        ['no_person1', 'jpeg'],
        ['no_person2', 'jpg'],
        ['no_person3', 'jpg'],
        ['no_person4', 'jpeg'],
        ['no_person5', 'png'],
        ['person', 'jpg'],
        ['person1', 'jpg'],
        ['person2', 'jpg'],
        ['person3', 'jpeg'],
        ['person4', 'jpeg'],
        ['person5', 'jpeg'],
        ['person6', 'jpg'],
        ['person7', 'jpeg'],
        ['person8', 'jpg'],
        ['person9', 'jpeg'],
        ['person10', 'jpg'],
        ['sir_farhan', 'jpeg'],
        ['space1', 'png'],
        ['space2', 'jpeg'],
        ['space3', 'jpeg'],
        ['space4', 'jpg']
    ]
    banana = [['banana', 'jpg']]
    masks = [['mask1', 'jpeg'], ['mask2', 'jpeg']]
    c_arr_file(banana)
