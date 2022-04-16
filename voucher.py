import cloudscraper

scraper = cloudscraper.create_scraper()

def redeem(phone, voucher):
    code = voucher.replace("https://gift.truemoney.com/campaign/?v=", "")
    header = {
        "content-type": "application/json",
        "user-agent": "Mozilla/5.0"
    }
    payload = {
        "mobile": phone,
        "voucher_hash": code
    }
    res = scraper.post(f"https://gift.truemoney.com/campaign/vouchers/{code}/redeem",headers=header, json=payload)
    data = res.json()

    if data["status"]["message"] == "success":
        return data["data"]["my_ticket"]["amount_baht"]
    else:
        return data["status"]["message"]
