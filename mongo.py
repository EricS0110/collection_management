from pymongo import MongoClient

class CollectionConnection:
    """This is a class to handle the collection operations with MongoDB Atlas instance"""
    def __init__(self, user: str, pwd: str, cluster: str, database: str):
        self.username = user
        self.password = pwd
        self.cluster = cluster
        self.database = database
        self.client = MongoClient(f'mongodb+srv://{self.username}:{self.password}'
                                  f'@{self.cluster}.rs3leio.mongodb.net')
        self.db = self.client[f'{database}']

    def add_book(self, book_data: dict):
        collection = self.db['books']
        book_filter = {"Title": book_data['Title'], "Author": book_data['Author'], "ISBN": book_data['ISBN'],
                       "Year": book_data['Year'], "Edition": book_data['Edition'],
                       "Condition": book_data['Condition']}
        collection.update_one(filter=book_filter, update={"$set": book_data}, upsert=True)
        return 200

    def add_comic(self, comic_data: dict):
        collection = self.db['comics']
        comic_filter = {"Title": comic_data['Title'], "Issue": comic_data['Issue'],
                        "Issue_Month": comic_data['Issue_Month'], "Issue_Year": comic_data['Issue_Year'],
                        "UPC": comic_data['UPC']}
        collection.update_one(filter=comic_filter, update={"$set": comic_data}, upsert=True)
        return 200

    def add_music(self, music_data: dict):
        collection = self.db['music']
        music_filter = {"Album": music_data['Album'], "Artist": music_data['Artist'], "Year": music_data['Year'],
                        "Disc_Number": music_data['Disc_Number'], "Disc_Count": music_data['Disc_Count'],
                        "Format": music_data['Format'], "Genre": music_data['Genre']}
        collection.update_one(filter=music_filter, update={"$set": music_data}, upsert=True)
        return 200

    def add_movie(self, movie_data: dict):
        collection = self.db['movies']
        movie_filter = {"Title": movie_data['Title'], "Year": movie_data['Year'],
                        "Disc_Format": movie_data['Disc_Format'], "Disc_Number": movie_data['Disc_Number'],
                        "Disc_Count": movie_data['Disc_Count']}
        collection.update_one(filter=movie_filter, update={"$set": movie_data}, upsert=True)
        return 200

    def add_television(self, television_data: dict):
        collection = self.db['television']
        television_filter = {"Title": television_data['Title'], "Year": television_data['Title'],
                             "Season": television_data['Season'], "Disc_Number": television_data['Disc_Number'],
                             "Disc_Count": television_data['Disc_Count'], "Disc_Format": television_data['Disc_Format'],
                             "Genre": television_data['Genre']}
        collection.update_one(filter=television_filter, update={"$set": television_data}, upsert=True)
        return 200
