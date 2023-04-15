from lab02 import QnABoard, Post

board = QnABoard()
board.add_post('객체지향의 원리', '홍길동', '객체지향의 원리 중 추상화에 대해 구체적인 예를 통해 설명해주세요')
board.add_post('파이썬 언어', '홍길순', '파이썬 언어가 다른 프로그래밍 언어에 비해 보편화된 이유는 무엇인가요?')

print(board)
board.remove_post('파이썬 언어')
print(board)