![Image of Website](https://i.imgur.com/6IFLuJb.png)
# Covid Tracker

Covid Tracker uses an API to fetch upto-date Corona Virus information.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
1. Clone the repo.

2. Install all the requirements
```
pip install -r requirements.txt
```
3. Go to ``` main/views.py ``` &
replace ```yourkeyhere``` in ```'x-rapidapi-key': "yourkeyhere"``` with the key you get from: [https://rapidapi.com/api-sports/api/covid-193](https://rapidapi.com/api-sports/api/covid-193)
4. Go to ```main/views.py``` &
replace ```yourcountryhere``` in ```querystring = {"country": "yourcountryhere"}``` with the country you'd like to show the data of.
5. Done! now run the project with ```python manage.py runserver``` 

## Deployment

follow instructions given on [This link](https://devcenter.heroku.com/categories/working-with-django)

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Covid API](https://rapidapi.com/api-sports/api/covid-193) - The API used

## Authors

* **Maitreya Patni** - *Everything* - [Github](https://github.com/Maitreya29) [Website](https://maitreyap.xyz)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

