import requests
from bs4 import BeautifulSoup

URL = "https://www.jumia.com.ng/groceries/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

food_items = soup.find_all(class_='food-item')
for item in food_items:
    name = item.find(class_='item-name').get_text()
    price = item.find(class_='item-price').get_text()
    print(f"Food Item: {name}, Price: {price}")
    description = item.find(class_='item-description').get_text()
    print(f"Description: {description}\n")
    location = Location.objects.first()
    FoodItem.objects.create(
        name=name,
        description=description,
        price=float(price.replace('$', '')),
        location=location
    )
    PricePoint.objects.create(
        location=location,
        price=float(price.replace('$', ''))
    )
def scrape_food_items(url, location_id):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    food_items = []
    for item in soup.select('.food-item'):
        name = item.select_one('.item-name').text
        description = item.select_one('.item-description').text
        price = float(item.select_one('.item-price').text.replace('$', ''))

        food_item, created = FoodItem.objects.get_or_create(
            name=name,
            location_id=location_id,
            defaults={'description': description, 'price': price}
        )

        if not created:
            food_item.description = description
            food_item.price = price
            food_item.save()

        food_items.append(food_item)

        PricePoint.objects.create(
            location_id=location_id,
            price=price
        )

    return food_items
