def main():
    path = 'H:\PycharmProjects\parse_data\job.txt'
    file = open(path, 'r', encoding='utf-8')
    lines = file.read()
    print(lines)


if __name__ == '__main__':
    main()
