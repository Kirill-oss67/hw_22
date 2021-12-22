import os
import sys
from pathlib import Path

python = sys.executable
project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[: basefolder_index + 1])
os.chdir(Path(os.path.abspath(__file__)).parent)

if __name__ == "__main__":
    os.system(f'{python} -m unittest')
