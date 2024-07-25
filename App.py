from flask import Flask, request, jsonify
from Search import binary_search
from Merge import merge_sort

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

video_titles.sort()

@app.route('/search', methods=['GET'])
def search_video():
    query = request.args.get('title')
    if not query:
        return jsonify({'error': 'Missing search query'}), 400
    
    index = binary_search(video_titles, query)
    
    if index != -1:
        return jsonify({'video': video_titles[index]}), 200
    else:
        return jsonify({'error': 'Video not found'}), 404

@app.route('/sort', methods=['GET'])
def sort_videos():
    sorted_videos = merge_sort(video_titles.copy())
    return jsonify({'sorted_videos': sorted_videos}), 200

if __name__ == '__main__':
    app.run(debug=True)
