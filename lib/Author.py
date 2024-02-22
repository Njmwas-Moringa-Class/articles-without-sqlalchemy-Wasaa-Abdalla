
class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        raise AttributeError("Cannot change author's name")

    def __str__(self):
        return self.name
    
    def add_article(self, magazine, title):
        article = Article(self, magazine, title)  # Return the created article
        return article

    def topic_areas(self):
        return list(set(article.magazine for article in self.magazine.articles))  # Fix this line

# Example usage:
author = Author("Wasaa Abdalla")

magazine1 = Magazine("Click click Bang")
author.add_article(magazine1, "Thug Life")
author.add_article(magazine1, "Ghetto life")

magazine2 = Magazine("Bandits")
author.add_article(magazine2, "Barefoot bandit")
author.add_article(magazine2, "Garissa attack")

# Trying to change the author's name will raise an exception:
try:
    author.name = "John Wick"
except AttributeError as e:
    print(e)

print("Author:", author)
print("Topic Areas:", author.topic_areas())