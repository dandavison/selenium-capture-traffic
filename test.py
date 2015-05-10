import unittest
from urlparse import urlparse

import browsermobproxy
from selenium import webdriver


SELENIUM_COMMAND_EXECUTOR = "http://localhost:4444/wd/hub"
BROWSERMOB = "http://localhost:9999"


class SeleniumMixin(object):
    browsermob = None

    @classmethod
    def setUpClass(cls):
        hostname, port = urlparse(BROWSERMOB).netloc.split(':')
        port = int(port)
        arbitrary_existing_file = __file__
        cls.browsermob = browsermobproxy.Server(
            arbitrary_existing_file,
            options={'port': port})

    def setUp(self):
        proxy = self.__class__.browsermob.create_proxy()
        browser_profile  = webdriver.FirefoxProfile()
        browser_profile.set_proxy(proxy.selenium_proxy())
        self.driver = webdriver.Remote(
            command_executor=SELENIUM_COMMAND_EXECUTOR,
            desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
            browser_profile=browser_profile)

    @classmethod
    def tearDownClass(cls):
        if cls.browsermob.process:
            cls.browsermob.stop()


class Test(SeleniumMixin, unittest.TestCase):

    def test(self):
        self.driver.get("http://www.python.org")
        self.assertIn("Python", self.driver.title)


if __name__ == "__main__":
    unittest.main()
