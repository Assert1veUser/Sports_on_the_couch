import asyncio

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer
import Model.Pars
from sqlalchemy.sql import text

sqlite_database = "sqlite:///DataBase/sotc.db"

engine = create_engine(sqlite_database, echo=True)

Session = sessionmaker(autoflush=False, bind=engine)

ty = []
td = []
tg = []
th = []

standingsName = []
standingsWA = []
standingsWV = []
standingsWH = []
standingsGA = []
standingsDA = []
standingsDH = []
standingsDV = []
standingsDeA = []
standingsDeH = []
standingsDeV = []

calendarName = []
calendarScore = []
calendarDate = []
calendarStadium = []
calendarWin_first = []
calendarDraw = []
calendarWin_second = []

teamsName = []
teamsCity = []
teamsYear_foundation = []
teamsStadium = []
teamsHead_coach = []
teamsSeasons_league = []
teamsGames_league = []
teamsWins = []
teamsDraws = []
teamsDefeats = []
teamsGoals_scored = []
teamsMissed_scored = []
teamsDry_matches = []

newsTitle = []
newsMain_text = []
newsDate = []


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

with Session(autoflush=False, bind=engine) as db:
    Model.Pars.pars_stand()
    for i in range(len(Model.Pars.teams)):
        ty.append(TeamDataBase())
    db.execute(text("DELETE FROM Standings"))
    for a in range(len(Model.Pars.teams)):
        ty[a].number = Model.Pars.teams[a].number
        ty[a].name = Model.Pars.teams[a].name
        ty[a].game_all = Model.Pars.teams[a].game_all
        ty[a].win_all = Model.Pars.teams[a].win_all
        ty[a].draw_all = Model.Pars.teams[a].draw_all
        ty[a].defeat_all = Model.Pars.teams[a].defeat_all
        ty[a].win_home = Model.Pars.teams[a].win_home
        ty[a].draw_home = Model.Pars.teams[a].draw_home
        ty[a].defeat_home = Model.Pars.teams[a].defeat_home
        ty[a].win_visit = Model.Pars.teams[a].win_visit
        ty[a].draw_visit = Model.Pars.teams[a].draw_visit
        ty[a].defeat_visit = Model.Pars.teams[a].defeat_visit
        db.add(ty[a])
        db.commit()

with Session(autoflush=False, bind=engine) as db1:
    Model.Pars.calendar_pars()
    for i in range(len(Model.Pars.calendar)):
        td.append(Calendar_DataBase())
    db1.execute(text("DELETE FROM Calendar"))
    for s in range(len(Model.Pars.calendar)):
        td[s].name = Model.Pars.calendar[s].name
        td[s].score = Model.Pars.calendar[s].score
        td[s].date = Model.Pars.calendar[s].date
        td[s].stadium = Model.Pars.calendar[s].stadium
        td[s].win_first = Model.Pars.calendar[s].win_first
        td[s].draw = Model.Pars.calendar[s].draw
        td[s].win_second = Model.Pars.calendar[s].win_second
        db1.add(td[s])
        db1.commit()
#
with Session(autoflush=False, bind=engine) as db2:
    Model.Pars.team_info_pars()
    for i in range(len(Model.Pars.team_info)):
        tg.append(Team_info_DataBase())
    db2.execute(text("DELETE FROM Team_info"))
    for k in range(len(Model.Pars.team_info)):
        tg[k].name = Model.Pars.team_info[k].name
        tg[k].city = Model.Pars.team_info[k].city
        tg[k].year_foundation = Model.Pars.team_info[k].year_foundation
        tg[k].stadium = Model.Pars.team_info[k].stadium
        tg[k].head_coach = Model.Pars.team_info[k].head_coach
        tg[k].seasons_league = Model.Pars.team_info[k].seasons_league
        tg[k].games_league = Model.Pars.team_info[k].games_league
        tg[k].wins = Model.Pars.team_info[k].wins
        tg[k].draws = Model.Pars.team_info[k].draws
        tg[k].defeats = Model.Pars.team_info[k].defeats
        tg[k].goals_scored = Model.Pars.team_info[k].goals_scored
        tg[k].missed_scored = Model.Pars.team_info[k].missed_scored
        tg[k].dry_matches = Model.Pars.team_info[k].dry_matches
        db2.add(tg[k])
        db2.commit()



