
import numpy as np

# Dữ liệu mẫu (đã được chuẩn bị trước)
movies = {
    'movie1': [1, 0, 1, 1, 0],
    'movie2': [0, 1, 1, 0, 1],
    'movie3': [1, 1, 0, 0, 1],
    'movie4': [0, 1, 0, 1, 0],
    'movie5': [1, 0, 1, 0, 0]
}

# Hàm tính toán độ tương đồng cosine giữa hai phim
def cosine_similarity(movie1, movie2):
    numerator = np.dot(movie1, movie2)  # Tính tích vô hướng giữa hai vectơ đặc trưng
    denominator = np.linalg.norm(movie1) * np.linalg.norm(movie2)  # Tính tích của độ dài hai vectơ đặc trưng
    return numerator / denominator if denominator != 0 else 0  # Trả về độ tương đồng cosine nếu mẫu khác 0, ngược lại trả về 0

# Hàm khuyến nghị dựa trên Content-based Filtering
def content_based_recommendation(movie, num_recommendations):
    similarity_scores = {}
    movie_features = movies[movie]
    
    # Tính toán độ tương đồng giữa phim hiện tại và các phim khác
    for other_movie in movies:
        if other_movie != movie:
            similarity_scores[other_movie] = cosine_similarity(movie_features, movies[other_movie])
    
    # Sắp xếp và trả về các phim có độ tương đồng cao nhất
    sorted_scores = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)
    recommendations = [movie for movie, _ in sorted_scores][:num_recommendations]
    return recommendations

# Sử dụng hàm khuyến nghị để đưa ra các gợi ý cho một phim
movie = 'movie1'
num_recommendations = 2
recommendations = content_based_recommendation(movie, num_recommendations)

print(f"Recommendations for {movie}:")
for i, movie in enumerate(recommendations, 1):
    print(f"{i}. {movie}")
    
