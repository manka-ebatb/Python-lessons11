from sqlalchemy import create_engine, inspect, text


db_connection_string = "postgresql://postgres:12345@localhost:5432/postgres"
db = create_engine(db_connection_string)
select_query = text("SELECT * FROM users WHERE user_id = :user_id")
add_query = text(
    "INSERT INTO users (user_id, user_email, subject_id) "
    "VALUES (:user_id, :user_email, :subject_id)")
update_query = text(
    "UPDATE users SET user_email = :user_email WHERE user_id = :user_id")
delete_query = text("DELETE FROM users WHERE user_id = :user_id")


def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[1] == 'species'


def test_add_users():
    connection = db.connect()
    connection.execute(add_query, {
        "user_id": 85427,
        "user_email": "ivanov@mail",
        "subject_id": 2
    })
    user_row = connection.execute(select_query, {"user_id": 85427}).fetchone()
    connection.execute(delete_query, {"user_id": 85427})
    assert user_row[1] == "ivanov@mail"
    connection.close()


def test_update_users():
    connection = db.connect()
    connection.execute(add_query, {
        "user_id": 85427,
        "user_email": "ivanov@mail",
        "subject_id": 2
    })
    connection.execute(update_query, {
             "user_email": 'new_email@ya.ru',
             "user_id": 85427
             })
    user_row = connection.execute(select_query, {"user_id": 85427}).fetchone()
    connection.execute(delete_query, {"user_id": 85427})
    assert user_row[1] == "new_email@ya.ru"
    connection.close()


def test_delete_users():
    connection = db.connect()
    connection.execute(add_query, {
        "user_id": 85427,
        "user_email": "petrov@mail",
        "subject_id": 4
    })
    connection.execute(delete_query, {"user_id": 85427})
    user_row = connection.execute(select_query, {"user_id": 85427}).fetchall()
    assert len(user_row) == 0
    connection.close()
