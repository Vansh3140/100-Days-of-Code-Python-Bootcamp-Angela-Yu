import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.in/Panasonic-Microwave-NN-ST26JMFDG-Silver-Menus/dp/B08CL8XF75/ref=sr_1_4?_encoding=UTF8&content-id=amzn1.sym.94cc05a3-43df-4c7f-8e72-95269ab45434&dib=eyJ2IjoiMSJ9.Gwe8yUk18H3gYwU_YUmJoSqHiEJzsgtHt7xcZjwdmw_mBe1dIQlkhWKs7mCKIACS9krx1FCgieEbKyFobjv1sSnYo838ZiNncVsVntPQkLO8dXXB63h6jxQoRX_phir6ifjAe_nL6gA9v7e3xY3NdMfpHrTK7lcIB-yHcLhRsRJjtO0TQWOf_8GAoNH6RQA6I-bBdLjq1IZMWha9N8OE04T5BGeqbi_Wnt1kBykufGu9Xqh85q2Brr_gvkJ8dppsiYgeNiTUA8Ju4pjxC7Zaom4WzZMiaZgHwLWEnZvGY-8.oIB-W40VmY108yXjC3CH1s1DtvBwaUIJ-zKEKliQ9VE&dib_tag=se&pd_rd_r=7ef72dba-edef-4004-b96a-4edcbabc4131&pd_rd_w=Wx3Lq&pd_rd_wg=vGWqQ&pf_rd_p=94cc05a3-43df-4c7f-8e72-95269ab45434&pf_rd_r=T8WEJ9NWBJDYZWNES4DC&qid=1716628260&refinements=p_85%3A10440599031&rps=1&s=kitchen&sr=1-4",

response = requests.get(
    url="https://www.amazon.in/Panasonic-Microwave-NN-ST26JMFDG-Silver-Menus/dp/B08CL8XF75/ref=sr_1_4?_encoding=UTF8"
        "&content-id=amzn1.sym.94cc05a3-43df-4c7f-8e72-95269ab45434&dib=eyJ2IjoiMSJ9"
        ".Gwe8yUk18H3gYwU_YUmJoSqHiEJzsgtHt7xcZjwdmw_mBe1dIQlkhWKs7mCKIACS9krx1FCgieEbKyFobjv1sSnYo838ZiNncVsVntPQkLO8dXXB63h6jxQoRX_phir6ifjAe_nL6gA9v7e3xY3NdMfpHrTK7lcIB-yHcLhRsRJjtO0TQWOf_8GAoNH6RQA6I-bBdLjq1IZMWha9N8OE04T5BGeqbi_Wnt1kBykufGu9Xqh85q2Brr_gvkJ8dppsiYgeNiTUA8Ju4pjxC7Zaom4WzZMiaZgHwLWEnZvGY-8.oIB-W40VmY108yXjC3CH1s1DtvBwaUIJ-zKEKliQ9VE&dib_tag=se&pd_rd_r=7ef72dba-edef-4004-b96a-4edcbabc4131&pd_rd_w=Wx3Lq&pd_rd_wg=vGWqQ&pf_rd_p=94cc05a3-43df-4c7f-8e72-95269ab45434&pf_rd_r=T8WEJ9NWBJDYZWNES4DC&qid=1716628260&refinements=p_85%3A10440599031&rps=1&s=kitchen&sr=1-4",
    headers={
        "User-Agent": "xyz",
        "Accept-Language": "en-US,en;q=0.9"
    })

soup = BeautifulSoup(response.text, "html.parser")

whole_price = int(soup.find(name="span", class_="a-price-whole").get_text().replace(",", "").replace(".", ""))

# Mailing Part

USERNAME = "ch@gmail.com"
PASSWORD = "abc"

if whole_price < 5500:
    connection = smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=USERNAME, password=PASSWORD)
    connection.sendmail(from_addr=USERNAME, to_addrs="workman3140@gmail.com", msg=f"Subject:Amazon Price has dropped!! \n\n Time to buy microwave as the price has dropped to {whole_price}. Click on {URL}")
    connection.close()
