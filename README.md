# API for keynote "Docker, Web Scraping and Django Rest Framework: building a complete application." for GORN event 

Scraping on the Real Python website, serving this data in an API made with
Django Rest Framework and Docker to set up the environment.

## Run


Rename sample.env to .env

```bash
mv ample.env .env
```

Enter your database information:

```
POSTGRES_DB=gorn
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```


```docker
docker-compose up
```