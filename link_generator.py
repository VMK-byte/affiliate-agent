import urllib.parse
import pyshorteners


def generate_affiliate_link(product_id: str, tag: str) -> str:
    base_url = 'https://www.amazon.com/dp/'
    affiliate_url = urllib.parse.urljoin(base_url, product_id)
    # Adding the affiliate tag to the URL
    query = {'tag': tag}
    affiliate_url += '?' + urllib.parse.urlencode(query)
    
    # Shortening the URL
    s = pyshorteners.Shortener()  
    short_url = s.tinyurl.short(affiliate_url)
    return short_url


# Example usage
if __name__ == '__main__':
    product_id = 'example_product_id'
    tag = 'example_affiliate_tag'
    print(generate_affiliate_link(product_id, tag))