<h1 align="center">
     Python Microservices (Integrated with Kafka)
</h1>

<h3 align="center">
     Technologies that were used:
</h3>

<p align="center">
   <img src="https://github.com/youngwishes/MSA/assets/92817776/0c233ba5-f0e4-44b8-b5ef-6608867e6d3b" width="50" height="50"/>
   <img src="https://github.com/youngwishes/MSA/assets/92817776/ecaae263-500a-4a80-b1ed-4296e830783c" width="50" height="50"/>
   <img src="https://github.com/youngwishes/MSA/assets/92817776/3675cec5-2b17-408c-88b8-de1a7737aef2" width="50" height="50"/>
   <img src="https://github.com/youngwishes/MSA/assets/92817776/c56eb267-fbac-4750-a473-deec88a84578" width="50" height="50"/>
   <img src="https://github.com/youngwishes/MSA/assets/92817776/acc192cb-42af-476f-9eb9-b66fe10f9164" width="50" height="50"/>
   <img src="https://github.com/youngwishes/MSA/assets/92817776/2d857681-aa69-4644-9b98-90eac1c876dd" width="50" height="50"/>
</p>
<p align="center">
   This project is an example of microservice architecture made on Python with Apache Kafka 💡
</p>

## Services:
 - web (FASTApi)
 - notify (Aiogram)
 - currency (Scrapy)



## How it works?
The first step is - user send request to **web service** on **FASTApi** with the only one ednpoint. This endpoint wait for two parameters: **currency char code** and **user telegram id**.
After that, **web service produce message to currency service**. Currency service is a spider that crawl info from [this open API](https://www.cbr.ru/scripts/xml_daily.asp) and it's works on python framework **Scrapy**.
At the end **currency service** produce message to **notify service** that just a **Telegram BOT** and its will send message **to user Telegram**.

_Also i missed point about caching in redis, but the project not about caching. You can see by yourself with more details in repo :)_

## Diagram
![image](https://github.com/youngwishes/MSA/assets/92817776/8c0bbc2c-0a38-43be-8fa1-3486a00e7558)

# Start locally

1. Clone repo

```
git clone https://github.com/youngwishes/fastapi-kafka.git
```
2. Create .env file and copy to it settings from .env.example
3. Go to **Bot Father** and get telegram bot **API toke**n. !!REMEMBER THAT BOT CANT SEND MESSAGE TO YOU IF YOU DON'T START THE DIALOG!!
```
docker compose up -d --build
```
4. Check that containers are ready. If anyone stopped - try to restart it:
```
docker restart <container-name>
```
**Thank you!**
