{
  description = "nix flake for deepfrier";

  inputs = {
    nixpkgs = {
      url = "github:NixOS/nixpkgs/nixos-21.05";
    };
  };

  outputs = inputs:
    let
      pkgs = import inputs.nixpkgs { localSystem = "x86_64-linux"; };
      deepfry =
        pkgs.stdenv.mkDerivation {
          name = "deepfrier";
          version = 1.0;
          src = pkgs.lib.cleanSource ./.;
          meta = with pkgs.lib; {
            description = "A deepfrier";
            homepage = "https://github.com/DieracDelta/deepfry";
            license = licenses.mit;
            platforms = platforms.linux;
          };

          nativeBuildInputs = [ pkgs.makeWrapper ];


          installPhase = ''
            mkdir -p $out/bin/
            mkdir -p $out/lib/
            cp frier.py $out/bin/
            cp bsmol.png $out/lib/
            chmod +x $out/bin/frier.py
          '';


          postFixup = ''
            makeWrapper $out/bin/frier.py $out/bin/deepfry --set-default B_LOCATION $out/lib/bsmol.png --set-default DISPLAY_FRONTEND X11 --prefix PATH : ${pkgs.lib.makeBinPath [ pkgs.imagemagick pkgs.xclip pkgs.maim (pkgs.python3.withPackages (ps: with ps; [ pillow tesserocr ])) ] }
          '';
        };
    in
    {
      packages.x86_64-linux.deepfry = deepfry;
      defaultPackage.x86_64-linux = deepfry;
      defaultApp.x86_64-linux = {
        type = "app";
        program = "${deepfry}/bin/deepfry";
      };
    };
}
