## KnowNow – a collaborative platform for creating and sharing study material.
#Study new material, check your level of knowledge, connect with other students and learn new subjects together, make custom cards and tests and share them with others.


## Site mockup:
![Landing Page](https://github.com/kate-sorokinaa/ITiROD/blob/main/lab2/Landing_Page.png)
![Buttom of Landing Page](https://github.com/kate-sorokinaa/ITiROD/blob/main/lab2/Buttom_of_Landing_Page.png)
![Sign In Page](https://github.com/kate-sorokinaa/ITiROD/blob/main/lab2/SignIn_Page.png)
![Sign Up Page](https://github.com/kate-sorokinaa/ITiROD/blob/main/lab2/SignUp_Page.png)
![Home Page](https://github.com/kate-sorokinaa/ITiROD/blob/main/lab2/Home_Page.png)
![Profile Page](https://github.com/kate-sorokinaa/ITiROD/blob/main/lab2/User_Page.png)
![Contacts Page](https://github.com/kate-sorokinaa/ITiROD/blob/main/lab2/Friends_Page.png)
![Flashcard Page](https://github.com/kate-sorokinaa/ITiROD/blob/main/lab2/Flashcard_Page.png)
![Test Page](https://github.com/kate-sorokinaa/ITiROD/blob/main/lab2/Test_Page.png)
![New Flashcard Page](https://github.com/kate-sorokinaa/ITiROD/blob/main/lab2/New_Flashcard_Page.png)
![New Test Page](https://github.com/kate-sorokinaa/ITiROD/blob/main/lab2/New_Test_Page.png)


## Main functions:
1. Authorization
2. Authentication
3. Connecting with other students
4. Learning using flashcards
5. Checking one's knowledge using tests
6. Making new flashcards
7. Making new tests
8. Competing with your contacts
9. Searching for new flashcards and tests


## Модели данных
# Users (Пользователи)
|имя поля | тип | ограничения | описание |
|:---:|:---:|:---:|:---:|
| id | pk(INT) | auto increment; not null; unique | первичный ключ |
| contact_list_id | fk(INT) | auto increment; not null; unique | список контактов пользователя |
| name | VARCHAR(100) | not null | ник пользователя |
| email | VARCHAR(50) | not null | почта пользователя |
| password | VARCHAR(255) | not null | пароль пользователя |
| bio | VARCHAR(500) |  | описание профиля пользователя |
| school | VARCHAR(100) |  | учебное заведение пользователя |
| date_of_birth | DATE |  | дата рождения пользователя |
| status | VARCHAR(100) | not null | статус пользователя |
| test_list_id | fk(INT) | auto increment; not null; unique | список тестов пользователя |
| flashcard_list_id | fk(INT) | auto increment; not null; unique | список карточек пользователя |


# Account_type (Тип аккаунта)
|имя поля | тип | ограничения | описание |
|:---:|:---:|:---:|:---:|
| id | pk(INT) | auto increment; not null; unique | первичный ключ |
| name | VARCHAR(100) | not null | название типа аккаунта |


# User_picture (Фото профиля пользователя)
|имя поля | тип | ограничения | описание |
|:---:|:---:|:---:|:---:|
| id | pk(INT) | auto increment; not null; unique | первичный ключ |
| user_id | fk(INT) | not null | пользователь |
| url | VARCHAR(300) | not null | путь к фото |


# Flashcard (Карточка)
|имя поля | тип | ограничения | описание |
|:---:|:---:|:---:|:---:|
| id | pk(INT) | auto increment; not null; unique | первичный ключ |
| name | fk(INT) | not null | название карточки |
| user_id | fk(INT) | not null | создатель карточки |
| terms_list_id | fk(INT) | not null | список терминов |
| terms_number | INT | not null | количество терминов |


# Term (Понятие)
|имя поля | тип | ограничения | описание |
|:---:|:---:|:---:|:---:|
| id | pk(INT) | auto increment; not null; unique | первичный ключ |
| term | VARCHAR(200) | not null | понятие |
| defenition | VARCHAR(1000) | not null | определение |


# Test (Тест)
|имя поля | тип | ограничения | описание |
|:---:|:---:|:---:|:---:|
| id | pk(INT) | auto increment; not null; unique | первичный ключ |
| name | fk(INT) | not null | название теста |
| user_id | fk(INT) | not null | создатель теста |
| questions_list_id | fk(INT) | not null | список вопросов |
| questions_number | INT | not null | количество вопросов |


# Question (Вопрос)
|имя поля | тип | ограничения | описание |
|:---:|:---:|:---:|:---:|
| id | pk(INT) | auto increment; not null; unique | первичный ключ |
| question | VARCHAR(200) | not null | вопрос |
| answers_list_id | fk(INT) | not null | список ответов |


# Answer (Ответ)
|имя поля | тип | ограничения | описание |
|:---:|:---:|:---:|:---:|
| id | pk(INT) | auto increment; not null; unique | первичный ключ |
| answer | VARCHAR(200) | not null | ответ |
| right | BOOLEAN | not null | правильный ли ответ |
