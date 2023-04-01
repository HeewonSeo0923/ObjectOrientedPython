import datetime
class Post:
    def __init__(self, id, title, author, content):
        self.id = id
        self.title = title
        self.author = author
        self.content = content
        self.comments = []
        self.date = datetime.datetime.now()

    def add_comments(self):
        pass

    def get_comments(self):
        return self.comments

if __name__ == "__main__":
    test_post = Post(1, '객체지향', '홍길동', '객체지향의 원리 중 추상화 설명')
    print(f'board 객체 : {test_post}')
