# -*- coding: utf-8 -*-
"""Untitled26.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j8Pq1e8EdeJYw-1HhmIpBgdbpFdNTMwl
"""

# Download image
!gdown 1i9dqan21DjQoG5Q_VEvm0LrVwAlXD0vB

!ls /content

import matplotlib.image as mpimg

img = mpimg.imread ("/content/dog.jpeg")
img

import numpy as np
def lightness_to_gray(img):
    # Tính giá trị max và min của các kênh màu
    max_color = np.max(img[..., :3], axis=-1)
    min_color = np.min(img[..., :3], axis=-1)
    # Tính giá trị xám
    gray_img = (max_color + min_color) / 2
    return gray_img

# Chuyển đổi ảnh màu sang ảnh xám
gray_img_01 = lightness_to_gray(img)

# In giá trị của pixel (0, 0)
print(gray_img_01[0, 0])

# Áp dụng phương pháp Average để chuyển đổi ảnh màu sang ảnh xám
import matplotlib.pyplot as plt
def average_to_gray(img):
    # Tính giá trị trung bình của các kênh màu
    gray_img = np.mean(img[..., :3], axis=-1)
    return gray_img

# Chuyển đổi ảnh màu sang ảnh xám
gray_img_02 = average_to_gray(img)

# Hiển thị ảnh xám
plt.imshow(gray_img_02, cmap='gray')
plt.axis('off')
plt.show()

# In giá trị của pixel (0, 0)
print(gray_img_01[0, 0])

def luminosity_to_gray(img):
    # Định nghĩa trọng số cho các kênh màu
    weights = [0.21, 0.72, 0.07]
    # Tính giá trị xám dựa trên trọng số
    gray_img = np.dot(img[..., :3], weights)
    return gray_img

gray_img_03 = luminosity_to_gray(img)

# Hiển thị ảnh xám
plt.imshow(gray_img_03, cmap='gray')
plt.axis('off')
plt.show()

# In giá trị của pixel (0, 0)
print(gray_img_03[0, 0])

! gdown 1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq

import pandas as pd
df = pd.read_csv("/content/advertising.csv")

data = df . to_numpy ()
pd.DataFrame(data)

df_from_numpy = pd.DataFrame(data)


new_column_names = ['TV', 'Radio', 'Newspaper', 'Sales']
df_from_numpy.columns = new_column_names

print(df_from_numpy)

# Tìm giá trị lớn nhất và chỉ mục của nó
max_value = data[:, 3].max()
max_index = data[:, 3].argmax()
print(f"Max: {max_value} - Index: {max_index}")

mean_tv = df['TV'].mean()
print(f"Giá trị trung bình của cột TV là: {mean_tv}")

count_sales = (df['Sales'] >= 20).sum()  # df[df['Sales'] >= 20]['Sales'].count()
print(f"Số lượng bản ghi có giá trị tại cột Sales lớn hơn hoặc bằng 20 là: {count_sales}")

# Tính giá trị trung bình của cột Radio khi giá trị cột Sales >= 15
mean_radio_condition = df[df['Sales'] >= 15]['Radio'].mean()
print(f"Giá trị trung bình của cột Radio khi giá trị cột Sales >= 15 là: {mean_radio_condition}")

# Tính giá trị trung bình của cột Newspaper
mean_newspaper = df['Newspaper'].mean()

# Tính tổng các hàng của cột Sales với điều kiện Newspaper > giá trị trung bình của Newspaper
total_sales_condition = df[df['Newspaper'] > mean_newspaper]['Sales'].sum()
print(f"Tổng các hàng của cột Sales với điều kiện Newspaper > giá trị trung bình của Newspaper là: {total_sales_condition}")

A = df['Sales'].mean()

# Tạo mảng scores dựa trên giá trị trung bình
def categorize_sales(value, avg):
    if value > avg:
        return "Good"
    elif value < avg:
        return "Bad"
    else:
        return "Average"

scores = df['Sales'].apply(lambda x: categorize_sales(x, A))

# In ra kết quả của scores[7:10]
print(scores[7:10].tolist())