#### Capture network traffic during execution of a selenium test

###### Instructions

1. `vagrant up` and `vagrant ssh`
2. In the VM, download the [browsermob executable package](https://github.com/lightbody/browsermob-proxy/releases/download/browsermob-proxy-2.0.0/browsermob-proxy-2.0.0-bin.zip), unzip it, and run `bin/browsermob-proxy --port 9999`
3. Make sure selenium server is running on localhost port 4444
4. `python test.py`


###### Resources
- https://code.google.com/p/selenium/wiki/RemoteWebDriverServer
- http://docs.seleniumhq.org/docs/04_webdriver_advanced.jsp#using-a-proxy
- https://selenium-release.storage.googleapis.com/2.45/selenium-server-standalone-2.45.0.jar
- https://github.com/lightbody/browsermob-proxy/releases/download/browsermob-proxy-2.0.0/browsermob-proxy-2.0.0-bin.zip
