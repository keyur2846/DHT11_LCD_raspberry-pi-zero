# 🌡️ DHT11 + 16x2 LCD on Raspberry Pi Zero W

This project reads **temperature and humidity** data using a **DHT11 sensor** and displays it on a **16x2 LCD** via **I2C**, all powered by a **Raspberry Pi Zero W**.

---

## 📦 Components Used

### Required:
1. 🧠 Raspberry Pi (any model, tested on Pi Zero W)
2. 🌡️ DHT11 Temperature & Humidity Sensor
3. 🖥️ 16x2 LCD Display with I2C adapter

### Optional (for portable use):
4. 🔋 TP4056 Li-ion Battery Charging Module
5. 🔋 3.7V Li-ion Battery (e.g., 18650 or flat cell)

---

## 🛠️ How It Works

- The **DHT11 sensor** reads temperature and humidity every few seconds.
- The data is then printed to a **16x2 LCD** using the I2C protocol.
- The entire system can run off a battery using the **TP4056 module** for charging and protection.

---

## 🗂️ Project Structure

