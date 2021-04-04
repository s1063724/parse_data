from bs4 import BeautifulSoup

def main():
    path = 'H:/PycharmProjects/parse_data/'
    file = open(path, 'r')
    htmlhandle = file.read()
    soup = BeautifulSoup(htmlhandle, 'html.parser')
    table =soup.find_all('table', {"id": "CPH1_tb_jobQueryResult"})
    elements = table.find_all("tr", {"class": "post"})
    data = [element.getText() for element in elements]


if __name__ == '__main__':
    main()
