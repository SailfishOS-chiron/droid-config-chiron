# ../droid-configs-device/droid-configs.inc
%define device chiron
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Mi Mix 2 (chiron)
%define dcd_path ./
# Adjust this for your device
%define pixel_ratio 2.0

# Community HW adaptations need this
%define community_adaptation 1

# We assume most devices will
%define have_modem 1

# Device-specific ofono configuration
Provides: ofono-configs
Obsoletes: ofono-configs-mer

Provides: usb-moded-configs
Obsoletes: usb-moded-defaults

%include droid-configs-device/droid-configs.inc

%pretrans -p <lua>
path = "/lib/firmware"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end
