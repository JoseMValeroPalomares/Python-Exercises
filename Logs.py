import os 

folder_path = "C:/ProgramData/USOShared/Logs/System"

for filename in os.listdir(folder_path):
    filepath = os.path.join(folder_path, filename)
    try:
        if os.path.isfile(filepath) or os.path.islink(filepath):
            os.unlink(filepath)
        elif os.path.isdir(filepath):
            os.rmdir(filepath)
    except Exception as e:
        print(f"Error al eliminar {filepath}: {e}")

        