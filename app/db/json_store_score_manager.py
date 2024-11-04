from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore


class ScoreManager:
    def __init__(self, score_file="score.json"):
        self._store = JsonStore(score_file, sort_keys=True)

    def get_score(self, category, key):
        """Retrieve the score data for a specific category and key."""
        if self._store.exists(category):
            category_data = self._store.get(category)
            if key in category_data:
                return category_data[key]
        return None

    def save_score(self, category, key, score, elapsed_time):
        """Save the latest score and update the best score if needed, in a nested JSON format."""

        category_data = (
            self._store.get(category) if self._store.exists(category) else {}
        )

        if key not in category_data:
            category_data[key] = {"last_score": {}, "best_score": {}}

        category_data[key]["last_score"] = {
            "score": score,
            "elapsed_time": elapsed_time,
            "timestamp": Clock.get_time(),
        }

        best_score_data: dict = category_data[key].get(
            "best_score", {"score": 0, "elapsed_time": float("inf")}
        )
        best_score = best_score_data.get("score", 0)
        best_time = best_score_data.get("elapsed_time", float("inf"))

        if score > best_score or (score == best_score and elapsed_time < best_time):
            category_data[key]["best_score"] = {
                "score": score,
                "elapsed_time": elapsed_time,
                "timestamp": Clock.get_time(),
            }

        self._store.put(category, **category_data)
