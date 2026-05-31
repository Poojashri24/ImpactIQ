import json
import os

memory_store = []

HISTORY_FILE = "data/history.json"


def load_history():
    global memory_store

    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                memory_store = json.load(f)
        except:
            memory_store = []


def save_history():
    with open(HISTORY_FILE, "w") as f:
        json.dump(memory_store, f, indent=2)


def add_to_memory(text):
    memory_store.append(text)
    save_history()


def search_memory(query, k=3):

    if len(memory_store) == 0:
        return []

    return memory_store[-k:]


load_history()