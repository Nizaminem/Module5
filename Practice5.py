import time
import hashlib


# Класс для представления пользователей
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)  # Хэшируем пароль
        self.age = age

    @staticmethod
    def hash_password(password):
        """Хэширование пароля"""
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)


# Класс для представления видео
class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration  # Продолжительность в секундах
        self.time_now = 0  # Текущая секунда просмотра
        self.adult_mode = adult_mode  # Ограничение по возрасту

# Основной класс платформы UrTube
class UrTube:
    def __init__(self):
        self.users = []  # Список всех зарегистрированных пользователей
        self.videos = []  # Список всех видео
        self.current_user = None  # Текущий пользователь

    def log_in(self, nickname, password):
        """Авторизация пользователя"""
        hashed_password = User.hash_password(password)
        for users in self.users:
            if users.nickname == nickname and users.password == hashed_password:
                self.current_user = users
                print(f"Вы вошли как {nickname}")
                return
        print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        """Регистрация нового пользователя"""
        if any(users.nickname == nickname for users in self.users):
            print(f"Пользователь {nickname} уже существует")
        return
        new_users = self.users(nickname, password, age)
        self.users.append(new_users)
        self.current_user = new_users
        print(f"Пользователь {nickname} успешно зарегистрирован и вошёл")

    def log_out(self):
        """Выход из аккаунта"""
        if self.current_user:
            print(f"Вы вышли из аккаунта {self.current_user.nickname}")
        self.current_user = None

    def add(self, *videos):
        """Добавление видео"""
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено")
            else:
                print(f"Видео '{video.title}' уже существует")

    def get_videos(self, search_term):
        """Поиск видео по ключевому слову"""
        search_term = search_term.lower()
        return [video.title for video in self.videos if search_term in video.title.lower()]

    def watch_video(self, title):
        """Просмотр видео"""
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        # Ищем видео по названию
        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            print("Видео не найдено")
            return

        # Проверяем возрастное ограничение
        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        # Начинаем просмотр
        print(f"Начинаем просмотр видео: {video.title}")
        for second in range(video.time_now, video.duration):
            print(f"Секунда {second + 1}")
            time.sleep(1)  # Пауза для имитации просмотра
        video.time_now = 0  # Сброс времени
        print("Конец видео")

# # Создаём платформу
# urtube = UrTube()
#
# # Регистрируем пользователей
# urtube.register("Alice", "password123", 25)
# urtube.register("Bob", "qwerty", 15)
#
# # Добавляем видео
# urtube.add(Video("Python Basics", 10), Video("Advanced Python", 15, adult_mode=True))
#
# # Авторизуемся и смотрим видео
# urtube.log_in("Alice", "password123")
# urtube.watch_video("Python Basics")
#
# # Попытка просмотра видео с ограничением 18+
# urtube.watch_video("Advanced Python")
#
# # Выходим из аккаунта и пробуем смотреть видео
# urtube.log_out()
# urtube.watch_video("Python Basics")

# Код для проверки:

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))


# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')