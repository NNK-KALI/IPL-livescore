import requests
from bs4 import BeautifulSoup


def main():
    content = requests.get("https://www.cricbuzz.com/cricket-match/live-scores")
    soup = BeautifulSoup(content.text, "html.parser")

    main_box = soup.find(class_="cb-col cb-col-100 cb-plyr-tbody cb-rank-hdr cb-lv-main")
    heading = main_box.h2.text
    # print(heading)

    match_title_box = main_box.find(class_="cb-mtch-lst cb-col cb-col-100 cb-tms-itm")
    match_title = match_title_box.h3.text
    # print(match_title)

    score_box = main_box.find(class_="cb-scr-wll-chvrn cb-lv-scrs-col")
    # print(score_box.text)

    team_box_01 = score_box.find(class_="cb-hmscg-bat-txt")
    team_box_text_01 = team_box_01.text
    # print(team_box_text_01)
    team_name_01 = team_box_01.find(class_="cb-ovr-flo cb-hmscg-tm-nm").text
    # print(team_name_01)
    team_score_01 = team_box_text_01.split(team_name_01)
    team_score_01 = team_score_01[1]
    # print(team_score_01)
    team_01_result = "{0}      {1}".format(team_name_01, team_score_01)
    # print(team_01_result)

    team_box_02 = score_box.find(class_="cb-hmscg-bwl-txt")
    team_box_text_02 = team_box_02.text
    # print(team_box_text_02)
    team_name_02 = team_box_02.find(class_="cb-ovr-flo cb-hmscg-tm-nm").text
    # print(team_name_02)
    team_score_02 = team_box_text_02.split(team_name_02)
    try:
        team_score_02 = team_score_02[1]
    except IndexError:
        team_score_02 = "                   "
    team_02_result = "{0}      {1}".format(team_name_02, team_score_02)
    # print(team_02_result)

    try:
        match_status = score_box.find(class_="cb-text-complete").text
        # print(match_status)
    except:
        try:
            match_status= score_box.find(class_="cb-text-live").text
            # print(match_status)
        except Exception as ex:
            print("EX from match_status :" + str(ex))

    score_card = "{0}\n" \
                 "{1}\n" \
                 "{2}\n" \
                 "{3}\n" \
                 "{4}".format(heading, match_title,
                              team_01_result, team_02_result,
                              match_status)
    print("Scrapped Successfully")
    return score_card


if __name__ == "__main__":
    main()
