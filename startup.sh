#!/bin/bash

# after installation
sudo pacman -S intel-ucode xorg xorg-server xorg-apps xf86-video-intel xf86-input-libinput mesa mesa-utils xorg-xinit intel-media-driver libva-utils libva-vdpau-driver libva-intel-driver libvdpau-va-gl vdpauinfo intel-gpu-tools --needed && sudo grub-mkconfig -o /boot/grub/grub.cfg

# general packages
sudo pacman -S firefox firefox-i18n-ru firefox-i18n-en-us firefox-spell-ru telegram-desktop gcc gdb nodejs neovim npm python-pip jre-openjdk-headless jre-openjdk jdk-openjdk openjdk-doc openjdk-src libreoffice-still libreoffice-still-ru hunspell hunspell-ru hunspell-en_us thunderbird thunderbird-i18n-ru thunderbird-i18n-en-us vlc rsync git gtk-engine-murrine sassc transmission-gtk gthumb gparted cmake lsd unzip wget xreader --needed
python3 -m pip install --user --upgrade pynvim

# packages for WM
sudo pacman -S flameshot feh lxsession-gtk3 xorg-xbacklight qt5ct alacritty xmonad xmonad-contrib xmobar breeze dmenu lxappearance --needed

# alsa
#sudo pacman -S alsa-utils alsa-tools --needed

# pipewire
# sudo pacman -S pipewire pipewire-jack pipewire-alsa pipewire-pulse --needed

# bluetooth
#sudo pacman -S bluez bluez-utils blueman --needed && sudo systemctl enable bluetooth

# delete packages from gnome de
# sudo pacman -Rsn totem sushi simple-scan nano gnome-weather gnome-photos gnome-maps gnome-contacts gnome-clocks gnome-calendar gnome-boxes gnome-books eog epiphany cheese --needed

#sudo pacman -Scc


# themes
#cd ~ && git clone https://github.com/vinceliuice/Qogir-theme.git && cd Qogir-theme && ./install.sh
#cd ~ && git clone https://github.com/vinceliuice/Graphite-gtk-theme.git && cd Graphite-gtk-theme && ./install.sh -t blue --tweaks rimless normal && cd wallpaper && ./install-wallpapers.sh
#cd ~ && git clone https://github.com/vinceliuice/Tela-icon-theme.git && cd Tela-icon-theme && ./install.sh
#cd ~ && git clone https://github.com/vinceliuice/Orchis-theme.git && cd Orchis-theme && ./install.sh --tweaks solid
#cd ~ && rm -rf Qogir-theme Graphite-gtk-theme Tela-icon-theme Orchis-theme


# JetBrainsMono font
#wget https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/JetBrainsMono.zip &&
#mkdir JetBrainsMono &&
#unzip -d JetBrainsMono JetBrainsMono.zip &&
#mkdir -p ~/.local/share/fonts &&
#mv JetBrainsMono ~/.local/share/fonts/ &&
#rm -rf JetBrainsMono.zip

# Oh My Zsh
# sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" &&
# git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
# git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
# git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
