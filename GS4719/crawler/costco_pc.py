from bs4 import BeautifulSoup
import requests

def check_costco_pc():
    costco_pc_page = requests.get('https://www.costco.com.tw/Computers/Tablets-Laptops-Desktops/Tablets-Laptops/c/20201')
    costco_pc_page_text = costco_pc_page.text
    costco_pc_bs4_obj = BeautifulSoup(costco_pc_page_text, 'html.parser')
    
    return costco_pc_bs4_obj.select('div.search-layout-btn-container div.search-pagination-container span')[0].text

if __name__ == '__main__':
    print(check_costco_pc())