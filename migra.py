from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from src.infrastructure.database.adapters.database import get_db
from src.infrastructure.models import Company, Order


def fix_sequence_numbers():

    with get_db() as session:
        companies = session.query(Company).all()

        for company in companies:
            # Har bir kompaniya uchun orderlarni tartib bo'yicha olish
            orders = session.query(Order).filter_by(
                company_id=company.id).order_by(Order.datetime).all()

            # sequence_number ni 1 dan boshlab yangilash
            for index, order in enumerate(orders, start=1):
                order.sequence_number = index

            # Kompaniyaning current_sequence ni yangilash
            company.current_sequence = len(orders)

        # O'zgarishlarni saqlash
        session.commit()


if __name__ == "__main__":
    fix_sequence_numbers()
    print("Sequence numbers have been fixed.")
