# -*- coding: utf-8 -*-
"""RecommendSystem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zHwhjGO40WtteVaewSHn1R9g2747-Ssr
"""

# import numpy as np

# # Dữ liệu mẫu (đã được chuẩn bị trước)
# movies = {
#     'movie1': [1, 0, 1, 1, 0],
#     'movie2': [0, 1, 1, 0, 1],
#     'movie3': [1, 1, 0, 0, 1],
#     'movie4': [0, 1, 0, 1, 0],
#     'movie5': [1, 0, 1, 0, 0]
# }

# # Hàm tính toán độ tương đồng cosine giữa hai phim
# def cosine_similarity(movie1, movie2):
#     numerator = np.dot(movie1, movie2)
#     denominator = np.linalg.norm(movie1) * np.linalg.norm(movie2)
#     return numerator / denominator if denominator != 0 else 0

# # Hàm khuyến nghị dựa trên Content-based Filtering
# def content_based_recommendation(movie, num_recommendations):
#     similarity_scores = {}
#     movie_features = movies[movie]
    
#     # Tính toán độ tương đồng giữa phim hiện tại và các phim khác
#     for other_movie in movies:
#         if other_movie != movie:
#             similarity_scores[other_movie] = cosine_similarity(movie_features, movies[other_movie])
    
#     # Sắp xếp và trả về các phim có độ tương đồng cao nhất
#     sorted_scores = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)
#     recommendations = [movie for movie, _ in sorted_scores][:num_recommendations]
#     return recommendations

# # Sử dụng hàm khuyến nghị để đưa ra các gợi ý cho một phim
# movie = 'movie1'
# num_recommendations = 2
# recommendations = content_based_recommendation(movie, num_recommendations)

# print(f"Recommendations for {movie}:")
# for i, movie in enumerate(recommendations, 1):
#     print(f"{i}. {movie}")

# Dữ liệu phim (tên phim và thể loại)
movies = {
    'Phim 1': ['Hành động', 'Phiêu lưu'],
    'Phim 2': ['Tình cảm', 'Lãng mạn'],
    'Phim 3': ['Hài', 'Tâm lý'],
    'Phim 4': ['Khoa học viễn tưởng', 'Phiêu lưu'],
    'Phim 5': ['Hành động', 'Tâm lý'],
    'Phim 6': ['Tình cảm', 'Lãng mạn'],
    'Phim 7': ['Hài', 'Tâm lý']
}

# Hàm gợi ý phim tương tự dựa trên thể loại
def recommend_movies(movie, n):
    movie_genres = movies[movie]  # Lấy thể loại của phim đầu vào
    recommendations = []  # Danh sách phim gợi ý
    
    # Duyệt qua tất cả các phim và tìm các phim có thể loại tương tự
    for title, genres in movies.items():
        if title != movie:
            common_genres = set(movie_genres) & set(genres)  # Tìm các thể loại chung
            similarity = len(common_genres) / len(movie_genres)  # Tính độ tương đồng
            recommendations.append((title, similarity))
    
    # Sắp xếp danh sách gợi ý theo độ tương đồng giảm dần
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    # Trả về n phim có độ tương đồng cao nhất
    return recommendations[:n]

# Gợi ý 3 phim tương tự với phim "Phim 3"
recommended_movies = recommend_movies('Phim 3', 5);
print(recommended_movies);
# In kết quả gợi ý
for movie, similarity in recommended_movies:
    print(movie)