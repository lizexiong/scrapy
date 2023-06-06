import scrapy


from scrapy import FormRequest,Request #Request是scrapy get请求方法

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']#首先访问登录页面
    def parse(self, response):
        authenticity_token=response.xpath('//input[@name="authenticity_token"]/@value').extract()[0]
        timestamp=response.xpath('//input[@name="timestamp"]/@value').extract()[0]
        timestamp_secret=response.xpath('//input[@name="timestamp_secret"]/@value').extract()[0]
        required_field=response.xpath('//input[@type="text"]/@name').extract()[1]
        form_data={
            "commit": "Sign+in",
            "authenticity_token":authenticity_token ,
            "login": "384775291@qq.com",
            "password": "Python@384775291",
            "webauthn-conditional": "undefined",
            "javascript-support": "true",
            "webauthn-support": "supported",
            "webauthn-iuvpaa-support": "unsupported",
            "return_to": "https://github.com/login",
            "allow_signup": "",
            "client_id": "",
            "integration": "",
            required_field: "",
            "timestamp": timestamp,
            "timestamp_secret":timestamp_secret,
        }
        print (form_data)
        yield scrapy.FormRequest(url="http://github.com/session",callback=self.login_parse,formdata=form_data)

    def login_parse(self, response):
        print ("URL:",response.url)
        #验证方式1
        #这里能获取到我的用户名就算登录成功了
        print ("My Name",response.xpath("//meta[@name='user-login']/@content").extract())

        #验证方式2
        # """验证登录是否成功"""
        #登录成功了会显示GitHub，登录不成功title显示Sign in to GitHub · GitHub
        print('parse starting。。。')
        title = response.xpath('//head/title/text()').extract_first()
        print("title",title)