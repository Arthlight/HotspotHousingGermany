from crontab import CronTab


cron = CronTab(user='arthred')
job = cron.new(command='echo hello_world')
job.minute.every(1)
cron.write()



#job = cron.new(command='cd Flat_Crawler_Scrapy/Flat_Crawler_Scrapy && scrapy crawl ImmobilienScout')








