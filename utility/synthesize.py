import cv2
import os
import numpy as np


origin_images_path = r'D:\Projects\Models\test_images_folder'

new_images_path = r'D:\Projects\Models\test_images_result'

origin_images = os.listdir(origin_images_path)

new_images = os.listdir(new_images_path)

origin_images_list = ['0.png', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png']
new_images_list = ['overlap_0z.png', 'overlap_1z.png', 'overlap_2z.png', 'overlap_3z.png', 'overlap_4z.png', 'overlap_5z.png', 'overlap_6z.png', 'overlap_7z.png', 'overlap_8z.png']
new_images_list1 = ['overlap_0.png', 'overlap_1.png', 'overlap_2.png', 'overlap_3.png', 'overlap_4.png', 'overlap_5.png', 'overlap_6.png', 'overlap_7.png', 'overlap_8.png']
new_dic = zip(origin_images_list,new_images_list1,new_images_list)


synthesized = r'D:\Projects\Models\synthesized'
if not os.path.exists(synthesized):
    os.mkdir(synthesized)
# new_dict = dict(new_dic)
new_image_name_prefix = "Original_ResNet_Res2Net_"
for k,v,j in new_dic:
    print(k,v,j)
    origin_image_path = os.path.join(origin_images_path,k)
    new_iamge_path1 = os.path.join(new_images_path,v)
    new_iamge_path = os.path.join(new_images_path,j)

    origin_image = cv2.imread(origin_image_path)
    new_image1 = cv2.imread(new_iamge_path1)
    new_image = cv2.imread(new_iamge_path)

    result = np.hstack([origin_image,new_image1,new_image])

    new_image_name = new_image_name_prefix + str(k)
    result_path = os.path.join(synthesized,new_image_name)
    print(result_path)
    cv2.imwrite(result_path,result)