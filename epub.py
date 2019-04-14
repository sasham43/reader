import ebooklib
from ebooklib import epub

# epub_path = '/home/pi/epub/dickens.epub'
epub_path = 'dickens.epub'

book = epub.read_epub(epub_path)

# all_items = book.get_items()
#
# print('epub', all_items)
count = 0
for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        print('==================================')
        print('NAME : ', item.get_name())
        print('----------------------------------')
        print(item.get_body_content())
        print('==================================')
        # break
        if count == 3:
            break
        count += 1
