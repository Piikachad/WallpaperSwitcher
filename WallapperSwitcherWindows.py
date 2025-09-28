import os
import ctypes
import json
import random
from datetime import datetime

# Make sure the paths are absolute
WALLPAPER_FOLDER = r"C:\Users\user\Pictures\Wallpapers"  # Absolute path to your wallpaper folder
STATE_FILE = r"C:\Users\user\Documents\current_wallpaper.json"  # Absolute path to the state file
IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.bmp')

def get_wallpapers(folder):
    """Retrieve the list of wallpaper files."""
    try:
        return [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(IMAGE_EXTENSIONS)]
    except Exception as e:
        print(f"Error while retrieving wallpapers: {e}")
        return []

def set_wallpaper(filepath):
    """Change the wallpaper."""
    try:
        # SPI_SETDESKWALLPAPER = 20, update immediately
        ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 3)
    except Exception as e:
        print(f"Error while changing wallpaper: {e}")

def save_state(index):
    """Save the index of the current wallpaper."""
    try:
        with open(STATE_FILE, 'w') as f:
            json.dump({'current_index': index, 'last_change': datetime.now().isoformat()}, f)
    except Exception as e:
        print(f"Error while saving state: {e}")

def load_state():
    """Load the current state, with validation."""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r') as f:
                state = json.load(f)
            if 'current_index' in state and 'last_change' in state:
                return state
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error while loading state: {e}")
    return {'current_index': -1, 'last_change': None}

def main():
    wallpapers = get_wallpapers(WALLPAPER_FOLDER)
    if not wallpapers:
        print("No wallpapers found in the specified folder.")
        return

    state = load_state()
    current_index = state['current_index']

    # Pick a random wallpaper index different from the last one
    available_indices = list(range(len(wallpapers)))
    if current_index in available_indices and len(wallpapers) > 1:
        available_indices.remove(current_index)
    next_index = random.choice(available_indices)
    next_wallpaper = wallpapers[next_index]

    set_wallpaper(next_wallpaper)
    save_state(next_index)

if __name__ == "__main__":
    main()
