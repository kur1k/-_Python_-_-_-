from playwright.sync_api import expect

from .base_page import BasePage

class MainPage(BasePage):
    def open_business_tab(self):
        """Открывает вкладку 'Для бизнеса' -> 'Для крупного бизнеса'."""
        # TODO: Вставьте локаторы для навигации к 'Для бизнеса'
        self.page.click("button:has-text('Для бизнеса')")
        self.page.click("a.FullSectionItem_tabSectionItemLink__A_K6_ >> text=Для крупного бизнеса")

    def open_product_section(self):
        """Открывает раздел Продукты -> 'Kaspersky Industrial CyberSecurity for Networks'."""
        # TODO: Вставьте локатор для 'Kaspersky Industrial CyberSecurity for Networks'
        self.page.hover("a.MainMenu_link__bNYzB:has-text('Продукты')")
        self.page.click("span.EntEntity_prodTitle__j0eHt:has-text('Industrial CyberSecurity')")

    def is_certificate_text_present(self, text: str) -> bool:
        """Проверяет наличие указанного текста на странице."""
        return self.page.inner_text("body").find(text) != -1

    def download_pdf(self):
        """Скачивает PDF файл."""
        # TODO: Вставьте локатор кнопки для скачивания PDF
        self.page.click("a.Link_link__hXQBL:has-text('Скачать обзор')")