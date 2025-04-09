# 📦 Amazon Product Lookup API

This is a simple Flask-based API that fetches product details from Amazon using the [Amazon Product Advertising API (PAAPI)](https://github.com/sergioteula/python-amazon-paapi).  
You can retrieve product information by providing an **ASIN (Amazon Standard Identification Number)** via the `/<asin>` endpoint.

---

## 🚀 Features

- 🔍 Retrieve product title, price, original price, and discount
- 🖼️ Fetch image URL and product URL
- 🛒 Get product category and ASIN
- 🏷️ Built on top of `amazon-paapi` Python wrapper

---

## 📦 Requirements

- Python 3.7+
- Amazon Product Advertising API credentials
- Flask
- `amazon-paapi` package


Clone this repository:
```
git clone https://github.com/yourusername/amazon-product-lookup-api.git
```

Navigate to the cloned directory:
```
cd amazon-product-lookup-api
```

Install the dependencies using:
```
pip install -r requirements.txt
```

---
### create .env file and set your own values

```
"SECRET_KEY="
"ACCESS_KEY="
"TAG="
"COUNTRY="
```

Run app.py by
```
python app.py
```
---

## Example

Request
```
curl http://127.0.0.1:5000/api/v1/product/B08FXP565F
```

Response
```
{
  "category": "Bottles",
  "deal_price": 510.66,
  "discount": 59,
  "image_url": "https://m.media-amazon.com/images/I/31tVNLeiC5L._SL500_.jpg",
  "original_price": 1250.0,
  "product_id": "B08FXP565F",
  "product_url": "https://www.amazon.in/dp/B08FXP565F?tag=buy-smart-21&linkCode=ogi&th=1&psc=1",
  "store": "amazon",
  "title": "Amazon Brand - Solimo Stainless Steel Insulated Flask 24 Hours Hot And Cold Bottle (Silver,750 Ml)"
}
```