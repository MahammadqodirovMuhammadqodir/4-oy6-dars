# from collections import namedtuple

# # Masala 1: 
# Car = namedtuple('Car', ['brand', 'model', 'year', 'price'])

# cars = [
#     Car('Tesla', 'Model 3', 2021, 50000),
#     Car('Toyota', 'Corolla', 2022, 20000),
#     Car('BMW', 'X5', 2019, 55000),
#     Car('Audi', 'A4', 2023, 35000)
# ]

# print("Mashinalar (2020-yildan keyin chiqarilgan):")
# for car in cars:
#     if car.year > 2020:
#         print(f"Brand: {car.brand}, Model: {car.model}, Year: {car.year}, Price: {car.price}")

# # Masala 2: 
# Player = namedtuple('Player', ['name', 'position', 'score'])

# players = [
#     Player('Ali', 'Hujumchi', 95),
#     Player('Vali', 'Himoyachi', 85),
#     Player('Guli', 'Hujumchi', 90),
#     Player('Samar', 'Himoyachi', 88),
#     Player('Diyor', 'Hujumchi', 92)
# ]

# top_player = max(players, key=lambda player: player.score)
# print(f"\nEng yuqori natija: {top_player.name} ({top_player.position}) - {top_player.score} ball")

# # Masala 3: 
# Book = namedtuple('Book', ['title', 'author', 'year', 'price'])

# books = [
#     Book('Kitob A', 'Muallif A', 2018, 20),
#     Book('Kitob B', 'Muallif B', 2021, 30),
#     Book('Kitob C', 'Muallif C', 2022, 15)
# ]

# total_price = sum(book.price for book in books if book.year > 2015)
# print(f"\nKitoblar narxi: ${total_price}")

# # Masala 4: 
# Employee = namedtuple('Employee', ['name', 'position', 'salary', 'experience'])

# employees = [
#     Employee('Vali', 'Dasturchi', 4000, 6),
#     Employee('Guli', 'Boshqaruvchi', 6000, 8),
#     Employee('Samar', 'Analitik', 3500, 3),
#     Employee('Diyor', 'Dasturchi', 4500, 4)
# ]

# print("\nTajribali ishchilar:")
# for employee in employees:
#     if employee.experience > 5:
#         print(f"{employee.name} - Tajriba: {employee.experience} yil")

# highest_salary_employee = max(employees, key=lambda employee: employee.salary)
# print(f"Eng yuqori maosh: {highest_salary_employee.name} (${highest_salary_employee.salary})")

# # Masala 5: 
# Competition = namedtuple('Competition', ['team', 'points'])

# competitions = [
#     Competition('Team A', 85),
#     Competition('Team B', 75),
#     Competition('Team C', 80),
#     Competition('Team D', 90)
# ]

# best_team = max(competitions, key=lambda competition: competition.points)
# print(f"\nEng kuchli jamoa: {best_team.team} - {best_team.points} ochko")

# # Masala 6: 
# Weather = namedtuple('Weather', ['city', 'temperature', 'humidity'])

# weathers = [
#     Weather('Toshkent', 30, 60),
#     Weather('Samarqand', 27, 55),
#     Weather('Buxoro', 20, 70)
# ]

# print("\nIssiq shaharlar:")
# for weather in weathers:
#     if weather.temperature > 25:
#         print(f"{weather.city} - {weather.temperature}°C")

# # Masala 7: 
# Student = namedtuple('Student', ['name', 'math_score', 'english_score'])

# students = [
#     Student('Ali', 85, 75),
#     Student('Guli', 95, 90),
#     Student('Vali', 80, 70),
#     Student('Samar', 90, 85)
# ]

# sorted_students = sorted(students, key=lambda student: student.math_score, reverse=True)
# print("\nEng yuqori matematika bahosi:")
# for student in sorted_students:
#     print(f"{student.name} ({student.math_score})")
