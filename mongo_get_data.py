import pymongo
import pandas as pd

# MongoDB connection URI (Replace with your actual URI)
mongo_uri =

# Connect to MongoDB
client = pymongo.MongoClient(mongo_uri)

# Select database and collection
db = client["mongodbVSCodePlaygroundDB"]  # Replace with your database name
collection = db["food_nutrition"]  # Replace with your collection name

# Fetch data (convert cursor to list of dictionaries)
data = list(collection.find())

# Convert to Pandas DataFrame
df = pd.DataFrame(data)

# Drop MongoDB default '_id' field if not needed
df.drop(columns=['_id'], inplace=True, errors='ignore')

# Display the DataFrame
print(df)
