<img src=".github/assets/wordmark-impact.svg" width="100%" alt="Denis7Kom" />

## Denis Komarov

I build web applications and interactive simulations. I study application security, with a particular interest in what happens between a user clicking a button and the server deciding whether to allow the request.

[Portfolio](https://denis7kom.github.io/denis-komarov/) · [Photography & aerial video](https://denis7kom.github.io/Denis-Komarov-PH/) · [Books](https://www.amazon.it/stores/Denis-Komarov/author/B0CCSK74QC)

## Featured project

### [VibeShop](https://github.com/Denis7Kom/website-turbo-layout)

A live-music storefront built with Ivan Perruolo and Giulio Alessandro Peluso at the University of Salerno. Visitors can browse concerts and merchandise. Customers can check out and review past orders. Administrators manage the catalogue and support requests.

**Inside the stack** · JSP renders the storefront, Java Servlets handle requests, and DAO classes read and write order data in SQL.

[Explore the controllers](https://github.com/Denis7Kom/website-turbo-layout/tree/main/VibeShop/src/main/java/com/turbolayout) · [View the database schema](https://github.com/Denis7Kom/website-turbo-layout/blob/main/VibeShop/db/VIBESHOP_FINAL.sql)

## Interactive projects

**[Virtual aviation](https://denis7kom.github.io/denis-aviation/)** — An aviation portfolio with interactive aircraft and a flight booking interface. [Source](https://github.com/Denis7Kom/denis-aviation)

**[SQUAD](https://denis7kom.github.io/SQUAD/)** — A squad leadership ranking system and a tactical match simulator. Explore how command structure, orders and supply affect a team. [Source](https://github.com/Denis7Kom/SQUAD)

## Application security

One question I use when reviewing an order-history endpoint is simple. If two customers are signed in, what happens when one requests the other’s order ID? I trace the request from the session to the database lookup, find where ownership is checked, and test both accounts.
