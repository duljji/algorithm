def dfs(level):
    # 1. 종료조건
    if level == len(stack):
        return True
    else:
        for j in range(1, 10):  # 1~9까지의 숫자 넣어보기
            r, c = stack[level]  # r번째행 c번째 열에 있는 0 채워주기
            if not r_check[r][j] and not c_check[c][j] and not s_check[r//3*3 + c//3][j]:
                sudoku[r][c] = j  # 0 채워넣고
                r_check[r][j] = True  # 모든 행과 열과 작은사각형 방문처리 해준 뒤
                c_check[c][j] = True
                s_check[r // 3 * 3 + c // 3][j] = True
                if dfs(level + 1):  # 다음 0 찾기(만약 찾아서 True 를 반환했으면 return True
                    return True
                else:  # 만약 다음 0을 못 찾고 돌아왔으면 다음 값을 넣어야하므로 모두 초기화
                    sudoku[r][c] = 0
                    r_check[r][j] = False
                    c_check[c][j] = False
                    s_check[r // 3 * 3 + c // 3][j] = False
    return False


T = int(input())

for tc in range(1, T + 1):
    # 1. 9개 행의 숫자 입력받기
    sudoku = [list(map(int, input())) for _ in range(9)]

    # 스도쿠에서 체크해야할 세가지
    r_check = [[False] * 10 for _ in range(9)]  # 가로 안에 들어갈 수 있는 숫자 체크하기 0~8번줄에 1~9까지의 숫자
    c_check = [[False] * 10 for _ in range(9)]  # 세로 안에 들어갈 수 있는 숫자 체크하기
    s_check = [[False] * 10 for _ in range(9)]  # 작은 사각형 안에 들어갈 수 있는 숫자 체크하기
    # 스도쿠에서 0인 곳 체크하기
    stack = []
    check = True
    # 스도쿠 돌면서 체크리스트 채워주기
    for i in range(9):
        for j in range(9):

            if r_check[i][sudoku[i][j]] == True or c_check[j][sudoku[i][j]] == True or s_check[i // 3 * 3 + j // 3][sudoku[i][j]] == True :
                check = False
                break
            if sudoku[i][j] != 0 :
                r_check[i][sudoku[i][j]] = True  # i행 숫자 체크
                c_check[j][sudoku[i][j]] = True  # j열 숫자도 체크
                # 작은 사각형은 i//3*3 + j//3 번째 사각형이 된다
                s_check[i // 3 * 3 + j // 3][sudoku[i][j]] = True
            if sudoku[i][j] == 0:  # 0이면 스택에 넣어주기
                stack.append((i, j))
    if dfs(0) and check :
        for i in sudoku :
            print("".join(map(str, i)))
    else :
        print("Could not complete this grid.")
    print()

