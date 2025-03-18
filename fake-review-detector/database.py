from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.fake_review_db
reviews_collection = db.reviews

def save_review(user_id, review):
    """ Save review to MongoDB """
    reviews_collection.insert_one({"user_id": user_id, "review": review})
    print(f"✅ Review saved for user {user_id}")

def check_duplicate(review):
    """ Check if the review already exists in MongoDB """
    print(f"🔍 Checking for duplicate review: {review}")
    return reviews_collection.find_one({"review": review}) is not None

def check_user_spam(user_id):
    """ Check if user has posted more than 5 reviews """
    user_review_count = reviews_collection.count_documents({"user_id": user_id})
    print(f"🔍 User {user_id} has posted {user_review_count} reviews")
    return user_review_count > 5  # Flag user if more than 5 reviews
