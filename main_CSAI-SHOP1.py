class CSALShop:
    def __init__(self):
        self.prices = {'notebook': 34000, 'tablet': 19000, 'mobile': 26000}
        self.notebook_qty = 0
        self.tablet_qty = 0
        self.mobile_qty = 0
        self.is_member = False
        self.total_price = 0
        self.payment = 0
        self.receipt = 0

    def get_user_input(self):
        while True:
            member_input = input("คุณเป็นสมาชิกหรือไม่ (Y/N): ").strip().lower()
            if member_input == "Y" or member_input == "y":
                self.is_member = True
                break
            elif member_input == "N" or member_input == "n":
                self.is_member = False
                break
            else:
                print("ข้อมูลไม่ถูกต้อง กรุณาป้อน 'Y' หรือ 'N'.")

        self.notebook_qty = self.get_positive_integer("รับ Notebook กี่เครื่อง: ")
        self.tablet_qty = self.get_positive_integer("รับ Tablet กี่เครื่อง: ")
        self.mobile_qty = self.get_positive_integer("รับ Mobile กี่เครื่อง: ")

    def get_positive_integer(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value >= 0:
                    return value
                else:
                    print("กรุณาป้อนจำนวนเต็มบวก.")
            except ValueError:
                print("ข้อมูลไม่ถูกต้อง กรุณาป้อนตัวเลข.")

    def calculate_price(self):
        self.total_price = (
            self.notebook_qty * self.prices['notebook'] +
            self.tablet_qty * self.prices['tablet'] +
            self.mobile_qty * self.prices['mobile']
        )

        if self.is_member:
            self.total_price *= 0.95  # ส่วนลดสำหรับสมาชิก 5%

        if self.total_price >= 50000:
            self.total_price *= 0.90  # ส่วนลดเพิ่มสำหรับยอดรวมมากกว่าหรือเท่ากับ 50,000 บาท

    # def process_payment(self):
    #     while True:
    #         try:
    #             self.payment = float(input("กรุณากรอกจำนวนเงินที่จะชำระ: "))
    #             if self.payment >= self.total_price:
    #               break
    #             else:
    #                 shortfall = self.total_price - self.payment
    #                 print(f"จำนวนเงินไม่เพียงพอ ขาดอีก {shortfall:.2f} บาท")
    #                 add_money = float(input("กรุณาใส่จำนวนเงินที่ขาด :"))
    #                 while add_money < shortfall:

    #                     add_money += float(input("กรุณาเพิ่มเงินเจ้าค่ะ: "))
    #                     # if add_money + self.payment >= self.total_price:
    #                     #   print("การชำระเงินเสร็จสิ้น")
    #                     #   break
    #                     # else:
    #                     #   print("error")
    #         except ValueError:
    #             print("ข้อมูลไม่ถูกต้อง กรุณาป้อนตัวเลข.")


    def process_payment(self):
        while True:
          try:
            
            self.payment = float(input("กรุณาระบุจำนวนเงินที่ต้องการชำระ: "))
            if self.payment < self.total_price:
                Lack_of_money = self.total_price - self.payment
                print(f"ขาดเงินอีก {Lack_of_money:.2f} บาท นะเจ้าคะ")
                Lack_money = float(input("กรุณาเพิ่มจำนวนเงินเจ้าค่ะ : "))
                while True:
                    if Lack_money >= Lack_of_money:
                        print("การชำระเงินเสร็จสิ้น ขอบพระคุณเจ้าค่ะ")
                        break
                    else:
                        print("กรุณาเพิ่มจำนวนเงินเจ้าค่ะ")
                        break
            else:
                print("การชำระเงินเสร็จสิ้น ขอบพระคุณเจ้าค่ะ")
                break

          except ValueError:
                print("[error]".upper())


    def print_receipt(self):
        print("************************** ใบเสร็จ *************************************\n")
        if self.notebook_qty > 0:
            print(f"Notebook {self.notebook_qty} เครื่อง ราคา {self.notebook_qty * self.prices['notebook']:.2f} บาท")
        if self.tablet_qty > 0:
            print(f"Tablet {self.tablet_qty} เครื่อง ราคา {self.tablet_qty * self.prices['tablet']:.2f} บาท")
        if self.mobile_qty > 0:
            print(f"Mobile {self.mobile_qty} เครื่อง ราคา {self.mobile_qty * self.prices['mobile']:.2f} บาท")
        print(f"ราคารวมหลังหักส่วนลด: {self.total_price:.2f} บาท")
        print(f"จำนวนเงินที่ชำระ: {self.payment:.2f} บาท")
        print(f"เงินทอน: {(self.payment - self.total_price):.2f} บาท")
        print("***************************************************************************\n")

    def run(self):
        self.get_user_input()
        self.calculate_price()
        print(f"ยอดรวมที่ต้องชำระ: {self.total_price:.2f} บาท")
        self.process_payment()
        self.print_receipt()

CSALShop().run()