'''Objective: Create a simple bank account that allows one to deposit and withdraw
money, as well as check one's balance, take loans, and even donate to the orphanage. '''


##front-end:

if __name__ == '__main__':
    #declaring variables
    total = 0;
    withdraw = 0;
    donate = 0;
    deposit = 0;
    interest = 0;
    loan_total = 0;
    deposit_total = 0;
    withdraw_total = 0;
    donate_total = 0;
    n_day = 0;
    n_month = 0;
    n_year = 0;
    need_donate = 0;
    need_withdraw = 0;

    name = input("You're welcome to the Python Bank!\nWhat is your name dear sir/madam?\nName: ")
    date = list(input("What is today's date? (format: DD/MM/YYYY)\nEnter here: ")); #date needed for loan

    while True:
        print("\n","-"*60)
        option = input(f"Dear {name}, what would you like to do today? (Enter corresponding number)\n1>> Deposit sika\n2>> Withdraw sika\n3>> Take loan\n4>> Donate to orphanage fund\n5>> Check balance\n6>> Complete course of action\n     Enter number: ");


    ##back-end:
         #date calculations (for loans)
        day = int(''.join(date[:2]));
        month = int(''.join(date[3:5]));
        year = int(''.join(date[6:]));

        #Money deposition function
        def fx_deposit():
            print('\n');
            print("-"*60);
            
            global total; ##Why am I doing this? Well how dare the function try modifying what is in the global variable (total=0) The only way I can modify the value stored in a global variable from in a function, is using global statement on that variable
            global deposit_total;
            deposit = int(input("How much would you like to deposit\nI am depositing GHC: "));
            total += deposit
            deposit_total += deposit;
            print(f"Congratulations {name}, you have successfuly deposited GHC {deposit}.00")

        
        #Money withdrawal function 
        def fx_withdraw():
            print('\n');
            print("-"*60);
            
            global total;
            global withdraw;
            global withdraw_total;
            global need_withdraw;
            withdraw = int(input("How much would you like to withdraw\nI am withdrawing GHC: "));
            
            if withdraw < total: 
                total -= withdraw;
                withdraw_total += withdraw;
                print(f"Congratulations {name}, You have successfully withdrawn GHC {withdraw}.00");
            else: #accounting for insufficient funds to withdraw
                need_withdraw = withdraw - total;
                print(f"{name}, Your ambition is bigger than your wallet.\nYou have insufficient funds to withdraw.\nYou might consider depositing some money (at least GHC {need_withdraw}.00) into your account.")
                
            
        #Money Donation function   
        def fx_donate():
            print('\n');
            print("-"*60);
            
            global total;
            global donate;
            global need_donate;
            global donate_total;
            donate = int(input("How much would you like to donate\nI am donating GHC: "));
            
            if donate < total: 
                total -= donate;
                donate_total += donate;
                print(f"Congratulations {name}, You have successfully donated GHC {donate}.00. You kind soul!")
            else:  #accounting for insufficient funds to donate
                need_donate = donate - total;
                print(f"{name}, Your heart is bigger than your wallet.\nYou have insufficient funds to donate.\nYou might consider depositing some money (GHC {need_donate}.00) into your account.")
                donate -= donate
                
        #Loan function
        #1. Gives options of loans to take or allows one to input his own loan 2. Calculates 10% interest on chosen loan(15% if it's personal loan) 3. Calculates date due for loan payment(1month from date given)
        def fx_loan():
            print('\n');
            print("-"*60);
            global total;
            global day;
            global month;
            global year;
            global interest;
            global loan_total;
            global n_day;
            global n_month;
            global n_year;
            
            #Options of loan (including personal-option)
            loan_option1 = 3000;
            loan_option2 = 5000;
            loan_option3 = 10000;

            if total < 100:
                print(f"My broke friend, you have an account balance of GHC {total}.00. Make deposits of at least GHC 100.00. The Python bank can't trust your ability to pay back your loan.");
                
            else:
                loan_option = input(f"Which loan offer would you like to take?:\n1. GHC {loan_option1}.00\n2. GHC {loan_option2}.00\n3. GHC {loan_option3}.00\n4. Persoanal loan\nEnter here: ");
                if loan_option == '1':
                    total += loan_option1;
                    interest = loan_option1 + 0.1*loan_option1;
                    loan_total += loan_option1;    #keeps a variable that records sum total of all loans taken (for balance)
                    print(f"Congratulations {name}, you have acquired a loan of GHC {loan_option1}.00.");
                elif loan_option == '2':
                    total += loan_option2;
                    interest = loan_option2 + 0.1*loan_option2;
                    loan_total += loan_option2;
                    print(f"Congratulations {name}, you have acquired a loan of GHC {loan_option2}.00.");   
                elif loan_option == '3':
                    total += loan_option3;
                    interest = loan_option3 + 0.1*loan_option3;
                    loan_total += loan_option3;
                    print(f"Congratulations {name}, you have acquired a loan of GHC {loan_option3}.00.");
                elif loan_option == '4': #for personal loans 
                    loan_option4 = int(input("How much of a loan would you like to withdraw?\nI would like to withdraw: GHC "));
                    total += loan_option4;
                    interest = loan_option4 + 0.15*loan_option4;
                    loan_total += loan_option4
                    print(f"Congratulations {name}, you have acquired a personal loan of GHC {loan_option4}.00.");
                          
                #calculating date of loan payment (30 days for first 3 loans, and 50 days for personal loan.
                days_loan_option123 = 30;
                days_loan_option4 = 50;
                if loan_option == '1' or loan_option == '2' or loan_option == '3':
                    n_day = day + days_loan_option123;
                    if n_day > 30:
                        n_day -= 30;
                        n_month = month + 1;
                        if n_month > 12:
                            n_month -= 12;
                            n_year = year + 1;
                        else:
                            n_year = year;
                else:
                    n_day = day + days_loan_option4;
                    d = n_day // 30;
                    n_month = month + d;
                    n_day -= d*30; #or n_day = n_day % 30
                    if n_month > 12:
                        n_month -= 12;
                        n_year = year + 1;
                    else:
                        n_year = year;

                print(f"\nAdditional loan info: You will pay an interest of GHC {interest} on your loan latest by {n_day}/{n_month}/{n_year}");
            

            
        #Balance function
        def fx_balance():
            print('\n');
            print("-"*60)
            global total;
            global deposit_total;
            global interest;
            global loan_total;
            global donate;
            print(f"Considering:\nTotal Deposits: GHC {deposit_total}.00\nTotal withdrawals: GHC {withdraw}.00\nTotal loan withdrawals: GHC {loan_total}.00\nTotal Donations: GHC {donate}.00\nYou have an account balance of: GHC {total}.00.") 

        #Complete
        if option == '6':
            print('\n');
            print("-"*60)
            print(f"Was great working with you {name}. Feel free to use the Python bank another time :)");
            break;
            

    #main program:
        #switch statement dict: (courtesy of Mike)
        main_switch = {
            '1': fx_deposit,
            '2': fx_withdraw,
            '3': fx_loan,
            '4': fx_donate,
            '5': fx_balance,
            }
        main_switch[option](); #for default function inclusion: main_switch.get(conditon, default_func);





        
