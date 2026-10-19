class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = 0
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if isinstance(number_of_pages, int) and not isinstance(number_of_pages, bool) and number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive.")

    def display_info(self):
        super().display_info()
        print(f"Number of Pages: {self.__number_of_pages}")


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = 0
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if isinstance(issue_number, int) and not isinstance(issue_number, bool) and issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive.")

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.__issue_number}")


pub1 = Publication("The Psychology of Learning", "John Smith")
pub2 = Publication("Introduction to Science", "Maria Santos")

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Noli Me Tangere", "Jose Rizal", 480)

mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Science Monthly", "Science Editors", 15)


print("PUBLICATION 1")
pub1.display_info()

print("\nPUBLICATION 2")
pub2.display_info()


print("\nBOOK 1")
book1.display_info()

print("\nBOOK 2")
book2.display_info()


print("\nMAGAZINE 1")
mag1.display_info()

print("\nMAGAZINE 2")
mag2.display_info()


print("\nDATA VALIDATION TESTS")
book1.set_number_of_pages(-310)
mag1.set_issue_number(0)

print("\nBook's number of pages:", book1.get_number_of_pages())
print("Magazine's issue number:", mag1.get_issue_number())
