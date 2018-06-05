from base import Base, Session, engine
from bases.city import City
from bases.person import Person

# - generate the database schema
Base.metadata.create_all(engine)

# - start a new session
session = Session()


def main():
    # - creating the data
    parnaiba = City("Parnaíba", "PI")
    teresina = City("Teresina", "PI")
    fortaleza = City("Fortaleza", "CE")
    person = Person("Luiz", "Rodrigo", 21)

    person.city = parnaiba

    # - persisting the data
    session.add(parnaiba)
    session.add(teresina)
    session.add(fortaleza)
    session.add(person)

    session.commit()

    # - selecting the cities
    search_query = session.query(City).all()

    print("Cities:")
    for city in search_query:
        print("\t-{}".format(city.name))

    # - making a join
    search_query = session.query(Person).join(Person.city)

    for person in search_query:
        print("First name: {} \nCity: {}".format(
            person.first_name,
            person.city.name
        ))

    # - deleting the data
    session.query(Person).delete()
    session.query(City).delete()
    session.commit()

    session.close()


if __name__ == '__main__':
    main()
