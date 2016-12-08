from sqlalchemy import Column, Integer, String, Sequence
import sqlalchemy
import os
import sqlalchemy.orm
import sqlalchemy.ext.declarative
from sqlalchemy.pool import SingletonThreadPool
from PySide import QtCore

data_directory = os.path.expanduser("~/.lightningmf")
if not os.path.exists(data_directory):
    os.makedirs(data_directory)

confFile = os.path.join(data_directory, "conf.json")

cstring = "sqlite:///" + os.path.join(data_directory, "db.sqlite")
engine = sqlalchemy.create_engine(cstring, poolclass=SingletonThreadPool)


class Base(object):
    @sqlalchemy.ext.declarative.declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    @sqlalchemy.ext.declarative.declared_attr
    def id(cls):
        return Column(Integer, Sequence(cls.__name__.lower() + "_id_seq"), primary_key=True)


Base = sqlalchemy.ext.declarative.declarative_base(cls=Base)


def Many2One(class_name, **kwargs):
    return Column(Integer, sqlalchemy.ForeignKey(class_name.lower() + ".id"), **kwargs)


class Game(Base):
    name = Column(String(50), nullable=False, index=True)
    description = Column(String(200), nullable=False, index=True)
    year = Column(String(10), nullable=False)
    manufacturer = Column(String(70), nullable=False)
    status = Column(String(50), nullable=False)

# session
Session = sqlalchemy.orm.sessionmaker(bind=engine, autocommit=True)
session = Session()
# database initialisation

def init_db():
    if len(Base.metadata.tables.keys()) == 0:
        return
    tname = Base.metadata.tables.keys()[0]
    if not engine.dialect.has_table(engine, tname):
        Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


class MyModel(QtCore.QAbstractTableModel):
    headers = {
        0: ("Title", "description"),
        1: ("Name", "name"),
        2: ("Year", "year"),
        3: ("Manufacturer", "manufacturer"),
        4: ("Status", "status"),
    }
    items_per_page = 50
    max_pages = 5

    def __init__(self):
        super(MyModel, self).__init__()
        self.cache = {}
        self.count = None
        self.searchString = ""
        self.order = "description"
        self.asc_or_desc = "asc"

        def reset():
            self.cache = {}
            self.count = None

        self.modelReset.connect(reset)

    def rowCount(self, *args):
        if self.count is None:
            self.count = self._buildQuery(session).count()
        return self.count

    def _buildQuery(self, session):
        return session.query(Game).order_by(getattr(getattr(Game, self.order), self.asc_or_desc)()).filter(
            sqlalchemy.or_(Game.description.like("%" + self.searchString + "%"),
                           Game.name.like("%" + self.searchString + "%")))

    def columnCount(self, *args):
        return len(MyModel.headers)

    def data(self, index, role):
        if role != QtCore.Qt.DisplayRole:
            return
        game = self._getRow(index.row())
        col = MyModel.headers[index.column()][1]
        return game.get("game_" + col, "")

    def _getRow(self, row):
        page = row / MyModel.items_per_page
        if not page in self.cache:
            if len(self.cache) >= MyModel.max_pages:
                del self.cache[self.cache.keys()[0]]
            result = session.execute(self._buildQuery(session) \
                                     .offset(page * MyModel.items_per_page).limit(MyModel.items_per_page))
            dicts = [dict(x) for x in result]
            self.cache[page] = dicts
        return self.cache[page][row % MyModel.items_per_page]

    def headerData(self, section, orientation, role):
        if role != QtCore.Qt.DisplayRole:
            return
        if orientation == QtCore.Qt.Horizontal:
            return MyModel.headers[section][0]

    def sort(self, column=None, direction=None):
        self.order = self.headers[column][1]
        if direction == QtCore.Qt.SortOrder.AscendingOrder:
            self.asc_or_desc = "asc"
        else:
            self.asc_or_desc = "desc"
        self.modelReset.emit()
        # print 'Model.sort: column: %s, direction: %s' % (column, direction)
