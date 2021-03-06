# 5-2 사전
         #같은key 여러명이 쓰면 마지막 값으로 초기화됨        #정수가 아니라 str도 key가능
cabinet = {3:"홍명보", 3:"김철수", 3:"유재석", 100:"김태호", "A-3":"유재석2", "B-100":"김태호2"}  # 변수에 번호 지정해서 값을 지정해 놓을 수 있음.
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5])  # 비어있는 경우 에러발생.
print(cabinet.get(5))  # .get으로 하면 비어있어도 'None' 표시만 뜨고 뒤에줄 실행 됨.
print("hi")

print(cabinet.get(5, "사용 가능"))  # 없는 경우 get으로 만들 수 있다. : None -> "사용 가능"

print(3 in cabinet)  # True -> 3이라는 key가 cabinet에 있으면 True 출력
print(6 in cabinet)  # False

print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["C-20"] = "조세호"  # cabinet에 C-20이라는 값을 만들고 그 안에 "조세호"를 넣는다.
                            # 만약 C-20 이 사용중이라면 값이 업데이트가 됨
cabinet["A-3"] = "김종국"  # A-3의 "유재석"->"김종국"

# 간 손님
del cabinet["A-3"]  # A-3에 애당하는 값 지우기
print(cabinet)

# key 들만 출력
print(cabinet.keys())
# value 들만 출력
print(cabinet.values())
# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)