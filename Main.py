
  create from selenium
import webdriver
from selenium.common.exceptions 
import NoSuchElementException
import time


def scanTakealotProduct(url):
    """returns the following information about the product:
                1. Price
                2. Availability
                3. Seller
                4. Next available offer
                    4.1 Price
                    4.2 Availability
                    4.3 Seller
    Keyword arguments:
    url -- a link to a product on takealot
    """
    driver = webdriver.Chrome()
    driver.get(url)

    while(pageHasLoaded(driver) is False):
        time.sleep(0.1)

    price = getElementText(
        driver,
        '.pdp-module_sidebar-buybox_1m6Sm > div > div'
        )
    print('1. Price: ' + price)

    availability = getElementText(driver, '.stock-availability-status')
    print('2. Availability: ' + availability)

    seller = getElementText(driver, '.brand-link')
    print('3. Seller: ' + seller)

    try:
        element = driver.find_element_by_class_name('plusminus').click()
    except NoSuchElementException:
        print('No additional offers')
        return

    print('4. Next Available Offer Info:')
    nextAvailableOfferPrice = getElementText(
        driver,
        '.sf-accordion-item > div > div > div > div > div' +
        '> div > div > div > div > div > span'
        )
    print('\t4.1 Price: ' + nextAvailableOfferPrice)

    nextAvailableOfferAvailability = getElementText(
        driver,
        '.sf-accordion-item > div > div > div > div >' +
        'div > div > div > div > div:nth-child(2) > div > div'
    )

    print('\t4.1 Availability: ' + nextAvailableOfferAvailability)

    nextAvailableOfferSeller = getElementText(
        driver,
        '.sf-accordion-item > div > div > div > div > div > div > div' +
        '> div > div:nth-child(2) > div > div:nth-child(2)'
    )
    print('\t4.1 Seller: ' + nextAvailableOfferSeller)


def pageHasLoaded(driver):
    """Checks if a page has been loaded by looking at the price:
    Keyword arguments:
    driver -- the web driver that has loaded the page
    """

    try:
        driver.find_element_by_css_selector(
            '.pdp-module_sidebar-buybox_1m6Sm > div > div'
        ).text
        return True
    except NoSuchElementException:
        return False


def getElementText(driver, cssSelector):
    """ retrurns an elements text based on the given css selector
        Keyword arguments:
            driver -- the web driver that has loaded the page
            cssSelector -- the css selector for the element
    """
    return driver.find_element_by_css_selector(cssSelector).text


scanTakealotProduct(
    'https://www.takealot.com/' +
    'russell-hobbs-2200w-crease-control-iron/PLID34147865'
    )
