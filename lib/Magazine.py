
class Magazine:
  def __init__(self, name, category):    
    self._name = name
    self._category = category
    self._contributors = []

  def name(self):    
    return self._name

  def set_name(self, name):
    self._name = name

  def category(self):
    return self._category

  def set_category(self, category):
    self._category = category

  def contributors(self):
    return self._contributors
  
  def add_contributor(self, author):
    self._contributors.append(author)

  @staticmethod
  def all():
    return []
  
#Example

#Authors
author1 = Author("Chinua Achebe")
author2 = Author("John Kiarie")
author3 = Author("Abel Mutua")

#Magazine
magazine = Magazine("Click Click Bang", "Bare foot bandit")

#contributors to the magazine
magazine.add_contributor(author1)
magazine.add_contributor(author2)

#Get conributors to the magazine
contibutors = magazine.contributors()
for contributor in contibutors:
  print(contributor.name())
