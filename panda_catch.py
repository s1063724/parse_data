import pandas as pd


def main():
    path = 'H:\PycharmProjects\Web_crawler\job_info.html'
    htmlfile = open(path, 'r')
    job_table = pd.read_html(htmlfile)
    print("型態：", type(job_table))
    print("長度：", len(job_table))
    job_df = job_table[0]
    print(job_df)


if __name__ == '__main__':
    main()
