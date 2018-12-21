from selenium import webdriver
from queue import Queue
from threading import Thread


class Work:

    def __init__(self, url):
        option = webdriver.ChromeOptions()
        option.add_argument('--no-sandbox')
        driver = webdriver.Chrome(chrome_options=option)
        driver.set_window_size(1920, 1380)
        driver.implicitly_wait(5)
        self.url = url
        driver.get(self.url)
        a_list = driver.find_elements_by_xpath("//p/a")
        self.q = Queue()
        for a in a_list:
            self.q.put(a)

    def click_a(self, link):
        link.click()
        while True:
            if not self.q.empty():
                self.q.get().click()
            else:
                break

    def task(self):
        l1 = []
        for i in range(10):
            link = self.q.get()
            t = Thread(target=self.click_a, args=(link,))
            t.start()
            l1.append(t)
        [i.join() for i in l1]


if __name__ == '__main__':
    url1 = "https://www.cnblogs.com/louyifei0824/p/9965557.html"
    Work(url1).task()
