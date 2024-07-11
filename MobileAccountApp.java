import java.util.Scanner;

public class MobileAccountApp {

	public static void main(String... args) {

		Scanner input = new Scanner(System.in);	

		System.out.println(" Welcome to En-Hakkore Mobile Banking App. ");
		System.out.println(" How can we be of service to you? ");
		System.out.println();

		int deposit = 0;
		int withdraw = 0;
		int balance = 0;
		int account = 0;
		int flag = 1;
		int newBalance = 0;

			String menu = """
						 press 1, Deposit
						 press 2, Withdraw
						 press 3, BaLance
						 press 4, Exit
						""";

		while (flag == 1 ) {
			System.out.print(menu);

			System.out.println(" Kindly Press any available number or 4 to quit ");
			account = input.nextInt();
			switch (account) {
					case 1:
						System.out.println(" Deposit ");
						System.out.println(" How much would you like to deposit? ");
						deposit = input.nextInt();
							balance += deposit;
							System.out.println(" You Have Deposited " + balance);
							
							break;

					case 2:
						System.out.println(" Withdraw ");
						System.out.println(" How much would you like to withdraw? ");
						withdraw = input.nextInt();
						balance -= withdraw;
						if(withdraw == 0) System.out.print(" Insufficient Fund ");
						if(withdraw > balance)System.out.print(" Insufficient Fund, Kindly make Deposit to your Account.");
						if(withdraw <= 0) {
							 System.out.print(" Insufficient Fund ");
							System.out.println(" You Have Withdrawn " + withdraw);
						};
						break;

					case 3:
						System.out.println(" Balance ");
						newBalance += balance;
						System.out.println(" Your Available Balance is: " + newBalance);
						break;
	
					default:
						System.out.println(" Invalid input, Please try again later !!!!! ");
			}
				System.out.println();
				System.out.print("To continue, press 1 to continue or -1 to quit! ");
				flag = input.nextInt();
		}

	}

}