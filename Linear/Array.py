# Array
# 동적 배열 구현 
# Python에선 동적배열인 list가 내부적으로 구현(내장함수)되어 있다. 
a = list()
a = []

# Python에선 list에 대한 다양한 function, method가 구현되어 있다.
# 삽입(추가), 삭제(추출), 조회 구현 
list_test = [1, 2, 3]
 
# 시간 복잡도가 O(1)인 연산 
# 추가
# append -> 마지막 요소 추가 
list_test.append(elem)
# 추출
# pop -> 마지막 요소 추출
list_test.pop()
# 조회
# [i] -> 원하는 위치의 요소 값 반환
list_test[i]

# 시간 복잡도가 O(n)인 연산 
# 추가
# insert -> 원하는 위치에 요소 추가
list_test.insert(i, elem)
# 삭제
# del -> 원하는 위치의 요소 삭제
del list_test[i]
# 조회
# index ->  원하는 요소의 인덱스를 반환
list_test.index(elem)

