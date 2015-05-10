import unittest

from selenium import webdriver


DRIVER_PROXY = "192.168.0.0:9999"
EXECUTOR = "http://localhost:4444/wd/hub"


class SeleniumMixin(object):

    def setUp(self):
        capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
        if DRIVER_PROXY:
            capabilities['proxy'] = {
                'httpProxy': DRIVER_PROXY,
                'ftpProxy': DRIVER_PROXY,
                'sslProxy': DRIVER_PROXY,
                'noProxy': None,
                'proxyType': 'MANUAL',
                'class': 'org.openqa.selenium.Proxy',
                'autodetect': False,
            }
        self.driver = webdriver.Remote(EXECUTOR, capabilities)

    def tearDown(self):
        self.driver.close()


class Test(SeleniumMixin, unittest.TestCase):

    def test(self):
        self.driver.get("http://www.python.org")
        self.assertIn("Python", self.driver.title)


if __name__ == "__main__":
    unittest.main()
