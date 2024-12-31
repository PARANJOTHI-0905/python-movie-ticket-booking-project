class MovieTicketBooking:
    
    def init(self):
        print("WELCOME TO ONLINE MOVIES TICKET BOOKING")

    def booktickets(self):
        while True:
            movie = input("1.Enter your movie name: Bloody Beggar/ Brother/ Kanguva/ Lubber Pandhu/ Amaran/ Goat & Valimai / cancel ")
            if movie.lower() == "cancel":
                print("Booking process canceled")
                return

            if movie == "Bloody Beggar" or movie == "Brother" or movie == "Kanguva" or movie == "Lubber Pandhu" or movie=="Amaran" or movie=="Goat & Valimai":
                print("Book Tickets")
                while True:
                    theater = input("2.Enter a theatre: RAJA /RAM /SWAMI /KRISHNA /WOODLANDS /KASI/ EVP CINEMAS / cancel ")
                    if theater.lower() == "cancel":
                        print("Booking process canceled")
                        return

                    if theater == "RAJA" or theater == "RAM" or theater == "SWAMI" or theater == "KRISHNA" or theater == "WOODLANDS" or theater == "KASI" or theater == "EVP CINEMAS":
                        print("Welcome")
                        while True:
                            time = input("3.Enter your timing: 7:00AM / 11:30AM/ 3:00PM/ 6:30PM/ 10:15PM / cancel ")
                            if time.lower() == "cancel":
                                print("Booking process canceled")
                                return

                            if time == "7:00AM" or time == "11:30AM" or time == "3:00PM" or time == "6:30PM" or time == "10:15PM":
                                print("Available Tickets: 100")
                                print("Ticket price: 150")
                                price = 150
                                while True:
                                        ticket = int(input("4.Enter your no of tickets /cancel: "))
                                        if ticket <= 100:
                                            ticketprice = ticket * price
                                            print("Ticket price:", ticketprice)
                                            while True:
                                                payment = input("5.Enter your Payment Method: UPI/ Debit Card /cancel ")
                                                if payment.lower() == "cancel":
                                                    print("Booking process canceled")
                                                    return
                                                if payment == "UPI":
                                                    while True:
                                                        upi = input("6.Enter your UPI number (4 or 6 digits): ")
                                                        if len(upi) == 4 or len(upi) == 6:
                                                            print("Your tickets are booking successfully")
                                                            print(movie,"MOVIE",theater,"THEATER",time,"TIME",ticket,"Tickets are Booking Successfully")
                                                            print("THANK YOU ")
                                                            return
                                                        else:
                                                            print("Invalid UPI number. Please enter a valid 4 or 6-digit UPI.")
                                                            break

                                                elif payment == "Debit Card":
                                                    while True:
                                                        num = input("6.Enter your Card number:")
                                                        d = input("Enter Expiry date:")
                                                        c = int(input("Enter CVV (3 digits): "))
                                                        name = input("Enter Card Holder Name: ")
                                                        print(movie,"MOVIE",theater,"THEATER",time,"TIME",ticket,"Tickets are Booking Successfully")
                                                        print("THANK YOU ")

                                                        return

                                                else:
                                                    print("Enter correct Payment option")

                                        else:
                                            print("Tickets are unavailable")
                            else:
                                print("Timing not available")
                    else:
                        print("Please select available theater")
            else:
                print("Please select available movie")       
        


booking = MovieTicketBooking()
booking.booktickets()