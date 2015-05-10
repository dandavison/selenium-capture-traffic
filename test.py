import unittest
from urlparse import urlparse

import browsermobproxy
from selenium import webdriver


SELENIUM_COMMAND_EXECUTOR = "http://localhost:4444/wd/hub"
BROWSERMOB = "http://192.168.0.10:9999"


class BrowserMob(browsermobproxy.Server):

    def __init__(self, path, options=None):
        if options is None:
            options = {}
        self.hostname = options.pop('hostname', 'localhost')
        super(BrowserMob, self).__init__(path=path, options=options)

    @property
    def url(self):
        return "http://%s:%d" % (self.hostname, self.port)



class SeleniumMixin(object):
    browsermob = None

    @classmethod
    def setUpClass(cls):
        hostname, port = urlparse(BROWSERMOB).netloc.split(':')
        port = int(port)
        arbitrary_existing_file = __file__
        cls.browsermob = BrowserMob(
            arbitrary_existing_file,
            options={'hostname': hostname, 'port': port})

    def setUp(self):
        self.proxy = self.__class__.browsermob.create_proxy()
        browser_profile  = webdriver.FirefoxProfile()
        browser_profile.set_proxy(self.proxy.selenium_proxy())
        self.driver = webdriver.Remote(
            command_executor=SELENIUM_COMMAND_EXECUTOR,
            desired_capabilities=webdriver.DesiredCapabilities.FIREFOX,
            browser_profile=browser_profile)
        self.proxy.new_har(self._testMethodName)

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
