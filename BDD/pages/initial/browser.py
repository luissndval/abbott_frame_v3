import time

import pyautogui

from BDD.data.country_brand import country
from BDD.data.credentials import user_password
from _pom.front.front import functions


class browser(functions):

    def start_browser(self, country_code, brand):
        try:
            functions.driver_Chrome(self)
            time.sleep(3)
            # Obtener la información de países y marcas desde el módulo country
            countries_data = country

            # Bucle para recorrer la información de países y marcas
            for country_key, brands_urls in countries_data.items():
                if country_code.lower() == country_key.lower():
                    # Verificar si la marca está presente en el país
                    if brand in brands_urls:
                        url = brands_urls[brand]
                        functions.browser(self,url)
                        break  # Salir del bucle si la marca es encontrada

            pyautogui.write(user_password["user"])
            pyautogui.press("tab")
            pyautogui.write(user_password["password"])
            pyautogui.press("tab")
            pyautogui.press("enter")
            functions.max(self)
            time.sleep(3)
            self.driver.refresh()

        except Exception as e:
            print("Error:", e)
            raise
