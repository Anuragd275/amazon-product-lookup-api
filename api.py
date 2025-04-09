import os
from dotenv import load_dotenv
from amazon_paapi import AmazonApi

load_dotenv()

# LOAD ENVIRONMENT VARIABLES
SECRET_KEY = os.getenv('SECRET_KEY')
ACCESS_KEY = os.getenv('ACCESS_KEY')
TAG = os.getenv('TAG')
COUNTRY = os.getenv('COUNTRY')

amazon = AmazonApi(SECRET_KEY, ACCESS_KEY, TAG, COUNTRY)

def get_item_details(asin):

    item = amazon.get_items(asin)[0]
        
    title = item.item_info.title.display_value
    deal_price = item.offers.listings[0].price.amount
    original_price = item.offers.listings[0].saving_basis.amount
    discount = item.offers.listings[0].price.savings.percentage
    category = item.browse_node_info.browse_nodes[0].display_name if item.browse_node_info and item.browse_node_info.browse_nodes else 'Unknown'
    product_id = item.asin
    image_url = item.images.primary.large.url if item.images and item.images.primary and item.images.primary.large else 'No Image'
    product_url = item.detail_page_url if hasattr(item, 'detail_page_url') else 'No URL'
    store = 'amazon'

    return {
        "title": title,
        "deal_price": deal_price,
        "original_price": original_price,
        "discount": discount,
        "category": category,
        "product_id": product_id,
        "image_url": image_url,
        "product_url": product_url,
        "store": store
    }