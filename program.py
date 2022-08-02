from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox


class otp_verifier(Tk):
    def __int__(self):
        super().__init__()
        self.geometry("600x550")
        self.resizable(False, False)
        self.n = random.randint(1000, 9999)
        account_sid = os.environ['ACc1c0efaa67d28d2ca50351bc9ba204cf']
        auth_token = os.environ['31eec4cfc3187b42ee3792eaff651413']
        self.client = Client(account_sid, auth_token)

        self.client.messages \
            .create(
            body=str(self.n),
            from_='+15017122661',
            to='+15558675310'
        )

    def labels(self):
        self.c = Canvas(self, bg="white", width=400, height=280)
        self.c.place(x=100, y=60)

        self.Login_Title = Label(self, text="OTP Verification", font="bold, 20", bg="white")
        self.Login_Title.place(x=210, y=90)

    def entry(self):
        self.User_name = Text(self, borderwidth=2, wrap="word", width=29, height=2)
        self.User_name.place(x=190, y=160)

    def buttons(self):
        self.submitButton = Button(self, text="Submit", width=10, command=self.checkOTP)
        self.submitButton.place(x=208, y=240)

        self.resendOTP = Button(self, text="Resend OTP", width=10, command=self.resendOTP)
        self.resendOTP.place(x=208, y=400)

    def checkOTP(self):
        try:
            self.userInput = int(self.User_name.get(1.0, "end-1c"))
            if self.userInput == self.n:
                messagebox.showinfo("showinfo", "Login Success")
                self.n = "done"

            elif self.n == "done":
                messagebox.showinfo("showinfo", "Already Logged in")

            else:
                messagebox.showinfo("showinfo", "Wrong OTP")

        except:
            messagebox.showinfo("showinfo", "INVALID OTP")

    def resendOTP(self):
        self.n = random.randint(1000, 9999)
        self.client = Client(account_sid, auth_token)

        self.client.messages \
            .create(
            body=str(self.n),
            from_='+15017122661',
            to='+15558675310'
        )


if __name__ == "__main__":
    window = otp_verifier()
    window.labels()
    window.entry()
    window.buttons()
    window.mainloop()
