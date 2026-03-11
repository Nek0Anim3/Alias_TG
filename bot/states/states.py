
_states: dict[int, dict] = {}

def set_state(user_id: int, state: str, **data):
    _states[user_id] = {"state": state, "data": data}

def get_state(user_id: int) -> str | None:
    return _states.get(user_id, {}).get("state")

def get_data(user_id: int) -> dict:
    return _states.get(user_id, {}).get("data", {})

def update_data(user_id: int, **kwargs):
    if user_id in _states:
        _states[user_id]["data"].update(kwargs)

def clear_state(user_id: int):
    _states.pop(user_id, None)

