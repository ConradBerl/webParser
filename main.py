import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

    # Store the webpages locally
    # -----------------------------------
    r_SAIL = requests.get('https://www.sail.ca/en/lowa-renegade-mid-men-s-gore-tex-hiking-boots-684550')
    r_Bushtaka = requests.get('https://shop.bushtukah.com/product/lowa-renegade-gtx-mid-wide-sizes-available-mens-36628.htm').text
    r_TrailHead = requests.get('https://www.trailheadpaddleshack.ca/lowa-renegade-gtx-mid-hiking-boots-mens.html').text


    # Create BeautifulSoup object
    # -----------------------------------
    html_SAIL = BeautifulSoup(r_SAIL.content, 'html.parser')
    html_Bushtaka = BeautifulSoup(r_Bushtaka, 'html.parser')
    html_TrailHead = BeautifulSoup(r_TrailHead, 'html.parser')


    # Parse each site to find the price line
    # -----------------------------------
    # Hint: Use Chrome's 'inspect element' [ CRTL+SHIFT+i ] to drill down and find the price line
    price_SAIL_line = html_SAIL.find("span", "price")

    price_Bushtaka_line = html_Bushtaka.find("div", "seRegularPrice")
    originalPrice_Bushtaka_line = html_Bushtaka.find("div", "seOriginalPrice")
    salePrice_Bushtaka_line = html_Bushtaka.find("div", "seSpecialPrice")

    price_TrailHead_line = html_TrailHead.find("span", "price")
    oldPrice_TrailHead_line = html_TrailHead.find("span", "old-price")


    # Parse each list to extract the price
    # -----------------------------------
    price_SAIL = price_SAIL_line.contents[0]
    print("SAIL price: " + price_SAIL)

    # check if there exists an original price
    if not price_Bushtaka_line:
        originalPrice_Bushtaka = originalPrice_Bushtaka_line.contents[0]
        print("Bushtaka price: " + originalPrice_Bushtaka)
        salePrice_Bushtaka = salePrice_Bushtaka_line.contents[0]
        print("Bushtaka Sale Price: " + salePrice_Bushtaka)
    else:
        price_Bushtaka = price_Bushtaka_line.contents[0]
        print("Bushtaka price: " + price_Bushtaka)

    # check if the sale price is an empty list
    if not oldPrice_TrailHead_line:
        price_TrailHead = price_TrailHead_line.contents[0]
        price_TrailHead = price_TrailHead[1:]
        print("TrailHead price: " + price_TrailHead)
    else:
        price_TrailHead = oldPrice_TrailHead_line.contents[0]
        price_TrailHead = price_TrailHead[1:]
        salePrice_TrailHead = price_TrailHead_line.contents[0]
        salePrice_TrailHead = salePrice_TrailHead[1:]
        print("TrailHead price: " + price_TrailHead)
        print("TrailHead Sale Price: " + salePrice_TrailHead)