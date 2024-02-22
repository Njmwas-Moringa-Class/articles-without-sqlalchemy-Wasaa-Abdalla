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


# Create authors and magazines
author1 = "Alpha Likembe"
magazine1 ="Elnino Rains"

# Create articles
article1 = Article(author1, magazine1, "Government Strategies")
article2 = Article(author1, magazine1, "Weather Forecast")

# Get the title of an article
print(article1.get_title())  

# Get a list of all articles
all_articles = Article.get_all_articles()
for article in all_articles:
    print(article.get_title())


print(article1.author)
print(article1.magazine)