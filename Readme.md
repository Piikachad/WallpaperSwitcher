# 🖼️ Random Wallpaper Changer

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![OS](https://img.shields.io/badge/OS-Linux%20%7C%20Windows-green)

A simple Python script to automatically change your desktop wallpaper, compatible with **Linux** (GNOME, KDE, XFCE) and **Windows**.  

This script also remembers the last wallpaper used to avoid repeating it consecutively.

---

## Features

- **Cross-platform support**: Works on Linux and Windows.
- **Random wallpaper selection**: Each change picks a random wallpaper from your folder.
- **State saving**: Keeps track of the last wallpaper used to avoid repetition.
- **Multiple desktop environments on Linux**:
  - GNOME
  - KDE Plasma
  - XFCE
  - Fallback using `feh` if the DE is not detected
- **Windows support**: Uses `ctypes` to change wallpaper immediately.
- Easy to configure: just set the folder path and state file path.

---

## Requirements

- **Python 3.6+**
- Linux: `feh` (for unsupported DEs), `gsettings` (GNOME), `qdbus` (KDE), `xfconf-query` (XFCE)
- Windows: No additional dependencies

---

## Setup

### Linux

1. Place your wallpapers in a folder (e.g., `/home/username/Images/Wallpapers`).
2. Update the `WALLPAPER_FOLDER` variable in `wallpaper_linux.py` with the absolute path to your folder.
3. Run the script:

```bash
python3 wallpaper_linux.py
```

The script will detect your desktop environment and set a random wallpaper from your folder.

---

### Windows

1. Place your wallpapers in a folder (e.g., `C:\Users\user\Pictures\Wallpapers`).
2. Update the `WALLPAPER_FOLDER` variable in `wallpaper_windows.py` with the absolute path to your folder.
3. Set the path for the state file (e.g., `C:\Users\user\Documents\current_wallpaper.json`).
4. Run the script:

```powershell
python wallpaper_windows.py
```

The script will randomly choose a wallpaper and save the last one in a JSON file to avoid repeating it consecutively.

---

## How it works

- **Linux**:
  - Detects the current desktop environment.
  - Uses the appropriate command to set the wallpaper:
    - `gsettings` for GNOME
    - `qdbus` for KDE Plasma
    - `xfconf-query` for XFCE
    - `feh` as fallback
  - Chooses a random wallpaper from the specified folder.

- **Windows**:
  - Retrieves all images from the folder.
  - Chooses a random wallpaper index, avoiding repetition.
  - Sets the wallpaper using `ctypes.windll.user32.SystemParametersInfoW`.
  - Saves the current wallpaper index and timestamp in a JSON file.

---

## Optional Improvements

- Automatically rotate wallpapers at regular intervals.
- Add support for additional Linux desktop environments.
- GUI to select folder and set interval.

---

## Scripts

- `wallpaper_linux.py` – Linux version of the script
- `wallpaper_windows.py` – Windows version of the script

---

## License

This project is licensed under the MIT License.