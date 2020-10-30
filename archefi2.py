from os import system

system('pacman -Sy')
system('pacman -S grub-efi-x86_64 efibootmgr')
system('grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=arch_grub --recheck')
system('grub-mkconfig -o /boot/grub/grub.cfg')
system('pacman -S dhcpcd')
system('systemctl enable dhcpcd')
system('passwd')