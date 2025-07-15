from mcresources import ResourceManager
from typing import Optional, List, Dict, Any


class Book:
    def __init__(self, rm: ResourceManager, mod_id: str, book_id: str, create_book: bool = False,
                 book_name: Optional[str] = None, landing_text: Optional[str] = None,
                 book_item: str = "patchouli:guide_book"):
        self.rm = rm
        self.mod_id = mod_id
        self.book_id = book_id
        self.lang_entries = {}

        if create_book:
            self.rm.data(
                (mod_id, 'patchouli_books', book_id, 'book'),
                {
                    "name": f"patchouli.{mod_id}.book.{book_id}",
                    "landing_text": landing_text or f"patchouli.{mod_id}.book.{book_id}.landing_text",
                    "version": 1,
                    "show_progress": True,
                    "use_blocky_font": False,
                    "book_texture": "patchouli:textures/gui/book.png",
                    "model": book_item,
                    "i18n": True
                },
                root_domain='assets'
            )

            self.rm.lang({
                f"patchouli.{mod_id}.book.{book_id}": book_name or book_id.replace("_", " ").title(),
                f"patchouli.{mod_id}.book.{book_id}.landing_text": landing_text or "Welcome to your journey!"
            })

    def generate_category(self, category_id: str, name: str, description: str, icon: str, sortnum: int,
                          flag: str = None):
        category = {
            "name": name,
            "description": description,
            "icon": icon,
            "sortnum": sortnum,
            "flag": flag
        }

        self.rm.data(
            ('../' + self.mod_id, 'patchouli_books', self.book_id, 'en_us', 'categories', category_id),
            category,
            root_domain='assets'
        )

        return BookCategory(self.rm, self.mod_id, self.book_id, category_id, self.lang_entries, flag)


class BookCategory:
    def __init__(self, rm: ResourceManager, mod_id: str, book_id: str, category_id: str,
                 lang_entries: Dict[str, str],
                 inherited_flag: str = None):
        self.rm = rm
        self.mod_id = mod_id
        self.book_id = book_id
        self.category_id = category_id
        self.lang_entries = lang_entries
        self.inherited_flag = inherited_flag

    def generate_entry(self, entry_id: str, name: str, icon: str,
                       priority: bool = False, flag: str = None):
        return BookEntry(
            self.rm,
            self.mod_id,
            self.book_id,
            self.category_id,
            entry_id,
            name,
            icon,
            self.lang_entries,
            priority,
            flag or self.inherited_flag
        )


class BookEntry:
    def __init__(self, rm: ResourceManager, mod_id: str, book_id: str, category_id: str, entry_id: str,
                 name: str, icon: str,
                 lang_entries: Dict[str, str],
                 priority: bool,
                 flag: str):
        self.rm = rm
        self.mod_id = mod_id
        self.book_id = book_id
        self.category_id = category_id
        self.entry_id = entry_id
        self.name = name
        self.icon = icon
        self.flag = flag
        self.lang_entries = lang_entries
        self.priority = priority
        self.pages = []

    def add_text_page(self, text: str, title: str = None):
        page = {
            "type": "patchouli:text",
            "text": text
        }

        if title:
            page["title"] = title

        self.pages.append(page)

        return self

    def add_crafting_page(self, recipe_id: str, recipe2_id: str = None, title: str = None, text: str = None):
        page = {
            "type": "patchouli:crafting",
            "recipe": recipe_id
        }

        if recipe2_id is not None:
            page["recipe2"] = recipe2_id
        if title is not None:
            page["title"] = title
        if text is not None:
            page["text"] = text

        self.pages.append(page)
        return self

    def add_tfc_multimultiblock_page(self, multiblocks: list, text: str = ""):
        page = {
            "type": "tfc:multimultiblock",
            "text": text,
            "multiblocks": multiblocks
        }
        self.pages.append(page)
        return self

    def save(self):
        entry = {
            "name": self.name,
            "category": f"{self.mod_id}:{self.category_id}",
            "icon": self.icon,
            "pages": self.pages,
            "priority": self.priority
        }
        if self.flag:
            entry["flag"] = self.flag

        self.rm.data(
            ('../' + self.mod_id, 'patchouli_books', self.book_id, 'en_us', 'entries', self.entry_id),
            entry,
            root_domain='assets'
        )

        return self
