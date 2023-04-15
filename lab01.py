import datetime
class Post:
    def __init__(self, id, title, author, content):
        self.id = id           # 자동생성 되어야 함
        self.title = title
        self.author = author
        self.content = content
        self.comments = []
        self.date = datetime.datetime.now()

    def add_comments(self, comment):
        self.comments.append(comment)

    def get_comments(self):
        return self.comments

    def __str__(self):
        info = f'제목: {self.title}\n작성자 : {self.author}\n 작성일 : {self.date}\n'
        info += f'글 내용 : {self.content}\n'
        return info

class Board:
    def __init__(self, name):
        self.name = name
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def get_post(self, id):
        return self.posts[id - 1]

    def __str__(self):
        info = f'게시판 이름 : {self.name} \n'

        for post in self.posts:
            info += f'{post}\n'
        return info
 
if __name__ == "__main__":
    test_post = Post(1, '객체지향', '홍길동', '객체지향의 원리 중 추상화 설명')
    print(f'board 객체 : {test_post}')

    qna_board = Board('QnA Board')
    qna_board.add_post(test_post)
    print(qna_board)
