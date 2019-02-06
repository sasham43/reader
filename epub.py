import ebooklib
from ebooklib import epub

epub_path = '/home/pi/epub/dickens.epub'

book = epub.read_epub(epub_path)

all_items = book.get_items()

print('epub', all_items)
