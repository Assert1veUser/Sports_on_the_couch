import requests
from bs4 import BeautifulSoup

from DTO.Standings import Team, Calendar, Team_info, News

BASE_URL_tournament_table = "https://premierliga.ru/tournament-table/"
BASE_URL_calendar = "https://premierliga.ru/calendar/"
BASE_URL_premierliga = "https://premierliga.ru/"
BASE_URL_news = "https://premierliga.ru/news/rfpl/"

teams = []
calendar = []
links = []
team_info = []
news = []

names_calendar = []
scores_calendar = []
dates_calendar = []
stadiums_calendar = []
win_first_all_calendar = []
draws_calendar = []
win_second_all_calendar = []

name_info = []
city_info = []
year_foundation_info = []
stadium_info = []
head_coach_info = []
stat_info = []
result_stat_info = []

title = []
main_text = []
main_text_clear = []
date = []


def pars_stand():
    response = requests.get(BASE_URL_tournament_table)
    soup = BeautifulSoup(response.text, 'lxml')
    for a in range(1, 17):
        items = soup.find_all("tr", {"class": f"s{a}"})

        for item in items:
            number = item.find("td", {"class": "place"}).text.strip()
            name = item.find("td", {"class": "club"}).text.strip()
            general_statistics = item.findAll("td", {"class": "dark-blue num"})
            game_all = general_statistics[0].text.strip()
            win_all = general_statistics[1].text.strip()
            draw_all = general_statistics[2].text.strip()
            defeat_all = general_statistics[3].text.strip()
            other_statistics = item.findAll("td", {"class": "blue num"})
            win_home = other_statistics[0].text.strip()
            draw_home = other_statistics[1].text.strip()
            defeat_home = other_statistics[2].text.strip()
            win_visit = other_statistics[3].text.strip()
            draw_visit = other_statistics[4].text.strip()
            defeat_visit = other_statistics[5].text.strip()
            teams.append(Team(
                number,
                name,
                game_all,
                win_all,
                draw_all,
                defeat_all,
                win_home,
                draw_home,
                defeat_home,
                win_visit,
                draw_visit,
                defeat_visit))


def calendar_pars():
    response_calendar = requests.get(BASE_URL_calendar)
    soup_calendar = BeautifulSoup(response_calendar.text, 'lxml')
    items_calendar_1 = soup_calendar.find_all("tr", {"class": "matchtr"})
    for item in items_calendar_1:
        names_calendar.append(item.find("td", {"width": "40%"}).text.strip())
        scores_calendar.append(item.find("td", {"width": "10%"}).text)
        dates_calendar.append(item.find("td", {"width": "15%"}).text)
        stadiums_calendar.append(item.find("td", {"width": "35%"}).text)

    items_calendar_2 = soup_calendar.find_all("td", {"colspan": "4"})
    for item_2 in items_calendar_2:
        coef = item_2.findAll("div", {"class": "orange-koeff"})
        win_first_all_calendar.append(coef[0].text)
        draws_calendar.append(coef[1].text)
        win_second_all_calendar.append(coef[2].text)
    if len(win_first_all_calendar) != len(names_calendar):
        for a in range(0, len(names_calendar) - len(win_first_all_calendar)):
            win_first_all_calendar.insert(0, "-")
            draws_calendar.insert(0, "-")
            win_second_all_calendar.insert(0, "-")
    for s in range(len(win_first_all_calendar)):
        calendar.append(Calendar(
            names_calendar[s],
            scores_calendar[s],
            dates_calendar[s],
            stadiums_calendar[s],
            win_first_all_calendar[s],
            draws_calendar[s],
            win_second_all_calendar[s]))


def team_info_pars():
    response_teamInfo = requests.get(BASE_URL_premierliga)
    soup_teamInfo = BeautifulSoup(response_teamInfo.text, "lxml")
    items_team_info = soup_teamInfo.find_all("div", {"class": "rpl-clubs"})
    for item in items_team_info:
        for link in item.findAll("a"):
            links.append(link.get("href"))
    for w in range(len(links)):
        response_teamInfo_2 = requests.get("https://premierliga.ru" + links[w])
        soup_teamInfo_2 = BeautifulSoup(response_teamInfo_2.text, "lxml")
        items_team_info_2 = soup_teamInfo_2.find_all("div", {"class": "main-info"})
        for item in items_team_info_2:
            main_team_info = item.find_all("b")
            name_info.append(main_team_info[0].text)
            parts = main_team_info[1].text.rsplit(',', 2)
            city_info.append(parts[0])
            year_foundation_info.append(parts[1].strip())
            stadium_info.append(main_team_info[2].text)
            head_coach_info.append(main_team_info[len(main_team_info) - 1].text)
        items_team_info_3 = soup_teamInfo_2.find_all("td", {"class": "count"})
        for items in items_team_info_3:
            main_team_info_2 = items.find_all("p")
            stat_info.append(main_team_info_2[0].text)
    for i in range(0, len(stat_info), 8):
        result_stat_info.append(stat_info[i:i + 8])
    for f in range(len(name_info)):
        team_info.append(Team_info(
            name_info[f],
            city_info[f],
            year_foundation_info[f],
            stadium_info[f],
            head_coach_info[f],
            result_stat_info[f][0],
            result_stat_info[f][1],
            result_stat_info[f][2],
            result_stat_info[f][3],
            result_stat_info[f][4],
            result_stat_info[f][5],
            result_stat_info[f][6],
            result_stat_info[f][7],
        ))


def news_pars():
    response_news = requests.get(BASE_URL_news)
    soup_news = BeautifulSoup(response_news.text, "lxml")
    items_news = soup_news.find_all("div", {"class": "news-wrap"})
    for item in items_news:
        date.append(item.find("span", {"class": "date"}).text)
        title.append(item.find("span", {"class": "text"}).text.strip())
        main_text_all = item.find_all("span", {"class": "text"})
        main_text.append(main_text_all[0].text.strip())
        main_text.append(main_text_all[1].text.strip())
    items = soup_news.find_all("div", {"class": "news"})
    for items_q in items:
        date_all = items_q.find_all("p", {"class": "date"})
        for i in range(len(date_all)):
            date.append(date_all[i].text)
        title_all = items_q.find_all("a", {"class": "title"})
        for k in range(len(title_all)):
            title.append(title_all[k].text)
        main_text_all = item.find_all("p")
    for d in range(len(main_text_all)):
        main_text.append(main_text_all[d].text)
    for j in range(1, len(main_text)):
        if j % 2 != 0:
            main_text_clear.append(main_text[j])
    for k in range(len(date)):
        news.append(News(
            title[k],
            main_text_clear[k],
            date[k]
        ))
