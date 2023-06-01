/*
 * SPDX-FileCopyrightText: 2010-2022 Espressif Systems (Shanghai) CO LTD
 *
 * SPDX-License-Identifier: CC0-1.0
 */
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "driver/gpio.h"
#include "driver/i2c.h"
#include "u8g2.h"

#define LED_GPIO 27
#define SDA_PIN 16
#define SCL_PIN 17

void app_main() {
    // initialize the LED GPIO pin as output
    gpio_set_direction(LED_GPIO, GPIO_MODE_OUTPUT);
    gpio_set_direction(2, GPIO_MODE_OUTPUT);

    int level = 0;
    while (1) {
        gpio_set_level(LED_GPIO, level);
        gpio_set_level(2, !level);
        level = !level;

        vTaskDelay(2000 / portTICK_PERIOD_MS);
    }
}
