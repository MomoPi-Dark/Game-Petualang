from kivy.storage.jsonstore import JsonStore


class ConfigManager:
    def __init__(self, score_file="configs.json"):
        self._store = JsonStore(score_file, sort_keys=True)

    def exists(self, key):
        return self._store.exists(key)

    def delete(self, key):
        self._store.delete(key)

    def set(self, key, values):
        if isinstance(values, dict):
            self._store.put(key, **values)
        else:
            self._store.put(key, value=values)

    def get(self, key, value_if_not_exists=None):
        if self.exists(key):
            return self._store.get(key).get("value", value_if_not_exists)
        return None

    def get_all(self):
        return self._store
