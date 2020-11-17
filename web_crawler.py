"""Definition of crawler for poll."""
# -*- coding: utf-8 -*-
import scrapy


class PollSpider(scrapy.Spider):
    name = 'lvb'
    start_urls = ['https://l-blog.de/lvb-kampagne-stimmt-ab-bei-unserem-geschichtenwettbewerb/']





poll_http_request = "https://l-blog.de/wp-admin/admin-ajax.php?action=totalpoll"
# TODO: find out how the voting choice is made in this request...
