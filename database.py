class Product():
    def __init__(self):
        pass

class Book(Product):
    def __init__(self):
        pass

class Item:
    def __init__(self, number, question, answer, choices):
        self.__done = False
        self.__number = number
        self.__question = question
        self.__answer = answer
        self.__choices = choices
        self.__correctness = False
        
    @property
    def answer(self):
        return self.__answer
        
    @property
    def doness(self):
        return self.__done
        
    @property
    def question(self):
        return self.__question
    
    @property
    def choices(self):
        return self.__choices
    
    @property
    def correctness(self):
        return self.__correctness
        
    @property
    def number(self):
        return self.__number
        
    def select_choice(self, choice):
        self.__done = True
        if choice == self.__answer:
            self.__correctness = True
        else:
            self.__correctness = False
    
class Exam:
    def __init__(self, title, id):
        self.__id = id
        self.__doness = 0
        self.__score = 0
        self.__title = title
        self.__items = []
        
    @property
    def title(self):
        return self.__title
    
    @property
    def id(self):
        return self.__id
    
    @property
    def items(self):
        return self.__items
    
    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        self.__score = value
        
    def add_item(self, item : Item):
        self.__items.append(item)
        
    def take_exam(self, number):
        for item in self.__items:
            if item.number == number:
                return item
    
    def grade(self):
        for item in self.__items:
            if item.correctness:
                self.__score += 1
        print(f"Your score is {self.__score}")
        
    def add_item(self, item : Item):
        self.__items.append(item)
    
    def doness(self):
        self.__doness = 0
        for item in self.__items:
            if item.doness:
                self.__doness += 1
        return self.__doness / len(self.__items)
    
    
    
class User:
    def __init__(self):
        pass
    
class Video:
    def __init__(self, title, id, path):
        self.__title = title
        self.__id = id
        self.__path = path
        
    @property
    def title(self):
        return self.__title
    
    @property
    def id(self):
        return self.__id
    
    @property
    def path(self):
        return self.__path
    
class Course:
    def __init__(self, title, id, price):
        self.__video = []
        self.__title = title
        self.__price = price
        self.__id = id
        self.__exam = []
        
    @property
    def title(self):
        return self.__title
    
    @property
    def id(self):
        return self.__id
    
    @property
    def video(self):
        return self.__video
    
    @property
    def exam(self):
        return self.__exam
    
    
    def add_video(self, value : Video):
        self.__video.append(value)
        
    def search_exam(self, exam_id):
        for exam in self.__exam:
            if exam_id == exam.id:
                return exam
        return None
        
    def search_video(self, title):
        for video in self.__video:
            if video.title == title:
                return video
        return None
    
    def add_exam(self, exam : Exam):
        self.__exam.append(exam)


class Platform:
    def __init__(self):
        self.__course = []
        self.__user = []
        
    @property
    def user(self):
        return self.__user
    
    @property
    def course(self):
        return self.__course
    
    def search_course(self, id):
        for course in self.__course:
            if course.id == id:
                return course
        return None
        
    def search_user(self, id):
        for user in self.__user:
            if user.id == id:
                return user
        return None
        
    def add_user(self, value : User):
        self.__user.append(value)
        
    def add_course(self, value : Course):
        self.__course.append(value)
        

app = Platform()

def set_initial_data():
    course1 = Course("Python", "1", 1000)
    vids1 = Video("Python Programing", "1", "vids/video1.mp4")
    vids2 = Video("Object Orient Programming", "2", "vids/video2.mp4")
    exam1 = Exam("Python Programming Quiz", "1")
    exam1.add_item(Item(1, "What is the output of 2 + 2?", "4", ["2", "3", "4", "5"]))
    exam1.add_item(Item(2, "What is the output of 2 * 2?", "4", ["2", "3", "4", "5"]))
    exam1.add_item(Item(3, "What is the output of 2 / 2?", "1", ["0", "1", "2", "3"]))
    exam1.add_item(Item(4, "What is the output of 2 - 2?", "0", ["0", "1", "2", "3"]))
    exam1.add_item(Item(5, "What is the output of 2 ** 2?", "4", ["2", "3", "4", "5"]))
    
    course1.add_video(vids2)
    course1.add_video(vids1)
    course1.add_exam(exam1)
    
    app.add_course(course1)
    

    
set_initial_data()