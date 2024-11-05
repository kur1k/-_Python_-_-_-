from framework.pages.base_page import BasePage


class BusinessPage(BasePage):
    """Класс для страницы продуктов Kaspersky для бизнеса."""

    INDUSTRIAL_CYBERSECURITY = 'text="Kaspersky Industrial CyberSecurity for Networks"'
    CERTIFICATION_TEXT_LOCATOR = '//*[contains(text(), "242 сертифицированных систем от 60 поставщиков АСУ ТП")]'
    DOWNLOAD_OVERVIEW_BUTTON = 'text="Скачать обзор"'

    def open_industrial_cybersecurity(self):
        """Переход к странице 'Kaspersky Industrial CyberSecurity for Networks'."""
        self.click_element(self.INDUSTRIAL_CYBERSECURITY)

    def check_certification_text(self) -> str:
        """Проверяет наличие текста о сертифицированных системах."""
        return self.get_text(self.CERTIFICATION_TEXT_LOCATOR)

    def download_overview(self):
        """Нажимает на кнопку скачивания обзора."""
        self.click_element(self.DOWNLOAD_OVERVIEW_BUTTON)
