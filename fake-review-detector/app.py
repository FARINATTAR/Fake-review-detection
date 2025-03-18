from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from database import save_review, check_duplicate, check_user_spam
from review_checker import detect_template_review

app = Flask(__name__, template_folder="templates")  # Ensure templates folder is set
CORS(app)

@app.route('/')  # This serves the HTML page
def home():
    return render_template('index.html')  # Make sure "index.html" is inside "templates" folder

@app.route('/check_review', methods=['POST'])
def check_review():
    data = request.json
    user_id = data.get('user_id')
    review = data.get('review', "").lower()

    print(f"Received Review: {review} from User: {user_id}")  # Debugging print

    if check_duplicate(review):
        return jsonify({"status": "Fake", "message": "Duplicate Review Detected!"})

    if detect_template_review(review):
        return jsonify({"status": "Fake", "message": "Template-Based Fake Review Detected!"})

    if check_user_spam(user_id):
        return jsonify({"status": "Fake", "message": "User Posting Too Many Reviews!"})

    save_review(user_id, review)
    return jsonify({"status": "Genuine", "message": "Review Accepted!"})

if __name__ == '__main__':
    app.run(debug=True)
