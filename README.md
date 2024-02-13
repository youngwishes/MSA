<h1 align="center">
     Python Microservices (Integrated with Kafka)
</h1>

<h3 align="center">
     Technologies used:
</h3>

<p align="center">
   <img src="https://github.com/youngwishes/fastapi-kafka/assets/92817776/19c422d7-806d-4fe4-9773-bd789c2f4e78" width="50" height="50"/>
   <img src="https://github.com/youngwishes/fastapi-kafka/assets/92817776/e27bcc09-b947-4b27-88b4-94c6922eecfb" width="50" height="50"/>
   <img src="https://github.com/youngwishes/fastapi-kafka/assets/92817776/a9d9c54f-124d-425e-8691-ef11bf131d46" width="50" height="50"/>
   <img src="https://github.com/youngwishes/fastapi-kafka/assets/92817776/c5adda28-6ae4-4bd3-ae9d-676104b74dae" width="50" height="50"/>
   <img src="https://github.com/youngwishes/fastapi-kafka/assets/92817776/a824c8aa-89cb-4d22-9706-c2a5affb98a0" width="50" height="50"/>
   <img src="https://github.com/youngwishes/fastapi-kafka/assets/92817776/325440cb-2f74-4fdc-a4e2-85bc55000727" width="50" height="50"/>
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
![image](https://github.com/youngwishes/fastapi-kafka/assets/92817776/e4c032f1-e7b8-4d47-9262-ca14c6ee4f05)

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
