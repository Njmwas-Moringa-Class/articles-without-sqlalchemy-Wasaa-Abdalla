class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all_articles.append(self)

    def get_title(self):
        return self._title
    
    def author(self):
        return self._author
    
    def magazine(self):
        return self._magazine

    @classmethod
    def get_all_articles(cls):
        return cls.all_articles

class Author:
    def __init__(self, name):
        self.name = name

class Magazine:
    def __init__(self, name):
        self.name = name


# Create authors and magazines
author1 = Author("Alpha Likembe")
magazine1 = Magazine("Elnino Rains")

# Create articles
article1 = Article(author1, magazine1, "Government Strategies")
article2 = Article(author1, magazine1, "Weather Forecast")

# Get the title of an article
print(article1.get_title())  

# Get a list of all articles
all_articles = Article.get_all_articles()
for article in all_articles:
    print(article.get_title())


print(article1.author().name)
print(article1.magazine().name)