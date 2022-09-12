## <div align="center"> Commerce

#### <div align="center">📚 _CS50 Web Project # 2 (Week 5) 08/16 - 08/\_\_/2022_ </div>

**_<p align="right">By Daniel Adeyemi_**</p>

<p align="center">
<img alt="HTML5" width="30px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png" />
<img alt="CSS3" width="30px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png" />
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="30"/>
<img alt="django" width="30px" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-plain.svg" />

</p>
<div align="center">

![GitHub last commit (branch)](https://img.shields.io/github/last-commit/DanielAdeyemi/CS50W_Project_2/main?color=purple&style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/DanielAdeyemi/CS50W_Project_2?color=purple&style=for-the-badge) ![Languages](https://img.shields.io/github/languages/top/DanielAdeyemi/CS50W_Project_2?color=purple&style=for-the-badge)

</div>
<p align="center"><img src="https://assets-global.website-files.com/600fe6e1ff56087409a9f096/60537020dbb180813c767e63_ebay.jpg" alt="ebaylogo" height="250px"/> </p>

## 🚩 _Description:_

#### **_An eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”_**

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

<summary><h3>📋 Project Specifications </h3></summary>
<details>

|   #   |           Block            |                                                                                                                                     Task Description                                                                                                                                     | Status |
| :---: | :------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----: |
| **0** |        **Project**         |                                                                                                                      **_Project creation and github link, README_**                                                                                                                      |   ✅   |
| **1** |         **Models**         |                                                                                                       **_Application should have at least 3 models in addition to `User` model_**                                                                                                        |   ✅   |
|  1a   |           Models           |                                                                                                                           Create a model for auction listings                                                                                                                            |   ✅   |
|  1b   |           Models           |                                                                                                                                 Create a model for bids                                                                                                                                  |   ✅   |
|  1c   |           Models           |                                                                                                                      Create a model for comments on auction listing                                                                                                                      |   ✅   |
| **2** |     **Create Listing**     |                                                                                                           **_Users should be able to visit a page to create a new listing._**                                                                                                            |   ❌   |
|  2a   |       Create Listing       |                                                                                  User should be able to specify a title for the listing, a text-based description, and what the starting bid should be.                                                                                  |   ✅   |
|  2b   |       Create Listing       |                                                                   Users should also optionally be able to provide a URL for an image for the listing and/or a category (e.g. Fashion, Toys, Electronics, Home, etc.).                                                                    |   ✅   |
| **3** |  **Active Listing Page**   |                                                                                               **_The default route should let users view all of the currently active auction listings._**                                                                                                |   ❌   |
|  3a   |    Active Listing Page     |                                                                     For each active listing, this page should display (at minimum) the title, description, current price, and photo (if one exists for the listing).                                                                     |   ❌   |
| **4** |      **Listing Page**      |                                         **_Clicking on a listing should take users to a page specific to that listing. On that page, users should be able to view all details about the listing, including the current price for the listing._**                                         |   ❌   |
|  4a   |        Listing Page        |                                                          If the user is signed in, the user should be able to add the item to their “Watchlist.” If the item is already on the watchlist, the user should be able to remove it.                                                          |   ❌   |
|  4b   |        Listing Page        | If the user is signed in, the user should be able to bid on the item. The bid must be at least as large as the starting bid, and must be greater than any other bids that have been placed (if any). If the bid doesn’t meet those criteria, the user should be presented with an error. |   ❌   |
|  4c   |        Listing Page        |                        If the user is signed in and is the one who created the listing, the user should have the ability to “close” the auction from this page, which makes the highest bidder the winner of the auction and makes the listing no longer active.                         |   ❌   |
|  4d   |        Listing Page        |                                                                                       If a user is signed in on a closed listing page, and the user has won that auction, the page should say so.                                                                                        |   ❌   |
|  4e   |        Listing Page        |                                                               Users who are signed in should be able to add comments to the listing page. The listing page should display all comments that have been made on the listing.                                                               |   ❌   |
| **5** |       **Watchlist**        |                                                                                                         **_Users who are signed in should be able to visit a Watchlist page._**                                                                                                          |   ❌   |
|  5a   |         Watchlist          |                                                          Watchlist should display all of the listings that a user has added to their watchlist. Clicking on any of those listings should take the user to that listing’s page.                                                           |   ❌   |
| **6** |       **Categories**       |                                                                                                **_Users should be able to visit a page that displays a list of all listing categories._**                                                                                                |   ❌   |
|  6a   |         Categories         |                                                                              Clicking on the name of any category should take the user to a page that displays all of the active listings in that category.                                                                              |   ❌   |
| **7** | **Django Admin Interface** |                                                               **_Via the Django admin interface, a site administrator should be able to view, add, edit, and delete any listings, comments, and bids made on the site._**                                                                |   ❌   |

<!-- ❌  ✅     -->

</details>
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

## 🛠️ _Technologies used:_

- Python 3.9.5
- Django 4.0.4
- HTML 5
- CSS 3
- Git and GitHub

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

## 🖥️ View the project:

You can access video demonstration of the project functionallity when the project is finished

<!-- [here](https://youtu.be/xdFXzDSagz0)    -->
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

## 🐛 _Known bugs:_

- no bugs at this time

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

## 🌟 _Improvement opportunities:_

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

## 📬 Contact Information

#### For any questions _[email author](mailto:adeyemidany+github@gmail.com?subject=[GitHubAPI])_

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

## 📘 _License and copyright:_

> **_© Daniel Adeyemi, 2022_**  
> ⚖️ _[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)_
