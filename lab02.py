import datetime


class Post:
    def __init__(self, id, title, author, content):
        self.__id = id
        self.__title = title
        self.__author = author
        self.__content = content
        self.__comments = []
        self.__date = datetime.datetime.now()

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content

    @property
    def author(self):
        return self.__author

    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, comments):
        self.__comments.append(comments)

    @property
    def date(self):
        return self.__date

    def search(self, title):
        if self.__title == title:
            return self.__id
        else:
            return None

    def __str__(self):
        info = f'아이디 : {self.__id} \n제목: {self.__title}\n작성자 : {self.__author}\n작성일 : {self.__date}\n'
        info += f'글 내용 : {self.__content}\n'
        return info


class QnABoard:
    id = 0
    no_posts = 0

    def __init__(self):
        self.posts = []

    def add_post(self, title, author, contents):
        QnABoard.id += 1
        QnABoard.no_posts += 1
        new_post = Post(QnABoard.id, title, author, contents)
        self.posts.append(new_post)

    def get_post(self, title):
        for post in self.posts:
            if post.search(title):
                return post
        return None

    def remove_post(self, title):
        for post in self.posts:
            if post.search(title):
                QnABoard.no_posts -= 1
                self.posts.remove(post)
                return True

        return False

    def __str__(self):
        info = f'질의 응답 게시판 : 글 갯수 {QnABoard.no_posts}\n\n'
        for post in self.posts:
            info += f'{post}\n{80 * "-"}\n'
        return info
