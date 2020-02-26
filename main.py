import helpers
import pandas as pd

result = []
for i in range(200):
    email = helpers.generate_email(host="gmail.com")
    name = helpers.generate_alphanumeric("l")
    phone = helpers.generate_alphanumeric("dDDDDDDDDD")

    row = {"email": email, "name": name.capitalize(), "phone": phone}
    result.append(row)



# df = pd.DataFrame(columns=list(result[0].keys()))

df = pd.DataFrame(result)

print(df)
df.to_csv("Customer.csv")