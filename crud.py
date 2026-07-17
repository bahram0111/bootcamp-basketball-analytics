from sqlalchemy.orm import Session



def create(session: Session, model, data: dict):

    obj = model(**data)

    session.add(obj)

    return obj


def create_many(session: Session, model, data: list[dict]):

    objects = [model(**row) for row in data]

    session.add_all(objects)

    return objects