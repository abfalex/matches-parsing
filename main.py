import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def get_matches(driver, url, class_name):
    driver.get(url)
    matches_elements = driver.find_elements(By.CLASS_NAME, class_name)
    return [match.text.splitlines() for match in matches_elements]


def process_matches(matches):
    columns = [
        "Статус",
        "Команда 1",
        "Команда 2",
        "Счет матча",
        "Счет в первом тайме",
        "none1",
    ]
    result = pd.DataFrame(matches, columns=columns).drop(["none1"], axis=1)
    finished_matches = result.loc[result["Статус"] == "Завершен"]
    return finished_matches


def save_to_excel(data, filename):
    data.to_excel(filename, index=False)


def main():
    custom_options = Options()
    driver = webdriver.Chrome(options=custom_options)

    url = "https://www.flashscorekz.com/"
    class_name = "event__match.event__match--withRowLink.event__match--twoLine"

    matches = get_matches(driver, url, class_name)
    finished_matches = process_matches(matches)
    save_to_excel(finished_matches, "matches.xlsx")


if __name__ == "__main__":
    main()
