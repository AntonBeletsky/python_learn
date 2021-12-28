import sys
from colorama import init, Fore, AnsiToWin32


init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream

# https://www.linux.org.ru/forum/development/14494819
# https://ru.wikipedia.org/wiki/%D0%9F%D1%81%D0%B5%D0%B2%D0%B4%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%BA%D0%B0
# Python 3
print(Fore.RED + '├├├├├├├├├├├├├├├├├├', file=stream)
print(Fore.BLUE + '███████████████████████████████████████', file=stream)
