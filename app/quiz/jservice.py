from typing import Optional, List, Dict
import requests


def fetch_random_questions(count: int) -> Optional[List[Dict]] | None:
    try:
        response = requests.get(f"https://jservice.io/api/random?count={count}")
        response.raise_for_status()
        question_data = response.json()
        return question_data
    except requests.RequestException:
        return None