with Session(autoflush=False, bind=engine) as db3:
    Model.Pars.news_pars()
    for i in range(len(Model.Pars.news)):
        th.append(News_DataBase())
    db3.execute(text("DELETE FROM News"))
    for a in range(len(Model.Pars.news)):
        th[a].title = Model.Pars.news[a].title
        th[a].main_text = Model.Pars.news[a].main_text
        th[a].date = Model.Pars.news[a].date
        db3.add(th[a])
        db3.commit()


def Select_calendar():
    select_calendarName = ()
    select_calendarScore = ()
    select_calendarDate = ()
    select_calendarStadium = ()
    select_calendarWin_first = ()
    select_calendarDraw = ()
    select_calendarWin_second = ()

    select_calendarName = Session(autoflush=False, bind=engine).query(Calendar_DataBase.name).all()
    select_calendarScore = Session(autoflush=False, bind=engine).query(Calendar_DataBase.score).all()
    select_calendarDate = Session(autoflush=False, bind=engine).query(Calendar_DataBase.date).all()
    select_calendarStadium = Session(autoflush=False, bind=engine).query(Calendar_DataBase.stadium).all()
    select_calendarWin_first = Session(autoflush=False, bind=engine).query(Calendar_DataBase.win_first).all()
    select_calendarDraw = Session(autoflush=False, bind=engine).query(Calendar_DataBase.draw).all()
    select_calendarWin_second = Session(autoflush=False, bind=engine).query(Calendar_DataBase.win_second).all()

    calendarName.clear()
    calendarScore.clear()
    calendarDate.clear()
    calendarStadium.clear()
    calendarWin_first.clear()
    calendarDraw.clear()
    calendarWin_second.clear()

    for i in range(0, 8):
        calendarName.append(select_calendarName[i][0])
        calendarScore.append(str(select_calendarScore[i][0]))
        calendarDate.append(str(select_calendarDate[i][0]))
        calendarStadium.append(str(select_calendarStadium[i][0]))
        calendarWin_first.append(str(select_calendarWin_first[i][0]))
        calendarDraw.append(str(select_calendarDraw[i][0]))
        calendarWin_second.append(str(select_calendarWin_second[i][0]))


def Select_standings():
    select_standingsName = ()
    select_standingsWA = ()
    select_standingsWV = ()
    select_standingsWH = ()
    select_standingsGA = ()
    select_standingsDA = ()
    select_standingsDH = ()
    select_standingsDV = ()
    select_standingsDeA = ()
    select_standingsDeH = ()
    select_standingsDeV = ()

    select_standingsName = Session(autoflush=False, bind=engine).query(TeamDataBase.name).all()
    select_standingsWA = Session(autoflush=False, bind=engine).query(TeamDataBase.win_all).all()
    select_standingsWV = Session(autoflush=False, bind=engine).query(TeamDataBase.win_visit).all()
    select_standingsWH = Session(autoflush=False, bind=engine).query(TeamDataBase.win_home).all()
    select_standingsGA = Session(autoflush=False, bind=engine).query(TeamDataBase.game_all).all()
    select_standingsDA = Session(autoflush=False, bind=engine).query(TeamDataBase.draw_all).all()
    select_standingsDH = Session(autoflush=False, bind=engine).query(TeamDataBase.draw_home).all()
    select_standingsDV = Session(autoflush=False, bind=engine).query(TeamDataBase.draw_visit).all()
    select_standingsDeA = Session(autoflush=False, bind=engine).query(TeamDataBase.defeat_all).all()
    select_standingsDeH = Session(autoflush=False, bind=engine).query(TeamDataBase.defeat_home).all()
    select_standingsDeV = Session(autoflush=False, bind=engine).query(TeamDataBase.defeat_visit).all()

    standingsName.clear()
    standingsWA.clear()
    standingsWV.clear()
    standingsWH.clear()
    standingsGA.clear()
    standingsDA.clear()
    standingsDH.clear()
    standingsDV.clear()
    standingsDeA.clear()
    standingsDeH.clear()
    standingsDeV.clear()

    for i in range(0, 16):
        standingsName.append(select_standingsName[i][0])
        standingsWA.append(str(select_standingsWA[i][0]))
        standingsWV.append(str(select_standingsWV[i][0]))
        standingsWH.append(str(select_standingsWH[i][0]))
        standingsGA.append(str(select_standingsGA[i][0]))
        standingsDA.append(str(select_standingsDA[i][0]))
        standingsDH.append(str(select_standingsDH[i][0]))
        standingsDV.append(str(select_standingsDV[i][0]))
        standingsDeA.append(str(select_standingsDeA[i][0]))
        standingsDeH.append(str(select_standingsDeH[i][0]))
        standingsDeV.append(str(select_standingsDeV[i][0]))


