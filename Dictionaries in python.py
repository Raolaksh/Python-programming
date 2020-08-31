
monthconversion = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}
print(monthconversion["Nov"])
print(monthconversion["Dec"])

print(monthconversion.update({"ting-tong": "Not a valid key"}))

print(monthconversion.get("ting-tong"))

