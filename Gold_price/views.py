from django.shortcuts import render, HttpResponse
import requests
from bs4 import BeautifulSoup
from .models import gold

def get_gold_prices():
    url = "https://www.gadgets360.com/finance/gold-rate-in-india/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the element that contains the gold price
        gp = soup.find("li", class_="_crprw _flx")
        gold_price_element = gp.find("span")
        
        if gold_price_element:
            gold_price = gold_price_element.text.strip()
            return gold_price
        
    return "Unable to retrieve gold prices"
    

# Create your views here.
def Price(request):
    gold_price = get_gold_prices()
    price = int(gold_price.split(' ')[1].replace(',',''))
    final_price = 0
    
    p = gold.objects.get(pk=1)

    if price - p.price > 500 or price - p.price < 700:
        final_price = gold_price
        p.price = price
        p.save()
    else:
        final_price = "₹ " + str(p.price)

    
    context = {
        'Price' : '{}'.format(final_price)
    }
    # return HttpResponse("{}".format(gold_price))
    return render(request, 'Price.html', context=context)