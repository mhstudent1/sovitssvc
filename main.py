from Person import Person as p
def main():
    person = p("苗辉", 25)
    person.show()
    with open('./person.txt', 'w') as f:
        f.write(str(person))
if __name__ == '__main__':
    main()