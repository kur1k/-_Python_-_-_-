import pytest
from playwright.sync_api import sync_playwright

from framework.utils.pdf_utils import PDFHelper
from framework.pages.main_page import MainPage


@pytest.fixture(scope="function")
def setup_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


def test_check_certificate_info(setup_playwright):
    """Тест для проверки наличия текста сертификата на странице."""
    page = setup_playwright
    main_page = MainPage(page)

    main_page.open("https://www.kaspersky.ru/")
    main_page.open_business_tab()
    main_page.open_product_section()

    print(main_page.is_certificate_text_present(text="242 сертифицированных систем от 60 поставщиков АСУ ТП"))

def test_check_pdf_info(setup_playwright, tmp_path):
    """Тест для проверки текста на 5-й странице PDF файла."""
    page = setup_playwright
    main_page = MainPage(page)
    pdf_helper = PDFHelper()

    main_page.open("https://www.kaspersky.ru/")
    main_page.open_business_tab()
    main_page.open_product_section()

    # Загружаем PDF в tmp_path
    download_path = tmp_path / "overview.pdf"
    page.on("download", lambda download: download.save_as(download_path))
    main_page.download_pdf()

    # Проверяем текст на 5-й странице
    assert "KICS for Networks" in pdf_helper.extract_text_from_page(download_path, 5)
