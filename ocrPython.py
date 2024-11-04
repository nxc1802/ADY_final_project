def generate_dictionary(a, b):
    key = f"background-position: -{a}px -{b}px"
    value = (b // 36) * 10 + (a // 36) + 1
    return {key: value}

# Tạo dictionary rỗng
my_dict = {}

# Sử dụng vòng lặp để thêm phần tử vào dictionary cho đến khi đạt 120 phần tử
# Đảm bảo `a` và `b` là các bội số của 36 nhưng bắt đầu từ giá trị 108 cho `a` và 216 cho `b` khi cần
count = 0
for b in range(0, 397, 36):
    for a in range(0, 325, 36):
        result = generate_dictionary(a, b)
        my_dict.update(result)
        count += 1

# Kiểm tra dictionary đã tạo ra
print(my_dict)

# Kiểm tra xem element cụ thể bạn mong đợi có trong dictionary hay không
print(my_dict.get('background-position: -108px -216px'))

# Lưu dictionary vào file
import json

with open('data.json', 'w') as f:
    json.dump(my_dict, f)

# Đọc dictionary từ file
with open('data.json', 'r') as f:
    data = json.load(f)
    print(data)
    