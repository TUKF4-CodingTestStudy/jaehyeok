# 베스트셀러 https://www.acmicpc.net/problem/1302

n = int(input())
books = {}

for i in range(n):
    book = input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1
target = max(books.values())
array = []

for book, number in books.items():
    if number == target:
        array.append(book)
print(sorted(array)[0])

# 딕셔너리에서 최댓값을 찾고 그 값과 같은 값을 가진 책들을 리스트에 넣어주고 정렬해주는 것이 포인트이다.
