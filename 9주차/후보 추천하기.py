# 1713번

def solution():
    n = int(input().strip())  # 게시할 수 있는 최대 후보 수
    candidate = int(input().strip())  # 추천 횟수
    votes = list(map(int, input().split()))  # 추천받은 학생 목록

    frame = []  # 게시판에 올라간 후보 리스트
    vote_count = []  # 각 후보의 추천 수 리스트

    for student in votes:
        if student in frame:  # 이미 게시판에 있는 경우
            vote_count[frame.index(student)] += 1  # 추천 수 증가
        else:
            if len(frame) >= n:  # 게시판이 가득 찬 경우
                # 최소 추천 수를 가진 후보 인덱스 찾기, 같은 후보가 여러명이면 index(min)은 가장 먼저 등장한 최소값을 반환
                min_idx = vote_count.index(min(vote_count))  
                del frame[min_idx]  # 게시판에서 삭제
                del vote_count[min_idx]  # 추천 수도 삭제
            
            frame.append(student)  # 새로운 학생 추가
            vote_count.append(1)  # 추천 수 1로 초기화

    print(" ".join(map(str, sorted(frame))))  # 최종 후보들을 오름차순 정렬 후 출력

solution()
