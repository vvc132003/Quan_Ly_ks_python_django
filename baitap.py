#bài 1
A = {
    "Toán": 6,
    "Văn": 8,
    "Sử": 9,
    "Địa": 7
}

#bài 1
maxdiem = max(A.values())
maxmonhoc = [s for s, c in A.items() if c == maxdiem]
print("Các điểm lớn nhất là:")
for s in maxmonhoc:
    print(f"{s}: {maxdiem}")


#bài 2
print(f"Môn có điểm cao nhất là: {maxmonhoc[0]} với điểm {maxdiem}")

#bài 3
sochan = [s for s in A.values() if s % 2 == 0]
print("Các điểm số chẵn là:")
for x in sochan:
    print(x)

#bài 4
trungbinh = sum(A.values()) / len(A)
print(f"Điểm trung bình của tất cả các môn là: {trungbinh}")

#bài 5
newa = {s: c for s, c in A.items() if c > 7}
print("Danh sách các môn có điểm lớn hơn 7 là:")
print(newa)



#bài 6
daonguoc = {v: k for k, v in A.items()}

print("Từ điển ban đầu:")
print(A)

print("Từ điển đảo ngược:")
print(daonguoc)