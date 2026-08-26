from flask import current_app
from sqlalchemy import exc

from enferno.extensions import db


class BaseMixin:
    def save(self, commit=True):
        db.session.add(self)
        if commit:
            try:
                db.session.commit()
                return self
            except exc.SQLAlchemyError as e:
                current_app.logger.error(f"Database save error: {e}")
                db.session.rollback()
                return None

    def delete(self, commit=True):
        db.session.delete(self)
        if commit:
            try:
                db.session.commit()
                return self
            except exc.SQLAlchemyError as e:
                current_app.logger.error(f"Database delete error: {e}")
                db.session.rollback()
                return None
