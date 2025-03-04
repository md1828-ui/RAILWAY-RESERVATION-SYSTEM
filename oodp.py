#include <iostream>
using namespace std;

class TrainTicketBooking
{
private:
int seats;
string passengerName;
int passengerAge;
string passengerGender;
int numPassengers;
int passengerPNR; // Initialize with -1 to indicate no booking
string cardNumber;
string cardHolderName;
string expiryDate;
string cvv;
string username; // added username

string password; // added password

public:
TrainTicketBooking(int numSeats) {
seats = 10;
passengerName = "";
passengerAge = 0;
passengerGender = "";
numPassengers = 0;
passengerPNR = -1;
cardNumber = "";
cardHolderName = "";
expiryDate = "";
cvv = "";
rand(); // Seed the random number generator
username = "kushal"; // set the default username
password = "123"; // set the default password
}

// Function to check ticket availability
bool checkTicketAvailability() {
return (seats > 0);
}

// Function to book a ticket

void bookTicket() {
if (checkTicketAvailability()) {
cout << "Enter number of passengers: ";
cin >> numPassengers;
for (int i = 0; i < numPassengers; i++) {
cout << "Enter passenger name: ";
cin >> passengerName;
cout << "Enter passenger age: ";
cin >> passengerAge;
cout << "Enter passenger gender: ";
cin >> passengerGender;
passengerPNR = rand();
cout << "Ticket booked successfully for Passenger " << i + 1 << "!
PNR Number: " << passengerPNR << endl;
seats--;
}
}
else {
cout << "Sorry, no seats available." << endl;
}
}

// Function to cancel a ticket
void cancelTicket() {
if (passengerPNR != -1) {

cout << "Passenger Details: " << endl;
cout << "Name: " << passengerName << endl;
cout << "Age: " << passengerAge << endl;
cout << "Gender: " << passengerGender << endl;
cout << "PNR: " << passengerPNR << endl;
cout << "Ticket with PNR " << passengerPNR << " has been canceled."
<< endl;
passengerPNR = -1;
seats++;
}
else {
cout << "No ticket to cancel." << endl;
}
}

// Function to accept payment details
void acceptPaymentDetails() {
cout << "Enter card number: ";
cin >> cardNumber;
cout << "Enter card holder name: ";
cin >> cardHolderName;
cout << "Enter expiry date (MM/YY): ";
cin >> expiryDate;
cout << "Enter CVV: ";
cin >> cvv;

cout << "Payment details accepted." << endl;
}

// Function to generate PNR
void generatePNR()
{
if (passengerPNR != -1) {
cout << "Generated PNR: " << passengerPNR << endl;
}
else {
cout << "No PNR available." << endl;
}
}

// Function to perform login
bool login(string uname, string pword)
{
if (username == uname && password == pword)
{
cout << "Login successful.";
}
}
};
int main() {
int numSeats;

//cout << "Enter number of seats in the train: ";
//cin >> numSeats;

TrainTicketBooking bookingSystem(numSeats); // Create a
TrainTicketBooking object

string uname, pword;
cout << "Enter username: ";
cin >> uname;
cout << "Enter password: ";
cin >> pword;

if (bookingSystem.login(uname, pword)) { // Perform login
int choice;
do {
cout << "=============== TRAIN TICKET BOOKING SYSTEM
===============" << endl;
cout << "1. Check ticket availability" << endl;
cout << "2. Book a ticket" << endl;
cout << "3. Cancel a ticket" << endl;
cout << "4. Accept payment details" << endl;
cout << "5. Generate PNR" << endl;
cout << "6. Logout" << endl;
cout << "Enter your choice: ";
cin >> choice;

switch (choice) {
case 1:
if (bookingSystem.checkTicketAvailability()) {
cout << "Seats available: " <<
bookingSystem.checkTicketAvailability() << endl;
} else {
cout << "No seats available." << endl;
}
break;
case 2:
bookingSystem.bookTicket();
break;
case 3:
bookingSystem.cancelTicket();
break;
case 4:
bookingSystem.acceptPaymentDetails();
break;
case 5:
bookingSystem.generatePNR();
break;
case 6:
cout << "Logged out." << endl;
break;
default:

cout << "Invalid choice. Try again." << endl;
}
}
while (choice != 6);
}
else {
cout << "Login failed1" << endl;
}
}