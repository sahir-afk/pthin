from pathlib import Path
import os
path = Path("spam", "bacon", "eggs")
print(path)
path = Path('spam')/"eggs"/"bacon"      #/ is kinda like + with strings because it concatenates the values
print(path)
