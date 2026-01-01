# Pairing Headphones via Bluetooth in Ubuntu

A step-by-step guide to connect Bluetooth headphones using `bluetoothctl` on Ubuntu.

## Prerequisites

- Bluetooth headphones in pairing mode
- Ubuntu system with Bluetooth support
- Terminal access

## Steps

### 1. Open the Bluetooth Controller

```bash
# Open terminal (CTRL + Alt + T)
bluetoothctl
```

### 2. Enable Bluetooth

```bash
# Power on Bluetooth
power on
```

### 3. Enable Pairing Mode on Your Headphones

Press and hold the power button for more than 7 seconds until you hear a pairing tone or see a pairing indicator.

### 4. Scan for Available Devices

```bash
# Start scanning
scan on
```

Multiple MAC addresses will appear representing nearby Bluetooth devices. Look for your headphone's name in the output:

```
[DEVICE] XX:XX:XX:XX:XX headphone-name
```

### 5. Stop Scanning and Pair

```bash
# Stop scanning
scan off

# Pair with your device (replace XX:XX:XX:XX:XX with your headphone's MAC address)
pair XX:XX:XX:XX:XX

# Trust the device
trust XX:XX:XX:XX:XX

# Connect to the device
connect XX:XX:XX:XX:XX
```

### 6. Exit

```bash
# Exit the Bluetooth controller
exit
```

## Success Indicator

Your headphones should now be connected and ready to use.
