#include "mbed.h"

// Define I/O pins (Standard Mbed aliases; replace with specific pins like D2, PC_13 if needed)
InterruptIn button(p14);
DigitalOut led(LED1);

// Interrupt Service Routine (ISR)
void button_pressed_isr() {
    led = !led; // Toggle LED directly in ISR
}

int main() {
    // Enable internal pull-up resistor if the switch pulls to GND
    button.mode(PullUp);

    // Attach callback function to the falling edge (button press)
    button.fall(&button_pressed_isr);

    while (true) {
        // Main thread sleeps to save power until an interrupt wakes the MCU
        sleep();
    }
}
