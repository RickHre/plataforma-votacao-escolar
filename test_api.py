import requests

BASE_URL = "http://127.0.0.1:8000"

def safe_print(label, response):
    try:
        print(label, response.status_code, response.json())
    except Exception:
        print(label, response.status_code, response.text)

def test_register_and_login():
    # Registrar professor
    r = requests.post(f"{BASE_URL}/auth/register", json={
        "username": "professor1",
        "password": "123456",
        "role": "professor"
    })
    safe_print("Register professor:", r)

    # Registrar aluno
    r = requests.post(f"{BASE_URL}/auth/register", json={
        "username": "aluno1",
        "password": "123456",
        "role": "aluno"
    })
    safe_print("Register aluno:", r)

    # Login professor
    r = requests.post(f"{BASE_URL}/auth/login", data={
        "username": "professor1",
        "password": "123456"
    })
    safe_print("Login professor:", r)
    token_prof = r.json().get("access_token")

    # Login aluno
    r = requests.post(f"{BASE_URL}/auth/login", data={
        "username": "aluno1",
        "password": "123456"
    })
    safe_print("Login aluno:", r)
    token_aluno = r.json().get("access_token")

    return token_prof, token_aluno

def test_create_election(token_prof):
    headers = {"Authorization": f"Bearer {token_prof}"}
    r = requests.post(f"{BASE_URL}/elections/", json={
        "title": "Eleição Teste"
    }, headers=headers)
    safe_print("Create election:", r)
    election_id = None
    try:
        election_id = r.json().get("id")
    except Exception:
        pass
    return election_id

def test_candidates(token_prof):
    headers = {"Authorization": f"Bearer {token_prof}"}
    r = requests.post(f"{BASE_URL}/candidates/", json={
        "name": "Maria Silva",
        "turma": "3A"
    }, headers=headers)
    safe_print("Create candidate:", r)
    candidate_id = None
    try:
        candidate_id = r.json().get("id")
    except Exception:
        pass

    r = requests.get(f"{BASE_URL}/candidates/", headers=headers)
    safe_print("List candidates:", r)

    return candidate_id

def test_votes(token_aluno, token_prof, candidate_id, election_id):
    headers_aluno = {"Authorization": f"Bearer {token_aluno}"}
    headers_prof = {"Authorization": f"Bearer {token_prof}"}

    r = requests.post(
        f"{BASE_URL}/votes/submit?candidate_id={candidate_id}&election_id={election_id}",
        headers=headers_aluno
    )
    safe_print("Submit vote:", r)

    r = requests.get(f"{BASE_URL}/votes/results/{election_id}", headers=headers_prof)
    safe_print("Results:", r)

def test_dashboard(token_prof):
    headers = {"Authorization": f"Bearer {token_prof}"}
    r = requests.get(f"{BASE_URL}/dashboard/", headers=headers)
    safe_print("Dashboard:", r)

if __name__ == "__main__":
    token_prof, token_aluno = test_register_and_login()
    election_id = test_create_election(token_prof)
    candidate_id = test_candidates(token_prof)
    test_votes(token_aluno, token_prof, candidate_id, election_id)
    test_dashboard(token_prof)