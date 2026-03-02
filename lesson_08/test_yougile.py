import requests

base_url = "https://ru.yougile.com"
token = "token"
auth = {"Authorization": f"Bearer {token}"}
auth1 = {"Authorization": f"Bearer {token + "1"}"}


def test_create_positive():
    project = {'title': 'Проект 12'}
    new_project = requests.post(base_url + "/api-v2/projects", json=project,
                                headers=auth)
    print(new_project.json())
    assert new_project.status_code == 201


def test_create_negative():
    project = {'title': ''}
    new_project = requests.post(base_url + "/api-v2/projects", json=project,
                                headers=auth)
    assert new_project.status_code == 400


def test_create_negative_1():
    project = {'title': 'Проект 12'}
    new_project = requests.post(base_url + "/api-v2/projects", json=project,
                                headers=auth1)
    print(new_project.json())
    assert new_project.status_code == 401


def test_update_positive():
    project = {'title': 'Проект 12'}
    new_project = requests.post(base_url + "/api-v2/projects", json=project,
                                headers=auth)
    project_id = new_project.json()["id"]
    project2 = {'title': 'Проект 13'}
    update = requests.put(base_url + "/api-v2/projects/" + f"{project_id}",
                          json=project2, headers=auth)
    assert update.status_code == 200


def test_update_negative():
    project = {'title': 'Проект 12'}
    new_project = requests.post(base_url + "/api-v2/projects", json=project,
                                headers=auth)
    project_id = new_project.json()["id"] + "24"
    project2 = {'title': 'Проект 13'}
    update = requests.put(base_url + "/api-v2/projects/" + f"{project_id}",
                          json=project2, headers=auth)
    assert update.status_code == 404


def test_update_negative_1():
    project = {'title': 'Проект 12'}
    new_project = requests.post(base_url + "/api-v2/projects", json=project,
                                headers=auth)
    project_id = new_project.json()["id"]
    project2 = {'title': 'Проект 13'}
    update = requests.put(base_url + "/api-v2/projects/" + f"{project_id}",
                          json=project2, headers=auth1)
    assert update.status_code == 401


def test_get_positive():
    project = {'title': 'Проект 12'}
    new_project = requests.post(base_url + "/api-v2/projects", json=project,
                                headers=auth)
    project_id = new_project.json()["id"]
    get = requests.put(base_url + "/api-v2/projects/" + f"{project_id}",
                       json=project, headers=auth)
    assert get.status_code == 200


def test_get_negative():
    project = {'title': 'Проект 12'}
    new_project = requests.post(base_url + "/api-v2/projects", json=project,
                                headers=auth)
    project_id = new_project.json()["id"]+"35"
    get = requests.put(base_url + "/api-v2/projects/" + f"{project_id}",
                       json=project, headers=auth)
    assert get.status_code == 404


def test_get_negative_1():
    project = {'title': 'Проект 12'}
    new_project = requests.post(base_url + "/api-v2/projects", json=project,
                                headers=auth)
    project_id = new_project.json()["id"]
    get = requests.put(base_url + "/api-v2/projects/" + f"{project_id}",
                       json=project, headers=auth1)
    assert get.status_code == 401
