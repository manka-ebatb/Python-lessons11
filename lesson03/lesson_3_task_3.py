from address import Address
from mailing import Mailing

ad_1 = Address("301012", "г.Новомосковск", "ул. Квартирная", "д.45", "кв.10")
ad_2 = Address("461524", "г.Орск", "ул. Зелёная", "д.63", "кв.117")


mail = Mailing(ad_1, ad_2, 587, "46952T356BHC243")
mail.info()
