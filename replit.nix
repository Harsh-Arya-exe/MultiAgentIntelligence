{pkgs}: {
  deps = [
    pkgs.rustc
    pkgs.libiconv
    pkgs.cargo
    pkgs.xdg-utils
    pkgs.freefont_ttf
  ];
}
