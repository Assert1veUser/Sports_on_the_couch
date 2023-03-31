import asyncio
import aiohttp
from bs4 import BeautifulSoup as BS
from fake_user_agent import user_agent
from DTO.Standings import Team, Calendar, Team_info, News

BASE_URL_tournament_table = "https://premierliga.ru/tournament-table/"
BASE_URL_calendar = "https://premierliga.ru/calendar/"
BASE_URL_premierliga = "https://premierliga.ru/"
BASE_URL_news = "https://premierliga.ru/news/rfpl/"
HEADERS = {"User-Agent": user_agent.__name__}
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


async def team_pars():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL_tournament_table, headers=HEADERS) as response:
            r = await aiohttp.StreamReader.read(response.content)
            soup = BS(r, "html.parser")
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


async def calendar_pars():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL_calendar, headers=HEADERS) as response:
            rr = await aiohttp.StreamReader.read(response.content)
            soup_calendar = BS(rr, "html.parser")
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
    for l in range(len(win_first_all_calendar)):
        calendar.append(Calendar(
            names_calendar[l],
            scores_calendar[l],
            dates_calendar[l],
            stadiums_calendar[l],
            win_first_all_calendar[l],
            draws_calendar[l],
            win_second_all_calendar[l]))


async def team_info_pars():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL_premierliga, headers=HEADERS) as response:
            rr = await aiohttp.StreamReader.read(response.content)
            soup_team_info = BS(rr, "html.parser")
            items_team_info = soup_team_info.find_all("div", {"class": "rpl-clubs"})
            for item in items_team_info:
                for link in item.findAll('a'):
                    links.append(link.get('href'))
        for w in range(len(links)):
            async with session.get("https://premierliga.ru" + links[w], headers=HEADERS) as response:
                rr = await aiohttp.StreamReader.read(response.content)
                soup_team_info_2 = BS(rr, "html.parser")
                items_team_info_2 = soup_team_info_2.find_all("div", {"class": "main-info"})
                for item in items_team_info_2:
                    main_team_info = item.find_all("b")
                    name_info.append(main_team_info[0].text)
                    parts = main_team_info[1].text.rsplit(',', 2)
                    city_info.append(parts[0])
                    year_foundation_info.append(parts[1].strip())
                    stadium_info.append(main_team_info[2].text)
                    head_coach_info.append(main_team_info[3].text)
                items_team_info_3 = soup_team_info_2.find_all("td", {"class": "count"})
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


async def news_pars():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL_news, headers=HEADERS) as response:
            rr = await aiohttp.StreamReader.read(response.content)
            soup_news = BS(rr, "html.parser")
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
            for l in range(len(main_text_all)):
                main_text.append(main_text_all[l].text)
            for j in range(1, len(main_text)):
                if j % 2 != 0:
                    main_text_clear.append(main_text[j])
            for l in range(len(date)):
                news.append(News(
                    title[l],
                    main_text_clear[l],
                    date[l]
                ))
