import matplotlib.pyplot as plt
import numpy as np

# Dữ liệu mẫu ngẫu nhiên (giả định thời gian thực hiện cho từng giai đoạn)
data = [
    np.random.randint(5, 20, size=50),  # Giai đoạn 1
    np.random.randint(10, 25, size=50),  # Giai đoạn 2
    np.random.randint(8, 18, size=50),  # Giai đoạn 3
    np.random.randint(15, 30, size=50),  # Giai đoạn 4
    np.random.randint(7, 22, size=50),  # Giai đoạn 5
    np.random.randint(12, 28, size=50),  # Giai đoạn 6
    np.random.randint(10, 25, size=50),  # Giai đoạn 7
    np.random.randint(5, 15, size=50)  # Giai đoạn 8
]

# Tên của người thực hiện theo từng giai đoạn
nguoi_thuc_hien = [
    "Nguyễn Đặng Thảo Uyên",  # Giai đoạn 1
    "Nguyễn Đặng Thảo Uyên",  # Giai đoạn 2
    "Nguyễn Đặng Thảo Uyên",  # Giai đoạn 3
    "Nguyễn Bảo Ngọc",  # Giai đoạn 4
    "Võ Văn Chính, Nguyễn Bảo Ngọc",  # Giai đoạn 5
    "Đỗ Quang Duy",  # Giai đoạn 6
    "Nguyễn Đặng Thảo Uyên",  # Giai đoạn 7
    "Võ Văn Chính"  # Giai đoạn 8
]

# Tạo biểu đồ
plt.figure(figsize=(10, 6))

# Vẽ biểu đồ boxplot với các tùy chỉnh
box = plt.boxplot(data, patch_artist=True, showmeans=True)
colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightpink', 'lightcoral', 'lightsalmon', 'lightcyan', 'lightgray']

# Tùy chỉnh màu sắc cho từng giai đoạn
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Đặt tên cho trục và biểu đồ
plt.title('Biểu đồ Boxplot cho 8 giai đoạn')
plt.xlabel('Giai đoạn')
plt.ylabel('Thời gian thực hiện (ngày)')
plt.xticks(ticks=np.arange(1, 9), labels=["Giai đoạn 1", "Giai đoạn 2", "Giai đoạn 3", "Giai đoạn 4",
                                         "Giai đoạn 5", "Giai đoạn 6", "Giai đoạn 7", "Giai đoạn 8"])

# Hiển thị grid và biểu đồ
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Ghi tên người thực hiện lên biểu đồ
for i, txt in enumerate(nguoi_thuc_hien):
    plt.text(i + 1, max(data[i]), txt, horizontalalignment='center', verticalalignment='bottom', color='black', weight='bold')

plt.tight_layout()
plt.show()
