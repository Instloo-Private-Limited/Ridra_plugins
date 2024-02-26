from django.shortcuts import render, HttpResponse
import requests
from bs4 import BeautifulSoup

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
    context = {
        'Price' : '{}'.format(gold_price)
    }

    # return HttpResponse("{}".format(gold_price))
    return render(request, 'Price.html', context=context)