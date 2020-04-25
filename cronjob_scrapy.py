from crontab import CronTab

#abspath = os.path.abspath(__file__)
#dname = os.path.dirname(abspath)
#os.chdir(dname)

cron = CronTab(user='arthred')
#cron.env['SHELL'] = '/bin/bash'
job = cron.new(command='cd /Users/arthred/Documents/Flat_Crawler_Django/Flat_Crawler_Scrapy/Flat_Crawler_Scrapy/spiders && sudo chown -R $(whoami) . && sudo chmod -R +rwX . && python __init__.py')
job.minute.every(2)
cron.write()


# PATH="/Library/Frameworks/Python.framework/Versions/3.7/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/TeX/texbin"




# chmod a+x /Users/arthred/Documents/Flat_Crawler_Django/Flat_Crawler_Scrapy/Flat_Crawler_Scrapy/spiders/__init__.py



#PATH="/Library/Frameworks/Python.framework/Versions/3.7/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/TeX/texbin"
#cd /Users/arthred/Documents/Flat_Crawler_Django/Flat_Crawler_Scrapy/Flat_Crawler_Scrapy/spiders && sudo chown -R $(whoami) . && sudo chmod -R +rwX . && python __init__.py