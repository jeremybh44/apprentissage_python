from faker import Faker

fake = Faker(locale="fr_FR")

for _ in range(10):
    print(fake.job())
    print(fake.file_path(depth=5, category='video'))
    print(fake.credit_card_number(), fake.credit_card_expire(), fake.credit_card_security_code())
    print(fake.rgb_color(), fake.hex_color())
    print(fake.numerify(text="%%%-%-%%%%-%%%%-%%%-##"))
    print(fake.bothify(text="Product Number: ????-########"))




