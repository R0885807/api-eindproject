
# API-eindproject

- Mijn hosted **API** link: **https://chess-api-service-r0885807.cloud.okteto.net/**


## Beschrijving
Het thema van mijn API is **schaken**. Sinds kort is schaken een kleine nieuwe hobby geworden van mij. Het is een API-service met een database gemaakt met SQLite.
De API en database zijn gehost op **Okteto*.

## Database
Hier is een tabel over de database:
![database](https://user-images.githubusercontent.com/91954479/211392059-2c0cba5e-6448-47dd-aeb5-9918dcb7d10e.png)



## Endpoints

### Get endpoint 1

Get endpoint 1: https://chess-api-service-r0885807.cloud.okteto.net/player/{player_id}. Geeft een object terug met data over player met player_id: {player_id}.

*Note: De wachtwoorden "dummypassword" zijn manueel toegevoegd in de database en zijn daarom niet gehashed, de gebruiker "Robbe Verbist" is via een api endpiont toegevoegd en dat wachtwoord is wel gehashed.*

![Get1](https://user-images.githubusercontent.com/91954479/211388992-09db970b-3ae0-43dc-b67e-22a95efb7f4d.png)

### Get endpoint 2

Get endpoint 2: https://chess-api-service-r0885807.cloud.okteto.net/players/. Geeft als default 5 players weer, maar het aantal kan aangepast worden met queryparameters bv: https://chess-api-service-r0885807.cloud.okteto.net/players/?skip=0&limit=3. Dit geeft 3 players weer.

![Get2](https://user-images.githubusercontent.com/91954479/211388994-dc036626-a7cc-4359-b94d-5b3163d7ca7d.png)

### Get endpoint 3

Get endpoint 3: https://chess-api-service-r0885807.cloud.okteto.net/opener/{opener_id}. Geeft een object terug met data over een officieel benaamde opener in schaken.

![Get3](https://user-images.githubusercontent.com/91954479/211388997-30b2479f-d8ce-41bb-bcab-3574db643b6c.png)

### Get endpoint 4

Get endpoint 4: https://chess-api-service-r0885807.cloud.okteto.net/stat/{stat_id}. Geeft een object terug met data over de statistieken met stat_id: {stat_id}.

![Get4](https://user-images.githubusercontent.com/91954479/211388998-2414c316-0ce7-4b89-a798-f5d734c48939.png)

### Post endpoint 1

Post endpoint 1: https://chess-api-service-r0885807.cloud.okteto.net/token/. Dit is de endpoint om een access token te krijgen voor de andere endpoints te kunnen gebruiken.

![Post1](https://user-images.githubusercontent.com/91954479/211389000-1c7bac7f-294a-41f9-8b5e-025e77b63e60.png)

### Post endpoint 2

Post endpoint 2: https://chess-api-service-r0885807.cloud.okteto.net/player/. Dit is de endpoint om een object player aan te maken. De info moet in de body.

![Post2](https://user-images.githubusercontent.com/91954479/211389003-ff96edd1-2cb5-4159-9087-746bd0e9ab86.png)

### Post endpoint 3

Post endpoint 3: https://chess-api-service-r0885807.cloud.okteto.net/stat/. Dit is de endpoint om een object stat aan te maken. De info moet in de body.

![Post3](https://user-images.githubusercontent.com/91954479/211389004-e9857478-17f2-4969-a301-b1d072aeb6c4.png)

### Put endpoint

Put endpoint: https://chess-api-service-r0885807.cloud.okteto.net/stat/. Dit is de endpoint om een object opener aan te maken. De info moet in de body.

![Put](https://user-images.githubusercontent.com/91954479/211389006-9edbf42c-60e9-4c6b-8427-3bafdf2445da.png)

### Delete endpoint

Delete endpoint: https://chess-api-service-r0885807.cloud.okteto.net/opener/{opener_id}. Dit is de endpoint om een object opener te verwijderen uit de databast met id: {opener_id}.
When using the delete endpoint, you get a 500 error, but the opener still gets deleted, so it still works. The second time it does not find the opener.

![Delete error](https://user-images.githubusercontent.com/91954479/211388983-83dd9824-ad78-4a0a-a632-40ea1035638e.png)
![Delete not found](https://user-images.githubusercontent.com/91954479/211388991-c751f8e5-d8d5-47af-a7a6-b7dedba66863.png)

## Full OpenApi docs
![Openapi1](https://user-images.githubusercontent.com/91954479/211393666-4eef9a17-22c2-4400-ada1-4bb211376143.png)
![Openapi2](https://user-images.githubusercontent.com/91954479/211391151-4c87e860-08e2-4e42-8d38-ae2b38e5309a.png)
![Openapi3](https://user-images.githubusercontent.com/91954479/211391156-f6353bc7-e829-46c0-acd5-518a014281fa.png)
![Openapi4](https://user-images.githubusercontent.com/91954479/211391158-f7c2abad-b227-44de-9a9e-ef4fb8e7ae5d.png)
![Openapi5](https://user-images.githubusercontent.com/91954479/211391160-51c7d72f-4539-445f-9b1f-b76be968716d.png)
![Openapi6](https://user-images.githubusercontent.com/91954479/211391161-326e36fe-ee48-4d6f-abdd-a5a62f1fb323.png)
![Openapi7](https://user-images.githubusercontent.com/91954479/211391162-7d3068e5-6d3b-433f-918a-5f57af9fa1ab.png)
![Openapi8](https://user-images.githubusercontent.com/91954479/211391163-464642fc-24f0-4e94-adb9-45026665ae84.png)
![Openapi9](https://user-images.githubusercontent.com/91954479/211391165-8e130022-c088-4441-ab32-348995b8bb10.png)
![Openapi10](https://user-images.githubusercontent.com/91954479/211391167-9b58dac6-fb47-4029-b9a6-bd64d578e1d3.png)
![Openapi11](https://user-images.githubusercontent.com/91954479/211391168-d033e2ac-ec81-489b-8e56-642055940c97.png)
![Openapi12](https://user-images.githubusercontent.com/91954479/211391170-5544fd92-5f73-4f30-beca-256e8286a599.png)
![Openapi13](https://user-images.githubusercontent.com/91954479/211391173-0dd3ffaf-b401-4a75-be3a-6ff5ed4ebfa7.png)
