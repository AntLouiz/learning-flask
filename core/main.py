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

    # - commiting and close
    session.commit()

    search_query = session.query(City).all()

    for city in search_query:
        print(city.name)

    session.query(Person).delete()
    session.query(City).delete()
    session.commit()

    session.close()


if __name__ == '__main__':
    main()
