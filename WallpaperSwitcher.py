import os
import subprocess
import random

# Make sure the path is absolute
WALLPAPER_FOLDER = r"/path/to/your/wallpapers"  # Replace with your actual wallpaper folder
IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.bmp')

def get_wallpapers(folder):
    """Retrieve the list of available image files in the folder."""
    try:
        return [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(IMAGE_EXTENSIONS)]
    except Exception as e:
        print(f"Error retrieving wallpapers: {e}")
        return []

def set_wallpaper(filepath):
    """Change the wallpaper based on the desktop environment."""
    try:
        desktop_env = os.environ.get("XDG_CURRENT_DESKTOP", "").lower()

        if "gnome" in desktop_env:
            subprocess.run([
                "gsettings", "set",
                "org.gnome.desktop.background",
                "picture-uri", f"file://{filepath}"
            ])
        elif "kde" in desktop_env:
            script = f'''
            var allDesktops = desktops();
            for (i=0; i<allDesktops.length; i++) {{
                d = allDesktops[i];
                d.wallpaperPlugin = "org.kde.image";
                d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General");
                d.writeConfig("Image", "file://{filepath}");
            }}
            '''
            subprocess.run([
                "qdbus", "org.kde.plasmashell",
                "/PlasmaShell",
                "org.kde.PlasmaShell.evaluateScript", script
            ])
        elif "xfce" in desktop_env:
            subprocess.run([
                "xfconf-query", "-c", "xfce4-desktop",
                "-p", "/backdrop/screen0/monitor0/image-path",
                "-s", filepath
            ])
        else:
            # Fallback for other environments using feh
            subprocess.run(["feh", "--bg-scale", filepath])
    except Exception as e:
        print(f"Error changing wallpaper: {e}")

def main():
    wallpapers = get_wallpapers(WALLPAPER_FOLDER)
    if not wallpapers:
        print("No wallpapers found in the specified folder.")
        return

    random_wallpaper = random.choice(wallpapers)
    set_wallpaper(random_wallpaper)

if __name__ == "__main__":
    main()
