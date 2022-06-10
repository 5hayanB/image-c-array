from cv2 import imread, imshow, waitKey, destroyAllWindows


if __name__ == '__main__':
    img = imread('../pics/test.png')
    imshow('img', img)
    waitKey(0)
    destroyAllWindows()