def Select_teams():
    select_teamsName = ()
    select_teamsCity = ()
    select_teamsYear_foundation = ()
    select_teamsStadium = ()
    select_teamsHead_coach = ()
    select_teamsSeasons_league = ()
    select_teamsGames_league = ()
    select_teamsWins = ()
    select_teamsDraws = ()
    select_teamsDefeats = ()
    select_teamsGoals_scored = ()
    select_teamsMissed_scored = ()
    select_teamsDry_matches = ()

    select_teamsName = Session(autoflush=False, bind=engine).query(Team_info_DataBase.name).all()
    select_teamsCity = Session(autoflush=False, bind=engine).query(Team_info_DataBase.city).all()
    select_teamsYear_foundation = Session(autoflush=False, bind=engine).query(Team_info_DataBase.year_foundation).all()
    select_teamsStadium = Session(autoflush=False, bind=engine).query(Team_info_DataBase.stadium).all()
    select_teamsHead_coach = Session(autoflush=False, bind=engine).query(Team_info_DataBase.head_coach).all()
    select_teamsSeasons_league = Session(autoflush=False, bind=engine).query(Team_info_DataBase.seasons_league).all()
    select_teamsGames_league = Session(autoflush=False, bind=engine).query(Team_info_DataBase.games_league).all()
    select_teamsWins = Session(autoflush=False, bind=engine).query(Team_info_DataBase.wins).all()
    select_teamsDraws = Session(autoflush=False, bind=engine).query(Team_info_DataBase.draws).all()
    select_teamsDefeats = Session(autoflush=False, bind=engine).query(Team_info_DataBase.defeats).all()
    select_teamsGoals_scored = Session(autoflush=False, bind=engine).query(Team_info_DataBase.goals_scored).all()
    select_teamsMissed_scored = Session(autoflush=False, bind=engine).query(Team_info_DataBase.missed_scored).all()
    select_teamsDry_matches = Session(autoflush=False, bind=engine).query(Team_info_DataBase.dry_matches).all()

    teamsName.clear()
    teamsCity.clear()
    teamsYear_foundation.clear()
    teamsStadium.clear()
    teamsHead_coach.clear()
    teamsSeasons_league.clear()
    teamsGames_league.clear()
    teamsWins.clear()
    teamsDraws.clear()
    teamsDefeats.clear()
    teamsGoals_scored.clear()
    teamsMissed_scored.clear()
    teamsDry_matches.clear()

    for i in range(0, 16):
        teamsName.append(select_teamsName[i][0])
        teamsCity.append(str(select_teamsCity[i][0]))
        teamsYear_foundation.append(str(select_teamsYear_foundation[i][0]))
        teamsStadium.append(str(select_teamsStadium[i][0]))
        teamsHead_coach.append(str(select_teamsHead_coach[i][0]))
        teamsSeasons_league.append(str(select_teamsSeasons_league[i][0]))
        teamsGames_league.append(str(select_teamsGames_league[i][0]))
        teamsWins.append(str(select_teamsWins[i][0]))
        teamsDraws.append(str(select_teamsDraws[i][0]))
        teamsDefeats.append(str(select_teamsDefeats[i][0]))
        teamsGoals_scored.append(str(select_teamsGoals_scored[i][0]))
        teamsMissed_scored.append(str(select_teamsMissed_scored[i][0]))
        teamsDry_matches.append(str(select_teamsDry_matches[i][0]))

def Select_news():
    select_newsInfo = ()
    select_newsMain_text = ()
    select_newsDate = ()

    select_newsInfo = Session(autoflush=False, bind=engine).query(News_DataBase.title).all()
    select_newsMain_text = Session(autoflush=False, bind=engine).query(News_DataBase.main_text).all()
    select_newsDate = Session(autoflush=False, bind=engine).query(News_DataBase.date).all()

    newsTitle.clear()
    newsMain_text.clear()
    newsDate.clear()

    for i in range(0, 20):
        newsTitle.append(select_newsInfo[i][0])
        newsMain_text.append(str(select_newsMain_text[i][0]))
        newsDate.append(select_newsDate[i][0])
