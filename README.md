# "Support" API

## URLs (allowed methods are indicated in brackets):

```
/api/v1/registration/                   <- user registration (POST)

/api/v1/token/                          <- getting access and refresh tokens (POST) 

/api/v1/token/refresh/                  <- getting a new access token (POST)

/api/v1/token/verify/                   <- token validity check (POST)

/api/v1/tickets/                        <- receiving and creating tickets (GET, POST)

/api/v1/tickets/{ticket_pk}/            <- getting a separate ticket (GET)

/api/v1/ticket/{ticket_pk}/messages/    <- receiving and creating ticket messages (GET, POST)
```

