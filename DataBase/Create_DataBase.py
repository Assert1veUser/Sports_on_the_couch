import asyncio

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer
import Model.Parsing
from sqlalchemy.sql import text

sqlite_database = "sqlite:///sotc.db"

engine = create_engine(sqlite_database, echo=True)

Session = sessionmaker(autoflush=False, bind=engine)

ty = []
td = []
tg = []
th = []


class Base(DeclarativeBase):
    pass


class TeamDataBase(Base):
    __tablename__ = "Standings"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer)
    name = Column(Integer)
    game_all = Column(Integer)
    win_all = Column(Integer)
    draw_all = Column(Integer)
    defeat_all = Column(Integer)
    win_home = Column(Integer)
    draw_home = Column(Integer)
    defeat_home = Column(Integer)
    win_visit = Column(Integer)
    draw_visit = Column(Integer)
    defeat_visit = Column(Integer)


class Calendar_DataBase(Base):
    __tablename__ = "Calendar"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Integer)
    score = Column(Integer)
    date = Column(Integer)
    stadium = Column(Integer)
    win_first = Column(Integer)
    draw = Column(Integer)
    win_second = Column(Integer)


class Team_info_DataBase(Base):
    __tablename__ = "Team_info"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Integer)
    city = Column(Integer)
    year_foundation = Column(Integer)
    stadium = Column(Integer)
    head_coach = Column(Integer)
    seasons_league = Column(Integer)
    games_league = Column(Integer)
    wins = Column(Integer)
    draws = Column(Integer)
    defeats = Column(Integer)
    goals_scored = Column(Integer)
    missed_scored = Column(Integer)
    dry_matches = Column(Integer)


class News_DataBase(Base):
    __tablename__ = "News"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Integer)
    main_text = Column(Integer)
    date = Column(Integer)


Base.metadata.create_all(bind=engine)


def stanf():
    with Session(autoflush=False, bind=engine) as db:

        if __name__ == '__main__':
            loop = asyncio.get_event_loop()
            loop.run_until_complete(Model.Parsing.team_pars())
        for i in range(len(Model.Parsing.teams)):
            ty.append(TeamDataBase())
        db.execute(text("DELETE FROM Standings"))
        for a in range(len(Model.Parsing.teams)):
            ty[a].number = Model.Parsing.teams[a].number
            ty[a].name = Model.Parsing.teams[a].name
            ty[a].game_all = Model.Parsing.teams[a].game_all
            ty[a].win_all = Model.Parsing.teams[a].win_all
            ty[a].draw_all = Model.Parsing.teams[a].draw_all
            ty[a].defeat_all = Model.Parsing.teams[a].defeat_all
            ty[a].win_home = Model.Parsing.teams[a].win_home
            ty[a].draw_home = Model.Parsing.teams[a].draw_home
            ty[a].defeat_home = Model.Parsing.teams[a].defeat_home
            ty[a].win_visit = Model.Parsing.teams[a].win_visit
            ty[a].draw_visit = Model.Parsing.teams[a].draw_visit
            ty[a].defeat_visit = Model.Parsing.teams[a].defeat_visit
            db.add(ty[a])
            db.commit()


with Session(autoflush=False, bind=engine) as db1:
    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(Model.Parsing.calendar_pars())
    for i in range(len(Model.Parsing.calendar)):
        td.append(Calendar_DataBase())
    db1.execute(text("DELETE FROM Calendar"))
    for s in range(len(Model.Parsing.calendar)):
        td[s].name = Model.Parsing.calendar[s].name
        td[s].score = Model.Parsing.calendar[s].score
        td[s].date = Model.Parsing.calendar[s].date
        td[s].stadium = Model.Parsing.calendar[s].stadium
        td[s].win_first = Model.Parsing.calendar[s].win_first
        td[s].draw = Model.Parsing.calendar[s].draw
        td[s].win_second = Model.Parsing.calendar[s].win_second
        db1.add(td[s])
        db1.commit()

with Session(autoflush=False, bind=engine) as db2:
    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(Model.Parsing.team_info_pars())
    for i in range(len(Model.Parsing.team_info)):
        tg.append(Team_info_DataBase())
    db2.execute(text("DELETE FROM Team_info"))
    for k in range(len(Model.Parsing.team_info)):
        tg[k].name = Model.Parsing.team_info[k].name
        tg[k].city = Model.Parsing.team_info[k].city
        tg[k].year_foundation = Model.Parsing.team_info[k].year_foundation
        tg[k].stadium = Model.Parsing.team_info[k].stadium
        tg[k].head_coach = Model.Parsing.team_info[k].head_coach
        tg[k].seasons_league = Model.Parsing.team_info[k].seasons_league
        tg[k].games_league = Model.Parsing.team_info[k].games_league
        tg[k].wins = Model.Parsing.team_info[k].wins
        tg[k].draws = Model.Parsing.team_info[k].draws
        tg[k].defeats = Model.Parsing.team_info[k].defeats
        tg[k].goals_scored = Model.Parsing.team_info[k].goals_scored
        tg[k].missed_scored = Model.Parsing.team_info[k].missed_scored
        tg[k].dry_matches = Model.Parsing.team_info[k].dry_matches
        db2.add(tg[k])
        db2.commit()

with Session(autoflush=False, bind=engine) as db3:
    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(Model.Parsing.news_pars())
    for i in range(len(Model.Parsing.news)):
        th.append(News_DataBase())
    db3.execute(text("DELETE FROM News"))
    for a in range(len(Model.Parsing.news)):
        th[a].title = Model.Parsing.news[a].title
        th[a].main_text = Model.Parsing.news[a].main_text
        th[a].date = Model.Parsing.news[a].date
        db3.add(th[a])
        db3.commit()
