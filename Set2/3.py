
#Creaing class
class NewsStory:

#Consttructor
    def __init__(self, guid, title, description, link,update):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = update

#Creating required methods
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_link(self):
        return self.link
    def get_pubdate(self):
        return self.pubdate

#Creating object from class
obj1 = NewsStory('a1rt', 'Padma Bridge','Long description.', 'www.link.com','5/6/22')

#Printing out informations
print(obj1.get_guid())
print(obj1.get_title())
print(obj1.get_description())
print(obj1.get_link())
print(obj1.get_pubdate())