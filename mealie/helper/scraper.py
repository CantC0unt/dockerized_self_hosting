import requests
from bs4 import BeautifulSoup
import json
import time

# --- CONFIGURATION ---
MEALIE_URL = "http://eat.mealie"  # No trailing slash
API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb25nX3Rva2VuIjp0cnVlLCJpZCI6IjVmODBhZTllLWU0MDMtNGJjYy1iY2RmLTQxNTVhZjgwOTRjMiIsIm5hbWUiOiJTY3JhcGVyIEhlbHBlciIsImludGVncmF0aW9uX2lkIjoiZ2VuZXJpYyIsImV4cCI6MTkyMTEzMDI3Mn0.aeXcee4crhZXSfECiK-ISCwR-dps1GcvQ0Nl9R5b2ug"  # Get this from Mealie > User Settings > Manage API Tokens
# URL_LIST_FILE = "urls.txt"    # File containing one recipe URL per line
# ---------------------

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# def clean_text(text):
#     """
#     Cleans text by normalizing unicode characters (removing &nbsp;)
#     and stripping extra whitespace.
#     """
#     if not text: return ""
#     # Normalize to fix weird characters like Â
#     text = unicodedata.normalize("NFKC", text)
#     # Explicitly remove non-breaking spaces
#     text = text.replace('\xa0', ' ')
#     # Collapse multiple spaces into one
#     return " ".join(text.split())

def scrape_recipe(url):
    try:
        print(f"Fetching {url}...")
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.encoding = 'utf-8' # Ensure UTF-8
        
        if response.status_code != 200:
            print(f"Failed status: {response.status_code}")
            return None
            
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 1. Title
        title = soup.find('h1').get_text(strip=True) if soup.find('h1') else "Unknown Recipe"

        # 2. Locate Headers (Ingredients vs Method)
        all_h2 = soup.find_all('h2')
        ing_header = None
        method_header = None
        
        for h2 in all_h2:
            text = h2.get_text().lower()
            if 'ingredient' in text:
                ing_header = h2
            elif 'method' in text:
                method_header = h2

        ingredients = []
        instructions = []

        # 3. Extract Ingredients
        # Logic: grab everything between 'Ingredients' header and 'Method' header
        if ing_header:
            curr = ing_header.next_sibling
            while curr and curr != method_header:
                if hasattr(curr, 'find_all'):
                    for li in curr.find_all('li'):
                        clean = li.get_text()
                        if clean:
                            # --- THE FIX ---
                            # Use "original" so Mealie parses "2 cups flour" 
                            # into Qty: 2, Unit: cups, Food: flour
                            ingredients.append({"original": clean})
                curr = curr.next_sibling

        # 4. Extract Instructions
        # Logic: grab everything after 'Method' header
        if method_header:
            curr = method_header.next_sibling
            while curr:
                if hasattr(curr, 'find_all'):
                    for li in curr.find_all('li'):
                        clean = li.get_text()
                        if clean:
                            instructions.append({
                                "@type": "HowToStep",
                                "text": clean
                            })
                curr = curr.next_sibling

        # 5. Image extraction
        image_url = ""
        img_tag = soup.find('img', id='imgRecipe')
        if img_tag:
            image_url = img_tag.get('src')
        else:
            # Fallback: find first image in post container
            container = soup.find('div', id='post-container')
            if container:
                imgs = container.find_all('img')
                if imgs: image_url = imgs[0].get('src')

        # Construct Payload
        recipe_data = {
            "name": title,
            "recipeIngredient": ingredients,
            "recipeInstructions": instructions,
            "orgURL": url,
            "image": image_url
        }
        
        return recipe_data
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

def import_to_mealie(recipe_data):
    api_endpoint = f"{MEALIE_URL}/api/recipes"
    
    # Use create endpoint
    response = requests.post(api_endpoint, json=recipe_data, headers=headers)
    
    if response.status_code == 201:
        print(f"SUCCESS: Imported '{recipe_data['name']}'")
    elif response.status_code == 409:
        print(f"SKIPPED: '{recipe_data['name']}' (Already exists)")
    else:
        print(f"FAILED: {response.status_code} - {response.text}")


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    try:
        # with open(URL_LIST_FILE, 'r') as f:
        #     urls = [line.strip() for line in f if line.strip()]
            
        urls = [
            "https://www.sanjeevkapoor.com/Recipe/chatpatta-guava-popsicle-9311195",
        ]
        print(f"Found {len(urls)} recipes to process...")
        
        for url in urls:
            data = scrape_recipe(url)
            if data:
                print(data)
                import_to_mealie(data)
            time.sleep(1) 
            
    except FileNotFoundError:
        print(f"Error: {URL_LIST_FILE} not found. Please create it with a list of URLs.")