import pymongo

# open the MongoDB connection
conn = pymongo.MongoClient('mongodb://localhost:27017')

# print the available MongoDB database
databases = conn.database_names()
for database in databases:
	print(database)

# Close the MongoDB connection
conn.close()