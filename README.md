# API-eindproject

- Mijn hosted **API** link: **https://chess-api-service-r0885807.cloud.okteto.net/**


## Beschrijving
Het thema van mijn API is **schaken**. Sinds kort is schaken een kleine nieuwe hobby geworden van mij. Het is een API-service met een database gemaakt met SQLite.
De API en database zijn gehost op **Okteto*.

## Endpoints

### Get endpoint 1

Get endpoint 1: https://chess-api-service-r0885807.cloud.okteto.net/player/{player_id}. Geeft een object terug met data over player met player_id: {player_id}.

*Note: De wachtwoorden "dummypassword" zijn manueel toegevoegd in de database en zijn daarom niet gehashed, de gebruiker "Robbe Verbist" is via een api endpiont toegevoegd en dat wachtwoord is wel gehashed.*
![Get "/player/{player_id}"](https://github.com/R0885807/api-project/blob/main/screenshots/Get%20guitars.png)

### Get endpoint 2

Get endpoint 2: https://chess-api-service-r0885807.cloud.okteto.net/players/. Geeft als default 5 players weer, maar het aantal kan aangepast worden met queryparameters bv: https://chess-api-service-r0885807.cloud.okteto.net/players/?skip=0&limit=3. Dit geeft 3 players weer.

### Get endpoint 3

Get endpoint 3: https://chess-api-service-r0885807.cloud.okteto.net/opener/{opener_id}. Geeft een object terug met data over een officieel benaamde opener in schaken.

### Get endpoint 4

Get endpoint 4: https://chess-api-service-r0885807.cloud.okteto.net/stat/{stat_id}. Geeft een object terug met data over de statistieken met stat_id: {stat_id}.

### Post endpoint 1

Post endpoint 1: https://chess-api-service-r0885807.cloud.okteto.net/token/. Dit is de endpoint om een access token te krijgen voor de andere endpoints te kunnen gebruiken.

### Post endpoint 2

Post endpoint 2: https://chess-api-service-r0885807.cloud.okteto.net/player/. Dit is de endpoint om een object player aan te maken. De info moet in de body.

### Post endpoint 3

Post endpoint 3: https://chess-api-service-r0885807.cloud.okteto.net/stat/. Dit is de endpoint om een object stat aan te maken. De info moet in de body.

### Put endpoint

Put endpoint: https://chess-api-service-r0885807.cloud.okteto.net/stat/. Dit is de endpoint om een object opener aan te maken. De info moet in de body.

### Delete endpoint

Delete endpoint: https://chess-api-service-r0885807.cloud.okteto.net/opener/{opener_id}. Dit is de endpoint om een object opener te verwijderen uit de databast met id: {opener_id}.
