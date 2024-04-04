import csv, requests, re
from bs4 import BeautifulSoup


def get_name_address_list():
    filename = "target_address.csv"

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        lists = []
        for row in reader:
            if len(row) == 2 and row[1] != "":
                lists.append((row[0], row[1]))
        return lists


def sales_index_crawling(name_address_list):
    response_data = []
    for name, url in name_address_list:
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        info_element = soup.select_one(
            "#yDetailTopWrap > div.topColRgt > div.gd_infoTop > span.gd_ratingArea > span.gd_sellNum"
        )
        data = int(re.sub(r"[^\d]", "", info_element.text))

        response_data.append((name, data))
    return response_data


print(sales_index_crawling(get_name_address_list()))
