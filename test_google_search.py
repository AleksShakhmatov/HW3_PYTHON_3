from selene import browser, be, have


def test_have_result():
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="rcnt"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_have_do_not_have_result():
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('rtgr ,;ksse awedsdertb55yu ll').press_enter()
    browser.element('[id="rcnt"]').should(have.text('По запросу rtgr ,;ksse awedsdertb55yu ll ничего не найдено.'))
