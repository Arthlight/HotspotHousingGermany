from crontab import CronTab

#abspath = os.path.abspath(__file__)
#dname = os.path.dirname(abspath)
#os.chdir(dname)

cron = CronTab(user='arthred')
cron.env['SHELL'] = '/bin/bash'
job = cron.new(command=' cd /Users/arthred/Documents/Flat_Crawler_Django/Flat_Crawler_Scrapy && scrapy crawl ImmobilienScout')
job.minute.every(2)
cron.write()










